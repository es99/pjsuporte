from flask import Blueprint
from flask import render_template

emails = Blueprint('emails', __name__)

@emails.route('/informativos', methods=['GET', 'POST'])
def informativos():
    return render_template('informativos/index.html')