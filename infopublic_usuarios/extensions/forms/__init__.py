from ast import Sub
from logging.config import valid_ident
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class ChamadosForm(FlaskForm):
    entidade = StringField('Entidade:', validators=[DataRequired()])
    sistema = SelectField(
        'Sistema:', choices=[
            ('PJPCTB', 'Contabilidade'),
            ('PJFolha', 'Folha'),
            ('PJTributos', 'Tributos'),
            ('PJFrota', 'Frota'),
            ('PJCheque', 'Cheque/Tesouraria'),
            ('PJDoacao', 'Doação/Concessão'),
            ('PJTomb', 'Tombamento')
        ], validators=[DataRequired()]
    )
    assunto = StringField('Assunto:', validators=[DataRequired()])
    descricao = TextAreaField('Descriçao do problema:', validators=[DataRequired()])
    detalhes = TextAreaField('Passo-a-passo de como reproduzir o erro: ', 
                                validators=[DataRequired()])
    submit = SubmitField('Abrir chamado')
