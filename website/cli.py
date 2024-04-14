from flask import Blueprint, request, render_template, url_for, redirect
from openai import OpenAI
from .asst_helper import get_response
from . import asst_cli_id, help_text

cli = Blueprint('cli', __name__)

@cli.route('/cli', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input != '':
            response = ''
            response = get_response(asst_id=asst_cli_id, user_msg=user_input)
            return render_template(
                'cli.html',
                title='CL Guru',
                help_text=help_text['cli_help_text'], 
                response=response, 
                )
        else:
            return redirect(url_for('cli.root'))

    return render_template(
        'cli.html', 
        title='CL Guru', 
        help_text=help_text['cli_help_text'])