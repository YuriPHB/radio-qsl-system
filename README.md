# Radio QSL System

Sistema simples para registro de comunicações de rádio (QSL), cadastro de contatos, gerenciamento de comunicações e envio automático de confirmações por email.

---

## Funcionalidades

- Cadastro de contatos com indicativo, nome e email
- Registro de comunicações com data, hora e detalhes
- Envio de confirmação por email após registro
- Listagem de contatos e comunicações registradas

---

## Requisitos

- Python 3.x
- Biblioteca padrão (smtplib, email)
- Conta Gmail com senha de app para envio de emails

---

## Configuração

1. No arquivo `main.py`, configure as variáveis:

```python
EMAIL = "seu_email@gmail.com"
SENHA = "sua_senha_de_app"
