from flask import Flask 
from .extensions import mongo
from .main import main

# from flask_restful import Api

def create_app(config_object='ZenAPI.settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongo.init_app(app)
    # api = Api(app)

    app.register_blueprint(main)

    return app