from flask_mail import Mail, Message
from flask import render_template
from infopublic_usuarios.funcoes_extras import msg_textplain

mail = Mail()


def init_app(app):
    mail.init_app(app)

#def send_mail(to, nome, cpf, senha, senha_sistema):
def send_email(to, nome, cpf, senha, senha_sistema):
    subject = '[Suporte Infopublic] - Credenciais de Acesso'
    sender = 'Suporte <suporte@infopublic.com.br>'

    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = msg_textplain.mensagem_text(nome=nome, cpf=cpf, senha=senha,
                                    senha_sistema=senha_sistema)
    mail.send(msg)