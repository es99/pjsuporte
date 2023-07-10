from flask import Blueprint
from datetime import datetime
from infopublic_usuarios.extensions.db import db, Informativos
from infopublic_usuarios.extensions.email import EmailInformativo
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

emails = Blueprint('emails', __name__)

@emails.route('/informativos', methods=['GET', 'POST'])
@login_required
def informativos():
    if request.method == 'POST':
        lista_emails = ['engels.franca@gmail.com', 'suporte@infopublic.com.br', 'engels.franca@icloud.com']
        msg = request.form['mensagem']
        data = datetime.now()
        enviante = current_user
        envio = Informativos(mensagem=msg, enviante=enviante, data=data)
        db.session.add(envio)
        db.session.commit()
        envia = EmailInformativo(lista_emails, msg)
        envia.envia_email()
        flash("Email informativo enviado!")
        return redirect(url_for('emails.informativos'))
    return render_template('informativos/index.html')