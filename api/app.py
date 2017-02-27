#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'TEST_LOGS_DB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/TEST_LOGS_DB'

mongo = PyMongo(app)

from logs import logs_api

app.register_blueprint(logs_api, url_prefix='/v1/logs')

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
