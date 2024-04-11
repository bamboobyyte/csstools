from flask import Blueprint, request, render_template, url_for
import yaml
import os

cli = Blueprint('cli', __name__)

@cli.route('/cli', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        os_type = request.form['os_type']
        shell_env = request.form['shell_env']
        user_input = request.form['user_input']
        # Here you would add the logic to send the data to the OpenAI API
        # For example, let's assume we get a response and store it in response_text
        response_text = "Example command response from OpenAI"

        return render_template('cli.html', response_text=response_text, os_type=os_type, shell_env=shell_env)

    # Load help text from YAML file
    with open(os.path.join(os.getcwd(), 'website/static/text.yaml'), 'r') as file:
        help_text = yaml.safe_load(file)

    return render_template('cli.html', help_text=help_text)
