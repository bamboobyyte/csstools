from flask import Flask
import os

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello world'

    # # Load environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    asst_cli_id = os.getenv('ASST_CLI_ID')

    from .pages import pages
    from .msip import msip
    from .sncalc import sncalc
    from .cli import cli

    # Registering blueprints
    app.register_blueprint(pages, url_pregix='/')
    app.register_blueprint(msip, url_pregix='/')
    app.register_blueprint(sncalc, url_pregix='/')
    app.register_blueprint(cli, url_pregix='/')

    return app