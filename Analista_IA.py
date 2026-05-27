import pandas as pd
import sqlite3
from openai import OpenAI
import datetime
#Bbiblioteca Streamlit para exibição visual dos dados
import streamlit as st

#É o título que vai aparecer na interface web
st.title("Analista de Dados por IA")

#Caminho do banco de dados e do arquivo de log 
caminho_log = r"caminho_log"
caminho_banco = r"caminho_banco"

#Configuração do cliente OpenAI para usar o modelo via Ollama
client = OpenAI(api_key="ollama", base_url="localhost")

#Solicita ao usuário uma consulta em linguagem natural para ser convertida em SQL
pergunta = st.text_input("Digite uma query que você deseja fazer em SQL: ")

#Envia a consulta para o modelo de linguagem, define os parâmetros de funcionamento
response = client.chat.completions.create(model="llama3.2:3b", temperature=0.3, max_tokens=500, stream=False,
    messages=[
        {"role": "system", "content":
         "Você é um especialista em SQLite que traduz linguagem natural apenas para comandos SELECT. "
         "É estritamente proibido retornar qualquer comando de modificação (INSERT, UPDATE, DELETE, DROP, etc). "
         "Se o usuário solicitar modificações, responda exatamente: 'Procure o setor de T.I. Log registrado'. "
         "Se a pergunta não for sobre SQL, responda apenas: 'Desculpe, não posso ajudar com isso.'. "
         "Os nomes de tabela escritos entre aspas no caixa de texto do usuário tem de ser interpretados exatamente como escritos, incluindo acentos e caracteres especiais. "
         "Se o usuário solicitar uma consulta que envolva múltiplas tabelas, use JOINs para relacioná-las. "
         "Não use markdown, não use crases, não use ```sql, adicione o script SQL usado no final. "
         "O elemento de comparação principal deve ser os elementos das colunas 'chave'. "
         "A resposta deve começar diretamente com SELECT."},
        {"role": "user", "content": pergunta}
    ]
)

#Definição da variável resposta sendo igual à resposta gerada pela IA
resposta = response.choices[0].message.content.strip()

#Exibição da query em SQL
print(response.choices[0].message.content)

#Por motivos de segurança e controle, registros de log para vermos o que tem sido executado
#(em casos de falha de segurança, veremos que hora que foi executado um comando DELETE, por exemplo)
with open(caminho_log, "a") as log:
    log.write(f"{datetime.datetime.now()}: Pergunta: {pergunta}\nResposta: {resposta}\n")

#Abre a conexão com o banco de dados
conexao = sqlite3.connect(caminho_banco)

#Executa a query no banco de dados
df_qry = pd.read_sql_query(f"{resposta}", conexao)

#Fecha a conexão com o banco de dados
conexao.close()

#Exibe os resultados na interface: Os dados e o script SQL no final pro usuário que tem mais experiência saber o script que foi feito
st.write(df_qry)
st.write(resposta)
