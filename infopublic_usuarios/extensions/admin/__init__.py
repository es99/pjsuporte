from flask_admin import Admin
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from infopublic_usuarios.extensions.db import db, User, Cadastros, Informativos

admin = Admin(name='Fila de usuários')


class UserView(ModelView):
    can_delete = True
    can_edit = False
    can_create = False
    can_view_details = True

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class CadastroView(ModelView):
    can_view_details = True
    can_edit = False
    can_create = False

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class Emails(ModelView):
    can_view_details = True
    can_edit = False
    can_create = False
    can_delete = False
    
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

admin.add_view(UserView(User, db.session))
admin.add_view(CadastroView(Cadastros, db.session))
admin.add_view(Emails(Informativos, db.session))

def init_app(app):
    admin.init_app(app)
