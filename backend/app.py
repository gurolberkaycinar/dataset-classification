import json
from flask import Flask, jsonify, request
from sklearn.feature_extraction import DictVectorizer
import numpy as np

from classification.naive_bayes.naive_bayes import *
from classification.knn.knn import *
from util.util import convert
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/classification/naive_bayes/<file_name>', methods=['POST'])
def naive_bayes_trainer(file_name):  # put application's code here
    request_body = request.get_json()

    dataset = pd.read_csv("datasets/" + file_name + ".csv", usecols=lambda x: x != 'url')
    dataset = dataset.dropna()

    print(request_body)

    label_column = request_body['label_column']
    test_percentage = request_body['test_percentage']
    accuracy, precision, recall = naive_bayes_train(dataset, label_column, test_percentage)

    values = convert(
        ['tableHeaders', dataset.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall])
    return jsonify(values)


@app.route('/prediction/naive_bayes', methods=['POST'])
def naive_bayes_predicter():
    req = request.get_json()
    prediction: np.ndarray = naive_bayes_predict(req['features'], req['label'])
    return jsonify(prediction[-1].item())


@app.route('/classification/knn/<file_name>', methods=['POST'])
def knn_trainer(file_name):
    req = request.get_json()
    label_column = req['label_column']
    test_percentage = req['test_percentage']
    neighbour_count = req['neighbour_count']
    distance_metric = req['distance_order']
    dataset = pd.read_csv("datasets/" + file_name + ".csv", usecols=lambda x: x != 'url')
    dataset = dataset.dropna()
    accuracy, precision, recall = knn_train(dataset, label_column, test_percentage, neighbour_count, distance_metric)

    values = convert(
        ['tableHeaders', dataset.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall])
    return jsonify(values)

@app.route('/classification/knn', methods=['POST'])
def knn_predicter():
    req = request.get_json()
    prediction: np.ndarray = knn_predict(req['features'], req['label'])
    return jsonify(prediction[-1].item())

@app.route('/datasets/<dataset>', methods=['GET'])
def get_dataset_sample(dataset):
    file = pd.read_csv("./datasets/" + dataset + ".csv", nrows=5)
    values = convert(['tableHeaders', file.columns.tolist(), 'tableValues', file.values.tolist()])
    return jsonify(values)


if __name__ == '__main__':
    app.run()
