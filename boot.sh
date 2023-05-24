#!/bin/sh
source venv/bin/activate

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo flask db upgrade failed, retrying in 5 secs...
done

gunicorn -b 0.0.0.0:8000 flasky:app