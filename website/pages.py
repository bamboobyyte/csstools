
from flask import Blueprint, render_template, url_for

pages = Blueprint('pages', __name__)

@pages.route('/')
def root(http_code):
    return render_template('base.html')
