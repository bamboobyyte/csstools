from flask import Blueprint, request, render_template, url_for
import yaml
import os

cli = Blueprint('cli', __name__)

@cli.route('/cli', methods=['GET', 'POST'])
def root():
    # Load help text from YAML file
    with open(os.path.join(os.getcwd(), 'website/static/text.yaml'), 'r') as file:
        yaml_file = yaml.safe_load(file)
    help_text = yaml_file['cli_help_text']

    if request.method == 'POST':
        os_type = request.form['os_type']
        # shell_env = request.form['shell_env']
        # user_input = request.form['user_input']
        # Here you would add the logic to send the data to the OpenAI API
        # For example, let's assume we get a response and store it in response_text
        response_text = "Example command response from OpenAI"
        # print(type(os_type))
        return render_template('cli.html', help_text=help_text, response_text=response_text, os_type=os_type, shell_env=shell_env)

    return render_template('cli.html', help_text=help_text)
