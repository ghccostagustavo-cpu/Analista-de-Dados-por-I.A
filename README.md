# Analista IA — Text-to-SQL com LLM Local

Script de conversão de linguagem natural para SQL utilizando LLM local via Ollama. O usuário descreve a consulta desejada em português e o modelo interpreta, gera o comando SQL correspondente e executa diretamente no banco de dados. A interface visual é construída com Streamlit.

## Como funciona

O script recebe uma pergunta em linguagem natural via interface Streamlit, monta um prompt com as instruções e o envia para o modelo via API REST local (Ollama). O modelo retorna o SQL gerado, que é validado e executado no banco. O resultado é exibido na interface formatado via Pandas DataFrame.

## Segurança

O modelo é instruído via system prompt a aceitar apenas comandos `SELECT`. Qualquer tentativa de executar `INSERT`, `UPDATE`, `DELETE`, `DROP` ou similares é bloqueada antes da execução. Todas as interações são registradas em log com timestamp para auditoria.

## Versões

### PostgreSQL (versão atual)

Utiliza SQLAlchemy com o driver `psycopg2` para conexão com banco PostgreSQL. As credenciais são carregadas via `.env`.

**Dependências:**

```
openai
pandas
sqlalchemy
psycopg2-binary
streamlit
python-dotenv
```

**Configuração — arquivo `.env`:**

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
OLLAMA_API_KEY=ollama
caminho_log=caminho/do/log.txt
```

**Execução:**

```bash
streamlit run Analista_IA.py
```

---

### SQLite (versão anterior)

Utiliza `sqlite3` nativo para conexão com banco local. Os caminhos são definidos diretamente no script.

**Dependências:**

```
openai
pandas
sqlite3 (nativo)
streamlit
```

**Configuração — início do script:**

```python
caminho_banco = r"caminho/do/banco.db"
caminho_log   = r"caminho/do/log.txt"
```

**Execução:**

```bash
streamlit run Analista_IA.py
```

---

## Stack

| Componente     | PostgreSQL                                      | SQLite                        |
|----------------|-------------------------------------------------|-------------------------------|
| LLM            | Llama 3.2 8B via Ollama                         | Llama 3.2 3B via Ollama       |
| Comunicação    | API REST local (OpenAI SDK → `localhost:11434`) | API REST local (OpenAI SDK → `localhost:11434`) |
| Banco de dados | PostgreSQL via SQLAlchemy + psycopg2            | SQLite nativo                 |
| Processamento  | Pandas                                          | Pandas                        |
| Interface      | Streamlit                                       | Streamlit                     |
| Configuração   | `.env` via python-dotenv                        | Variáveis no script           |

## Pré-requisitos

O Ollama deve estar instalado e rodando localmente:

```bash
ollama serve
ollama pull llama3.2:8b   # versão PostgreSQL
ollama pull llama3.2:3b   # versão SQLite
```

## Observações

Processamento 100% local — nenhum dado trafega para servidores externos.
