#!/usr/bin/bash

FLASK_APP="flasky.py"
FLASK_DEBUG=1
FLASK_ENV="development"
FLASK_CONFIG="development"
SECRET_KEY="pjsuporte_secret"


LINE="------------------------------------------------------------------"
HEADER="
$LINE
Description: Seta as variáveis de ambiente para iniciar o FLASK
$LINE
FLASK_APP
FLASK_DEBUG
FLASK_ENV
FLASK_CONFIG
SECRET_KEY
$LINE
"

echo "$HEADER"
export FLASK_APP
export FLASK_DEBUG
export FLASK_ENV
export FLASK_CONFIG
export SECRET_KEY

sleep 1

echo "Done!"
