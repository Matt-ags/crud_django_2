# 🐍 Projeto Django - Relembrando Django

Este projeto é um exemplo simples feito com Django, contendo rotas, formulários e operações básicas com o banco de dados.

[![Acesse o Projeto](https://img.shields.io/badge/Acessar%20Projeto-Online-blue?style=for-the-badge&logo=django)](https://mattzin.pythonanywhere.com/)


## 📥 Clonando o repositório

Para copiar este projeto para a sua máquina, use o comando:

```bash
  git clone https://github.com/Matt-ags/relembrando-django.git
```
Depois, entre na pasta do projeto:
```bash
  cd relembrando-django
```

## ▶️ Executando o projeto

Para iniciar o servidor localmente, siga estes passos:

1. Certifique-se de que o ambiente virtual está ativado:

```bash
  python3 -m venv venv
```

```bash
  source venv/bin/activate      # Linux/macOS
  # ou
  venv\Scripts\activate         # Windows
```

2. Execute as migrações para criar o banco de dados:

```bash
  python manage.py migrate
```

3. Inicie o servidor de desenvolvimento do Django:

```bash
  python manage.py runserver
```
