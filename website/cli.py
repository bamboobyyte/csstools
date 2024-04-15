from flask import Blueprint, request, render_template, url_for, redirect
from openai import OpenAI
from .asst_helper import get_response
from . import asst_cli_id, help_text

cli = Blueprint('cli', __name__)

@cli.route('/cli', methods=['GET', 'POST'])
def root():
    kwargs = {
        'title': 'CL Guru',
        'help_text': help_text['cli_help_text'],
        'how_to': help_text['cli_how_to']
    }
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = get_response(asst_id=asst_cli_id, user_msg=user_input)
        return render_template(
            'cli.html',
            response=response, 
            **kwarg
            )

    return render_template(
        'cli.html', **kwargs)