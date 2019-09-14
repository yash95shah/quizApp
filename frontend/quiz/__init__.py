from flask import Flask
app = Flask(__name__, static_folder='static')


#Registering the blueprints

from quiz.api.routes import api_blueprint
from quiz.web-app.routes import web-app_blueprint 
api.register_blueprint(api.routes.api_blueprint, url_prefix='/api')
api.register_blueprint(web-app.routes.web-app_blueprint, url_prefix=)