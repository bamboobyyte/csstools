from flask import Flask
from dotenv import load_dotenv
from os import getenv, path, getcwd
from yaml import safe_load
from openai import OpenAI

def init_app():
    # Load environment variables
    load_dotenv()
    global asst_cli_id
    asst_cli_id = getenv('ASST_CLI_ID')
    global asst_email_polisher_id
    asst_email_polisher_id = getenv('ASST_EMAIL_POLISHER_ID')
    global asst_email_fqr_id
    asst_email_fqr_id = getenv('ASST_EMAIL_FQR_ID')
    global asst_email_meeting_id
    asst_email_meeting_id = getenv('ASST_EMAIL_MEETING_ID')
    global asst_email_soft_id
    asst_email_soft_id = getenv('ASST_EMAIL_SOFT_ID')

    # Crerate OpenAI client
    openai_api_key = getenv('OPENAI_API_KEY')
    global client
    client = OpenAI(api_key=openai_api_key)

    global help_text
    with open(path.join(getcwd(), 'website/static/text.yaml'), 'r') as file:
        help_text = safe_load(file)

    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    from .pages import pages
    from .msip import msip
    from .sncalc import sncalc
    from .cli import cli
    from .email import email

    # Registering blueprints
    app.register_blueprint(pages, url_pregix='/')
    app.register_blueprint(msip, url_pregix='/')
    app.register_blueprint(sncalc, url_pregix='/')
    app.register_blueprint(cli, url_pregix='/')
    app.register_blueprint(email, url_pregix='/')

    return app