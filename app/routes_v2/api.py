from flask import jsonify, request
from app import app
from app.data.data_loader import get_data
from app.data.connect import Connect
from bson.json_util import dumps
from bson.objectid import ObjectId

# This tutorial is intended as an introduction to working with MongoDB and PyMongo.
# https://api.mongodb.com/python/current/tutorial.html

def success():
    return {
        "status": "success",
        "message": "Or optional success message"
    }

def error():
    return {
        "status": "error",
        "message": "No documents left"
    }

mongo = Connect.get_connection()
db = mongo.db.swift_blog

@app.route('/v2/api', methods=['POST'])
def api():
    feed = get_data()

    entryes = []
    for key, value in feed.items():
        for key, value in value.items():
            if key == "entry":
                entryes = value

    db.insert_many(entryes)
    return jsonify(success())


@app.route('/v2/entries', methods=['GET'])
def entries():
    page = db.find()
    return dumps(page)

# https://www.codementor.io/@arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr
@app.route('/v2/pages', methods=['POST'])
def pages():
    # { "page_size": 3, "last_id": null }
    # { "page_size":	5, "last_id": "5f53ceb1828dcbc882dac088" }
    page_size = request.json['page_size']
    last_id = request.json['last_id']

    if last_id is None:
        cursor = db.find().limit(page_size)
    else:
        # '$gt' - https://docs.mongodb.com/manual/reference/operator/query-comparison/
        cursor = db.find({'_id': {'$gt': ObjectId(last_id)}}).limit(page_size)

    # Get the data
    data = [x for x in cursor]

    if not data:
        return jsonify(error())

    # Since documents are naturally ordered with _id, last document will
    # have max id.
    last_id = data[-1]['_id']

    data.append({'last_id': last_id})

    return dumps(data)
