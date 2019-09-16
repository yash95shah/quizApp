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

@webapp_blueprint.route('/client/')
def serve_client():
    return send_from_directory('webapp/static/client', 'index.html')

@webapp_blueprint.route('/client/<path:path>')    
def serve_client_files(path):
    return send_from_directory('webapp/static/client', path)

@webapp_blueprint.route('/questions/add', methods=['GET','POST'])
def add_question():
    if request.method == 'GET':
        return render_template('add.html', question={}, action='Add')
    elif request.method == 'POST':
        data = request.form.to_dict(flat=True)
        image_file = request.files.get('image')
        questions.save_question(data, image_file)
        return redirect('/', code=302)
    else:        
        return "Method not supported for /questions/add"