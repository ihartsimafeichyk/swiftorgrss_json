from flask import jsonify
from app import app
from app.data import get_data

@app.route('/all')
def all():

    return get_data()


