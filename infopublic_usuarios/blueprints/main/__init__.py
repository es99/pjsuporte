from .main_views import main

def init_app(app):
    app.register_blueprint(main)