import collections
from flask import Flask
import pymongo
from pymongo import MongoClient
from pymongo import collection
from bson import json_util
from bson.json_util import loads, dumps
import json
import ssl

cluster = MongoClient("mongodb+srv://immiico_infy--1:hE9kqAnxP2Ct3z2X@zenmoney.wiojz.mongodb.net/zenmoney?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

app = Flask(__name__)


db = cluster["zenmoney"]
collection = db["users"]
list_collection = list(collection.find({}))
user_json_list = json.dumps(list_collection,default=json_util.default)

user_json = json.dumps(user_json_list)
# id = collections.find({"_id"})

# collection_json = json(collection)


@app.route("/",methods=["GET"])
def get_cc():
    
    return user_json


# if __name__ == "__main__":
#     app.run(debug=True)