from flask import Blueprint
from flask import render_template

solicita_cadastro = Blueprint('solicita_cadastro', __name__)

@solicita_cadastro.route('/solicita_cadastro', methods=['GET', 'POST'])
def sol_cadastro():
    return render_template('novos_cadastros/sol_cadastro.html')