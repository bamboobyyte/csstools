from flask import Blueprint, request, render_template, url_for, redirect
from openai import OpenAI
from .asst_helper import get_response
from . import asst_cli_id, help_text

email = Blueprint('email', __name__)

@email.route('/email/fqr', methods=['GET', 'POST'])
def fqr():
    response='''
    Simple
    output
    from OpenAI
    
    
    '''
    return render_template(
        'email_fqr.html',
        help_text=help_text['email_fqr'],
        response=response)

@email.route('/email/meeting', methods=['GET', 'POST'])
def meeting():
    return render_template(
        'dev.html')
