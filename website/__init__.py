from flask import Flask

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello world'

    from .pages import pages
    from .msip import msip
    from .sncalc import sncalc

    app.register_blueprint(pages, url_pregix='/')
    app.register_blueprint(msip, url_pregix='/')
    app.register_blueprint(sncalc, url_pregix='/')

    return app