from flask import Blueprint, render_template, request, flash, redirect, url_for
from infopublic_usuarios.extensions.forms import ChamadosForm
from infopublic_usuarios.extensions.db import db, ChamadosTicket
from infopublic_usuarios.extensions.email import send_email
from flask_login import login_required, current_user
from datetime import date, datetime
from .funcoes import trata_cpf
import boto3, os


main = Blueprint('main', __name__)

dynamodb = boto3.resource(
    'dynamodb',
    region_name='sa-east-1'
)
table = dynamodb.Table('usuarios')
solicitacoes = dynamodb.Table('solicitacoes_cadastro')


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    contagem_de_itens = table.item_count
    if request.method == 'POST':
        cpf = request.form['cpf']
        if not cpf:
            flash('Faltou inserir o CPF!')
        else:
            cpf_validado = trata_cpf(cpf)
            usuario = dict(cpf=cpf_validado)
            response = table.get_item(Key=usuario)
            if ('Item' in response):
                return redirect(url_for('main.user', cpf_num=cpf_validado))
            flash('CPF não encontrado no sistema, cadastre com os dados necessários o novo CPF.')
        return redirect(url_for('main.index'))
    return render_template('index.html', num_itens = contagem_de_itens)

@main.route('/mail_confirma/<string:cpf>', methods=['GET', 'POST'])
@login_required
def email_confirma(cpf):
    usuario = {'cpf': cpf}
    response = table.get_item(Key=usuario)
    item = response['Item']

    return render_template('confirma_email.html', item=item)


@main.route('/user/<string:cpf_num>', methods=['GET', 'POST'])
@login_required
def user(cpf_num):
    usuario = dict(cpf=cpf_num)
    response = table.get_item(Key=usuario)
    item = response['Item']
    if request.method == "POST":
        email = item['email']
        if not email:
            flash("O usuário em questão não possui o campo email preenchido")
        else:
            dados = dict(nome=item['nome'], cpf=item['cpf'],
                         senha_ts=item['senha_ts'], senha_sistema=item['senha_sistema'])
            try:
                send_email(email, **dados)
                return redirect(url_for('main.email_confirma', cpf=dados['cpf']))
            except:
                flash("Infelizmente, por alguma razão, e email não pôde ser enviado.")
    return render_template('usuario.html', item=item)


@main.route('/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro():
    if request.method == 'POST':
        d = datetime.now()
        data = d.strftime("%d-%m-%Y - %H:%M")
        cpf = trata_cpf(request.form['cpf'])
        nome = request.form['nome'].title()
        email = request.form['email'].lower()
        entidade = request.form['entidade'].title()
        sistema = request.form.getlist('sistema')
        tel = request.form['tel']
        rg = request.form['rg']
        nome_solicitante = request.form['nome_solicitante']
        cpf_solicitante = trata_cpf(request.form['cpf_solicitante'])
        senha_ts = request.form['senha_ts']
        senha_sistema = request.form['senha_sistema']
        permissao = request.form['permissao']
        data_cadastro = data
        usuario = dict(cpf=cpf, nome=nome, email=email, tel=tel, nome_solicitante=nome_solicitante,
                        rg=rg, senha_ts=senha_ts, senha_sistema=senha_sistema, cpf_solicitante=cpf_solicitante,
                            data_cadastro=data_cadastro, entidade=entidade,
                            sistema=sistema, permissao=permissao)
        try:                    
            table.put_item(Item=usuario)
            flash(f"Usuário {nome}-{cpf} cadastrado com sucesso")
        except:
            flash("Falha ao cadastrar usuário")
        return redirect(url_for('main.cadastro'))
    return render_template('cadastro.html')


@main.route('/chamados/<string:cpf>', methods=['GET', 'POST'])
@login_required
def chamados(cpf):
    form = ChamadosForm()
    usuario = dict(cpf=cpf)
    response = table.get_item(Key=usuario)
    item = response['Item']
    d = datetime.now()
    author = current_user
    data = d.strftime("%d/%m/%Y - %H:%M")
    if form.validate_on_submit():
        entidade = form.entidade.data
        sistema = form.sistema.data
        assunto = form.assunto.data
        descricao = form.assunto.data
        detalhes = form.detalhes.data
        chamado = ChamadosTicket(status=1, data=data, cpf=cpf, nome=item['nome'],
                    sistema=sistema, entidade=entidade, assunto=assunto, descricao=descricao,
                    detalhes=detalhes, author=author)
        try:
            db.session.add(chamado)
            db.session.commit()
            flash("Chamado cadastrado com sucesso, aguarde o suporte.")
        except:
            flash("Erro ao cadastrar o chamado!, consulte o administrador.")
        return redirect(url_for('main.chamados', cpf=cpf))
    return render_template("chamados.html", form=form, cpf=cpf, nome=item['nome'], data=data)


@main.route('/solicitar_cadastro', methods=['GET', 'POST'])
@login_required
def solicita_cadastro():
    if request.method == 'POST':
        cpf = trata_cpf(request.form['cpf'])
        nome = request.form['nome'].title()
        email = request.form['email'].lower()
        entidade = request.form['entidade'].capitalize()
        sistema = request.form.getlist('sistema')
        tel = request.form['tel']
        if (not cpf) or (not nome) or (not email) or (not entidade) or (not sistema) \
            or (not tel):
            flash("Preencha as informações obrigatórias!")
        else:
            rg = request.form['rg']
            comentario = request.form['comentario']
            d = datetime.now()
            data = d.strftime("%d/%m/%Y - %H:%M")
            author = str(current_user)
            chamado = dict(cpf=cpf, nome=nome, email=email, entidade=entidade,
                            sistema=sistema, tel=tel, rg=rg, comentario=comentario,
                            status=1, data_abertura=data, author=author)
            try:
                solicitacoes.put_item(Item=chamado)
                flash(f"Solicitação de cadastro feita com sucesso, favor aguardar")
            except:
                flash("Erro ao cadastrar chamado, contactar administrador")
        return redirect(url_for('main.solicita_cadastro'))
    return render_template('solicita_cadastro.html')


@main.route('/fila_cadastros', methods=['GET', 'POST'])
@login_required
def fila_cadastros():
    response = solicitacoes.scan()
    data = response['Items']
    return render_template('fila_cadastros.html', data=data)


@main.route('/fila_chamados', methods=['GET', 'POST'])
@login_required
def fila_chamados():
    data = ChamadosTicket.query.all()
    return render_template('fila_chamados.html', data=data)


@main.route('/lista_chamados_fechados')
@login_required
def lista_chamados_fechados():
    data = ChamadosTicket.query.filter_by(status=3).all()
    return render_template('lista_chamados_fechados.html', data=data)