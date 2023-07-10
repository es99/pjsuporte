from flask_mail import Mail, Message
from flask import render_template
from infopublic_usuarios.funcoes_extras import msg_textplain

mail = Mail()


def init_app(app):
    mail.init_app(app)

#def send_mail(to, nome, cpf, senha, senha_sistema):
def send_email(to, **kwargs):
    subject = '[Suporte Infopublic] - Credenciais de Acesso'
    sender = 'Suporte <noreply@suporte.infopublic.com.br>'

    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = msg_textplain.mensagem_text(nome=kwargs['nome'], cpf=kwargs['cpf'],
                                senha_ts=kwargs['senha_ts'], senha_sistema=kwargs['senha_sistema'])
    msg.html = render_template('template-email.html', nome=kwargs['nome'],
                        cpf=kwargs['cpf'], senha_ts=kwargs['senha_ts'], 
                        senha_sistema=kwargs['senha_sistema'])
    mail.send(msg)
    
def send_email_informativo(lista_emails, msg):
    subject = '[Informativo Infopublic] - Aviso'
    sender = 'Informativo <noreply@suporte.infopublic.com.br>'
    
    msg = Message(subject, sender=sender, recipients=lista_emails)
    msg.body = msg_textplain.msg_informativo_text(msg)
    msg.html = 