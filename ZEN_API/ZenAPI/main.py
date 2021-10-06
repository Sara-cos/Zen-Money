from flask import Blueprint
from flask import Flask, Response, request
from flask_restful import Api, Resource
# from Zen_API import app
import configparser
from Zen_API.extensions import mongo
from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo

# import Zen_API.pre

# app = Flask(__name__)
# api = Api(app)
# config = configparser.ConfigParser()


DataB = mongo.db
print(DataB)

# for collect in collection_names:
#     print(collect)


main = Blueprint('main', __name__)

# @main.route('/read_credit_card')
# def read_credit_card():
#     db_Credit_Card = mongo.db.CREDIT_CARD
#     coll = db_Credit_Card.find()
#     print(coll)

#     return jsonify(coll)


# class deposit(Resource):
#     def get(self, currentBalance):
#         return 


# if __name__ == "__main__":
#     app.run(debug=True)
    



# # @main.route('/')
# # def index():
# #     db = mongo.db
    

# #     return db

