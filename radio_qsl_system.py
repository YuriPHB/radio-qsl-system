import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Dados do email remetente (configure com seu email e senha do app)
EMAIL = "seu_email@gmail.com"
SENHA = "sua_senha_de_app"  # Senha de app do Gmail (não a senha normal!)

# Lista para armazenar contatos e comunicações
contatos = []
comunicacoes = []

def enviar_email(destino, assunto, mensagem):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = destino
        msg['Subject'] = assunto

        msg.attach(MIMEText(mensagem, 'plain'))

        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL, SENHA)
        servidor.send_message(msg)
        servidor.quit()
        print(f"✅ Email enviado para {destino} com sucesso!\n")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}\n")

def cadastrar_contato():
    print("=== Cadastrar Contato ===")
    indicativo = input("Indicativo: ").strip().upper()
    nome = input("Nome completo: ").strip()
    email = input("Email para contato: ").strip()

    # Verifica se já existe contato com mesmo indicativo
    for c in contatos:
        if c['indicativo'] == indicativo:
            print("⚠️ Contato com esse indicativo já cadastrado!\n")
            return

    contato = {
        'indicativo': indicativo,
        'nome': nome,
        'email': email
    }
    contatos.append(contato)
    print(f"✅ Contato {indicativo} cadastrado com sucesso!\n")

def listar_contatos():
    print("=== Lista de Contatos ===")
    if not contatos:
        print("Nenhum contato cadastrado.\n")
        return
    for c in contatos:
        print(f"Indicativo: {c['indicativo']} | Nome: {c['nome']} | Email: {c['email']}")
    print()

def registrar_comunicacao():
    print("=== Registrar Comunicação ===")
    indicativo = input("Indicativo do contato: ").strip().upper()

    # Procura contato
    contato = None
    for c in contatos:
        if c['indicativo'] == indicativo:
            contato = c
            break
    if contato is None:
        print("⚠️ Contato não encontrado. Cadastre o contato antes.\n")
        return

    data_hora = input("Data e hora da comunicação (dd/mm/aaaa HH:MM) ou Enter para agora: ").strip()
    if not data_hora:
        data_hora = datetime.datetime.now()
    else:
        try:
            data_hora = datetime.datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        except ValueError:
            print("⚠️ Formato inválido. Use dd/mm/aaaa HH:MM\n")
            return

    detalhes = input("Detalhes da comunicação (ex: frequência, localização, modo): ").strip()

    registro = {
        'indicativo': contato['indicativo'],
        'nome': contato['nome'],
        'email': contato['email'],
        'data_hora': data_hora,
        'detalhes': detalhes
    }
    comunicacoes.append(registro)
    print(f"✅ Comunicação registrada para {contato['indicativo']} em {data_hora}.\n")

    # Pergunta se quer enviar confirmação por email
    enviar = input("Enviar confirmação por email? (s/n): ").strip().lower()
    if enviar == 's':
        assunto = f"Confirmação de Comunicação - {data_hora.strftime('%d/%m/%Y %H:%M')}"
        mensagem = f"Olá {contato['nome']},\n\nConfirmamos a comunicação realizada em {data_hora.strftime('%d/%m/%Y %H:%M')}.\nDetalhes: {detalhes}\n\nAtenciosamente,\nRadio QSL System"
        enviar_email(contato['email'], assunto, mensagem)

def listar_comunicacoes():
    print("=== Comunicações Registradas ===")
    if not comunicacoes:
        print("Nenhuma comunicação registrada.\n")
        return
    for i, c in enumerate(comunicacoes, 1):
        print(f"{i}. Indicativo: {c['indicativo']} | Nome: {c['nome']} | Data/Hora: {c['data_hora'].strftime('%d/%m/%Y %H:%M')}")
        print(f"    Detalhes: {c['detalhes']}")
    print()

def menu():
    print("""
=== Sistema Radio QSL ===

[1] Cadastrar Contato
[2] Listar Contatos
[3] Registrar Comunicação
[4] Listar Comunicações
[0] Sair
""")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()
        if escolha == '1':
            cadastrar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            registrar_comunicacao()
        elif escolha == '4':
            listar_comunicacoes()
        elif escolha == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
