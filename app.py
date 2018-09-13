from flask import Flask, g, jsonify, render_template

import models
from resources.virtual_company import virtualco_api

import config

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(virtualco_api, url_prefix='/api/v1')


@app.route('/')
def my_companies():
    return render_template('index.html')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
