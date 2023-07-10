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
    
    
class EmailInformativo():
    """
    Classe que contem métodos para envio de email
    utilizando o template de envio informativo.
    """
    
    def __init__(self, destinatarios, message):
        """
        :param destinatarios: A lista de destinatarios que receberá
        o email informativo
        """
        self.destinatarios = destinatarios
        self.message = message
        self.subject = "[Informativo Infopublic] - Aviso"
        self.sender = "noreply@suporte.infopublic.com.br"
        
    def envia_email(self):
        """
        :param message: A mensagem informativa que será atrelada ao template do email.
        """
        msg = Message(self.subject, sender=self.sender, recipients=self.destinatarios)
        msg.body = self.message
        msg.html = render_template('/informativos/modelo.html', message=self.message)
        mail.send(msg)