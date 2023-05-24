from ast import Attribute
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from infopublic_usuarios.extensions.login import login_manager

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)

class ChamadosTicket(db.Model):
    __tablename__ = "chamados"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, index=True)
    data = db.Column(db.String(64), index=True)
    cpf = db.Column(db.String(64), index=True, nullable=False)
    nome = db.Column(db.String(64), unique=False, index=True, nullable=False)
    sistema = db.Column(db.String(64), unique=False, index=True)
    entidade = db.Column(db.String(120))
    assunto = db.Column(db.String(120), unique=False, index=True)
    descricao = db.Column(db.Text, unique=False, nullable=False)
    detalhes = db.Column(db.Text, unique=False, nullable=False)
    solucao = db.Column(db.Text, unique=False, nullable=True)
    author = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'Ticket id: {self.id}'

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(64), index=True, nullable=False)
    nome = db.Column(db.String(64), index=True, nullable=False)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f"{self.cpf}"

    @property
    def password(self):
        raise AttributeError('password não é um atributo de leitura')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))