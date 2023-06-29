from .views import solicita_cadastro

def init_app(app):
    app.register_blueprint(solicita_cadastro)