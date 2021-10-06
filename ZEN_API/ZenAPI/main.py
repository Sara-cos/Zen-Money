from flask import Blueprint
from flask import Flask, Response, request
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

from flask_restful import Resource
import json
# from src.utils.transactions import Charts
import pandas as pd

from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = mongo.db.collection_names
    

    return '<h1>Hi</h1>'

