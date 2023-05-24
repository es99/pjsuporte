import os
from infopublic_usuarios.app import create_app

app = create_app(os.getenv('FLASK_CONFIG'))