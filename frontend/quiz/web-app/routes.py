from flask import Blueprint, render_template
from flask import send_from_directory
from flask import request, redirect

import questions


webapp_blueprint = Blueprint(
    'webapp', 
    __name__, 
    template_folder='templates',
)

@webapp_blueprint.route('/')
def serve_home():
    return render_template('home.html')
def server_client():
    return send_from_directory('webapp/static/client', 'index.html')
def serve_client_files(path):
    return send_from_directory('webapp/static/client', path)
