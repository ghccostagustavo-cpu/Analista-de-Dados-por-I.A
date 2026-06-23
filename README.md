# Analista IA — Text-to-SQL com LLM Local

Script de conversão de linguagem natural para SQL utilizando LLM local via Ollama. O usuário descreve a consulta desejada em português e o modelo interpreta, gera o comando SQL correspondente e executa diretamente no banco de dados.

## Como funciona

O script recebe uma pergunta em linguagem natural, monta um prompt com as instruções e o envia para o modelo via API REST local (Ollama). O modelo retorna o SQL gerado, que é validado e executado no banco. O resultado é exibido no terminal formatado via Pandas.

## Segurança

O modelo é instruído via system prompt a aceitar apenas comandos `SELECT`. Qualquer tentativa de executar `INSERT`, `UPDATE`, `DELETE`, `DROP` ou similares é bloqueada antes da execução. Todas as interações são registradas em log com timestamp para auditoria.

## Dependências

openai

pandas

sqlite3 (nativo)

sqlalchemy

tabulate


## Configuração

Defina as credenciais de conexão/diretórios no início do script:

```python
DB_HOST     = "localhost"
DB_PORT     = 5432
DB_NAME     = "nome_do_banco"
DB_USER     = "usuario"
DB_PASSWORD = "senha"
caminho_log = r"caminho/do/log.txt"
caminho_banco = r"caminho_sqlite.db"
```

O Ollama deve estar instalado e rodando localmente com o modelo `llama3.2:8b`:

```bash
ollama serve
ollama pull llama3.2:8b
```

## Execução

```bash
python streamlit run Analista_IA_Postgre.py
pyhton streamlit run Analista_IA.py #no caso do sqlite
```

## Stack

| Componente      | Tecnologia                                      |
|-----------------|-------------------------------------------------|
| LLM             | Llama 3.2 8B via Ollama                         |
| Comunicação     | API REST local (OpenAI SDK → `localhost:11434`) |
| Banco de dados  | SQLite e PostgreSQL                             |
| Processamento   | Pandas                                          |

## Observações

Processamento 100% local, nenhum dado trafega para servidores externos. Interface visual via Streamlit em desenvolvimento.
