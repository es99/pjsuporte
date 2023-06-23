from flask import Blueprint
from datetime import datetime
from infopublic_usuarios.extensions.db import db
from flask import redirect, url_for
from flask import render_template, request, flash
from infopublic_usuarios.extensions.db import Cadastros
from infopublic_usuarios.blueprints.main.funcoes import trata_cpf

solicita_cadastro = Blueprint('solicita_cadastro', __name__)

@solicita_cadastro.route('/solicita_cadastro', methods=['GET', 'POST'])
def sol_cadastro():
    if request.method == 'POST':
        cpf = trata_cpf(request.form['cpf'])
        user = Cadastros.query.filter_by(cpf=cpf).first()
        if user is not None:
            flash('Este CPF já se encontra na fila de solicitação de cadastros, por favor aguarde o email ' \
                'com as credenciais')
            return redirect(url_for('solicita_cadastro.sol_cadastro'))
        data = datetime.now()
        nome = request.form['nome']
        email = request.form['email']
        tel = request.form['tel']
        rg = request.form['rg']
        entidade = request.form['entidade']
        sistema = request.form['sistema']
        nome_solicitante = request.form['nome_solicitante']
        cpf_solicitante = trata_cpf(request.form['cpf_solicitante'])
        solicitacao = Cadastros(nome=nome, cpf=cpf, tel=tel, email=email, data=data,
                                rg=rg, entidade=entidade, sistema=sistema, nome_solicitante=nome_solicitante,
                                cpf_solicitante=cpf_solicitante)
        db.session.add(solicitacao)
        db.session.commit()
        flash(f"A solicitação de cadastro foi enviada com sucesso, pedimos que aguarde o email com as credenciais")
        return redirect(url_for('solicita_cadastro.sol_cadastro'))

    return render_template('novos_cadastros/sol_cadastro.html')