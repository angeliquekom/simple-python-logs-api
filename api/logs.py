#!flask/bin/python
from flask import Flask, Blueprint, request
from bson.json_util import dumps

logs_api = Blueprint('logs_api', __name__)

from app import mongo

@logs_api.route('/', methods=['GET'])
def get_logs():
    js = mongo.db.logs.find()

    return dumps(js)

@logs_api.route('/', methods=['POST'])
def create_log():
    if not request.json or not 'title' in request.json or not 'user' in request.json:
        error_response = {'status': 'error'}
        return dumps(error_response)

    log = {
        'title': request.json['title'],
        'user': request.json['user']
    }

    mongo.db.logs.insert(log)

    success_response = {'status': 'success'}

    return dumps(success_response), 201
