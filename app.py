#!/usr/bin/env python
# -*- coding: utf-8 -*-

# flask stuff
from flask import Flask, request, jsonify
from flask_cors import CORS

# ml stuff
from ml.ml_model import predict_iris, predict_iris_file

# CORS for connecting with the front
allowed_domains = [
    r'http://localhost:5000',
]

application = Flask(__name__)
CORS(application,
     origins=allowed_domains,
     resources=r'/v1/*',
     supports_credentials=True)
# only allows access to listed domains (CORS will only be applied to allowed_domains
# only allows access to v1 (CORS will only be applied to domains that start with /v1/*
# IMPORTANT: supports_credentials is allows COOKIES and CREDENTIALS to be submitted across domains


# more CORS settings here: https://flask-cors.corydolphin.com/en/latest/api.html#extension
# github example: https://github.com/corydolphin/flask-cors/blob/master/examples/app_based_example.py


# only POST
@application.route('/v1/', methods=['POST'])
def hello():
    a = request.form['a']

    results = predict_iris(input=a)
    return "hello {}".format(a)


# GET request
@application.route('/v1/predict/', methods=['GET'])
def nn_prediction():
    x_1 = request.args.get("s_length")
    x_2 = request.args.get("s_width")
    x_3 = request.args.get("p_length")
    x_4 = request.args.get("p_width")

    x_input = [x_1, x_2, x_3, x_4]

    results = predict_iris(x_input=x_input)

    output = {
        "results": results,
        "status": 200
    }
    return jsonify(output)


# POST request (file input)
@application.route('/v1/predict/', methods=['POST'])
def nn_prediction_file():
    x_1 = request.files.get("input_file")

    results = predict_iris_file(x_file_input=x_1)
    print('returning: ', results)

    output = {
        "results": results,
        "status": 200
    }
    return jsonify(output)


application.run(debug=True)
print('a flask app is initiated at {0}'.format(application.instance_path))
