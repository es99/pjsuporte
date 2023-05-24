from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user
from infopublic_usuarios.blueprints.main.funcoes import trata_cpf, retorna_username
from infopublic_usuarios.extensions.db import User, db, ChamadosTicket

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = trata_cpf(request.form['login'])
        password = request.form['password']
        if (not login) or (not password):
            flash("Falta inserir login e/ou senha")
        user = User.query.filter_by(cpf=login).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Login ou senha inválidos!')
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash('Usuário deslogado com sucesso.')
    return redirect(url_for('auth.login'))

@auth.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        cpf = trata_cpf(request.form['cpf'])
        nome = request.form['nome'].title()
        email = request.form['email']
        senha = request.form['password']
        senha2 = request.form['confirma_password']
        if (len(senha) >= 6) and (senha == senha2):
            if cpf and nome and email:
                user = User.query.filter_by(cpf=cpf).first()
                if user is None:
                    username = retorna_username(nome)
                    user = User(cpf=cpf, username=username, nome=nome,
                        email=email, password=senha)
                    db.session.add(user)
                    db.session.commit()
                    flash('Registro realizado com sucesso!')
                    return redirect(url_for('auth.login'))
                else:
                    flash(f"Este cpf {cpf} já encontra-se registrado.")
            else:
                flash('Preencha todos os campos!')
        else:
            flash('A senha não atende os requisitos de complexidades ou não são iguais!')
    return render_template('auth/registro.html')

@auth.route('/chamado/<id>', methods=['GET', 'POST'])
def visualiza_chamado(id):
    chamado = ChamadosTicket.query.filter_by(id=id).first()
    id = chamado.id
    status = chamado.status
    data = chamado.data
    cpf = chamado.cpf
    nome = chamado.nome
    sistema = chamado.sistema
    autor_chamado = chamado.author
    entidade = chamado.entidade
    assunto = chamado.assunto
    descricao = chamado.descricao
    detalhes = chamado.detalhes
    solucao_chamado = chamado.solucao
    if request.method == 'POST':
        solucao_form = request.form['solucao']
        if solucao_form:
            chamado.status = 2
            chamado.solucao = solucao_form
            try:
                db.session.add(chamado)
                db.session.commit()
            except:
                flash("Erro ao atualizar o chamado, consulte o administrador.")
            return redirect(url_for('main.fila_chamados'))
        else:
            flash("Insira uma solução antes de atualizar o chamado!")
    return render_template('visualiza_chamados.html', status=status, data=data, id=id,
            descricao=descricao, assunto=assunto, entidade=entidade, detalhes=detalhes,
            cpf=cpf, nome=nome, autor_chamado=autor_chamado, sistema=sistema,
            solucao_chamado=solucao_chamado)

@auth.route('/chamado_fechado/<id>')
def chamado_fechado(id):
    chamado = ChamadosTicket.query.filter_by(id=id).first()
    chamado.status = 3
    db.session.add(chamado)
    db.session.commit()
    return render_template('chamado_fechado.html', id=id)