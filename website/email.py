from flask import Blueprint, request, render_template, url_for, redirect
from openai import OpenAI
from .asst_helper import get_response
from . import asst_email_polisher_id, asst_email_fqr_id, asst_email_meeting_id, asst_email_soft_id, help_text

email = Blueprint('email', __name__)

@email.route('/email/polisher', methods=['GET', 'POST'])
def polisher():
    kwargs = {
        'title': 'Sentences Polisher',
        'help_text': help_text['email_polisher'],
        'important': help_text['email_important'],
        'input_area_text': 'Enter Sentences Needs Paraphrase Here:',
        'button_name': 'Polish',
    }
    if request.method == 'POST':
        user_input = request.form['user_input']
        response=get_response(asst_id=asst_email_polisher_id, user_msg=user_input)
        return render_template('email_base.html', response=response, user_inputed=user_input, **kwargs)
    
    return render_template('email_base.html', **kwargs)

@email.route('/email/fqr', methods=['GET', 'POST'])
def fqr():
    kwargs = {
        'title': 'FQR Helper',
        'help_text': help_text['email_fqr'],
        'how_to': help_text['email_fqr_how_to'],
        'example': help_text['email_fqr_example'],
        'important': help_text['email_important'],
        'input_area_text': 'Enter Case Statement Here:',
        'button_name': 'Get the FQR',
    }
    input_area_text = 'Enter Case Statement Here:'
    if request.method == 'POST':
        user_input = request.form['user_input']
        response=get_response(asst_id=asst_email_fqr_id, user_msg=user_input)
        return render_template('email_base.html', response=response, user_inputed=user_input, **kwargs)
    
    return render_template('email_base.html', **kwargs)

@email.route('/email/meeting', methods=['GET', 'POST'])
def meeting():
    kwargs = {
        'title': 'Meeting Summary Helper',
        'help_text': help_text['email_meeting'],
        'example': help_text['email_meeting_example'],
        'important': help_text['email_important'],
        'input_area_text': 'Enter Meeting Notes Here:',
        'button_name': 'Get the summary email',
    }
    if request.method == 'POST':
        user_input = request.form['user_input']
        response=get_response(asst_id=asst_email_meeting_id, user_msg=user_input)
        return render_template('email_base.html', response=response, user_inputed=user_input, **kwargs)
    
    return render_template('email_base.html', **kwargs)

@email.route('/email/softskillmaster', methods=['GET', 'POST'])
def softskillmaster():
    kwargs = {
        'title': 'Soft Skill Master',
        'help_text': help_text['email_softskillmaster'],
        'how_to': help_text['email_softskillmaster_how_to'],
        'example': help_text['email_softskillmaster_example'],
        'important': help_text['email_important'],
        'input_area_text': 'Enter Detailed Scenario Here:',
        'button_name': 'Soft it',
    }
    if request.method == 'POST':
        user_input = request.form['user_input']
        response=get_response(asst_id=asst_email_soft_id, user_msg=user_input)
        return render_template('email_base.html', response=response, user_inputed=user_input, **kwargs)
    
    return render_template('email_base.html', **kwargs)