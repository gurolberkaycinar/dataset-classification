import json
from flask import Flask, jsonify, request

import numpy as np

from classification.naive_bayes.naive_bayes import *
from classification.knn.knn import knn
from util.util import convert
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/classification/naive_bayes/<file_name>', methods=['POST'])
def naive_bayes_trainer(file_name):  # put application's code here
    request_body = request.get_json()

    dataset = pd.read_csv("datasets/" + file_name + ".csv")
    dataset = dataset.dropna()

    label_column = request_body['label_column']
    test_percentage = request_body['test_percentage']
    accuracy, precision, recall, f1 = naive_bayes_train(dataset, label_column, test_percentage)

    values = convert(
        ['tableHeaders', dataset.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall, 'f1',
         f1])
    return jsonify(values)


@app.route('/anan', methods=['POST'])
def naive_bayes_predicter():
    # req = request.get_json()
    # print(json.load(request, strict=False))
    # print(req['features'])
    # return jsonify("xd")
    print("sdf")

    something = {
        'fixed acidity': float(7.5),
        'volatile acidity': float(0.7),
        'citric acid': float(0),
        'residual sugar': float(1.9),
        'chlorides': float(0.076),
        'free sulfur dioxide': float(11),
        'total sulfur dioxide': float(34),
        'density': float(0.99),
        'pH': float(3.51),
        'sulphates': float(0.56),
        'alcohol': float(9.4)
    }
    print(type(something))
    # return jsonify("ANAN")
    dataset = pd.read_csv("datasets/" + "Wine" + ".csv")
    dataset = dataset.dropna()

    label_column = 'quality'
    test_percentage = 80

    naive_bayes_train(dataset, label_column, test_percentage)
    print(type (something))
    ordered = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']
    m = np.array([something[i] for i in ordered])
    print(naive_bayes_predict(m.reshape(1, -1)))
    return jsonify("l")


@app.route('/classification/knn/<file_name>', methods=['POST'])
def knn_controller(file_name):
    req = request.get_json()
    label_column = req['label_column']
    test_percentage = req['test_percentage']
    neighbour_count = req['test_percentage']
    distance_metric = req['test_percentage']

    dataset = pd.read_csv("datasets/" + file_name + ".csv")
    dataset = dataset.dropna()

    accuracy, precision, recall, f1 = knn(dataset, label_column, test_percentage, neighbour_count, distance_metric)

    values = convert(
        ['tableHeaders', dataset.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall, 'f1',
         f1])
    return jsonify(values)


@app.route('/datasets/<dataset>', methods=['GET'])
def get_dataset_sample(dataset):
    file = pd.read_csv("./datasets/" + dataset + ".csv", nrows=5)
    values = convert(['tableHeaders', file.columns.tolist(), 'tableValues', file.values.tolist()])
    return jsonify(values)


if __name__ == '__main__':
    app.run(debug=True)
