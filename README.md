# Meu Projeto

Uma aplicação FastAPI simples com estrutura de pastas organizada para rotas, templates e arquivos estáticos.

## Executar localmente

1. Crie um virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

Acesse `http://127.0.0.1:8000/`.
