from flask import jsonify
from app import app
from app.data.data_loader import get_data

@app.route('/all')
def all():
    return jsonify(get_data())
