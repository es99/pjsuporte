from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from infopublic_usuarios.extensions.db import db, User, Cadastros

admin = Admin()


class UserView(ModelView):
    can_delete = False
    can_edit = False
    can_create = False


class CadastroView(ModelView):
    can_view_details = True
    can_edit = False
    can_create = False


admin.add_view(UserView(User, db.session))
admin.add_view(CadastroView(Cadastros, db.session))


def init_app(app):
    admin.init_app(app)
