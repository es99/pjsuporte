from .informativo_views import emails

def init_app(app):
    app.register_blueprint(emails)