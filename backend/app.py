from flask import Flask, jsonify, request
from classification.naive_bayes.naive_bayes import naive_bayes
from classification.knn.knn import knn
from util.util import convert
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/classification/naive_bayes/<file_name>', methods=['POST'])
def naive_bayes_controller(file_name):  # put application's code here
    request_body = request.get_json()

    dataset = pd.read_csv("datasets/" + file_name + ".csv")
    dataset = dataset.dropna()

    label_column = request_body['label_column']
    test_percentage = request_body['test_percentage']
    accuracy, precision, recall, f1 = naive_bayes(dataset, label_column, test_percentage)

    values = convert(
        ['tableHeaders', dataset.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall, 'f1',
         f1])
    return jsonify(values)

@app.route('/classification/knn/<file_name>', methods=['POST'])
def knn_controller(file_name):
    req = request.get_json()
    label_column = req['label_column']
    test_percentage = req['test_percentage']
    neighbour_count = 3
    # neighbour_count = req['test_percentage']
    distance_metric = 2
    # distance_metric = req['test_percentage']

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
    app.run()
