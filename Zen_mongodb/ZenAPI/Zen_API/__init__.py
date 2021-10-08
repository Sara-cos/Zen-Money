from flask import Flask 
from .extensions import mongo
# from ZenAPI.main import main
from flask_restful import Api, Resource
from .settings import MONGO_URI
# from .routes import initialize_routes

def create_app(config_object='Zen_API.settings'):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config_object)

    mongo.init_app(app)

    # app.register_blueprint(main)

    return app



# initialize_routes(api)


# def create_app(config_object='ZenAPI.settings'):

# app.config.from_object(settings)


# app.register_blueprint(main)