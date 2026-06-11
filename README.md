Script de conversão de linguagem natural para SQL utilizando LLM local via Ollama. O usuário descreve a consulta desejada em português e o modelo interpreta, gera o comando SQL correspondente e executa diretamente no banco de dados.
Como funciona
O script recebe uma pergunta em linguagem natural, monta um prompt com as instruções e envia para o modelo via API REST local (Ollama). O modelo retorna o SQL gerado, que é validado e executado no banco. O resultado é exibido no terminal formatado via Pandas.
Segurança
O modelo é instruído via system prompt a aceitar apenas comandos SELECT. Qualquer tentativa de executar INSERT, UPDATE, DELETE, DROP ou similares é bloqueada antes da execução. Todas as interações são registradas em log com timestamp para auditoria.
Dependências
openai
pandas
sqlite3 (nativo)
tabulate
Configuração
Definir os caminhos no início do script:
pythoncaminho_banco = r"caminho/do/banco.db"
caminho_log   = r"caminho/do/log.txt"
O Ollama deve estar instalado e rodando localmente com o modelo llama3.2:3b:
bashollama serve
ollama pull llama3.2:3b
Execução
bashpython Analista_IA.py
Stack

LLM: Llama 3.2 3B via Ollama
Comunicação: API REST local (OpenAI SDK apontando para localhost:11434)
Banco: SQLite
Dados: Pandas

Observações
Processamento 100% local. Nenhum dado trafega para servidores externos. Interface visual via Streamlit em desenvolvimento.