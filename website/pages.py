from flask import Blueprint, render_template, url_for, redirect

pages = Blueprint('pages', __name__)

@pages.route('/')
def root():
    return redirect(url_for('msip.root'))
