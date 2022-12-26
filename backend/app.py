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
    data = request.get_json()

    file = pd.read_csv("datasets/" + file_name + ".csv")
    file = file.dropna()

    label_column = data['label_column']
    test_percentage = data['test_percentage']
    accuracy, precision, recall, f1 = naive_bayes(file, label_column, test_percentage)

    values = convert(
        ['tableHeaders', file.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
         recall, 'f1',
         f1])
    return jsonify(values)

@app.route('/classification/knn/<file_name>', methods=['POST'])
def knn_controller(file_name):
    req = request.get_json()
    label_column = req['label_column']
    test_percentage = req['test_percentage']

    data = pd.read_csv("datasets/" + file_name + ".csv")
    data = data.dropna()

    accuracy, precision, recall, f1 = knn(data, label_column, test_percentage, 3, 2)

    values = convert(
        ['tableHeaders', file.columns.tolist(), 'accuracy', accuracy, 'precision', precision, 'recall',
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
