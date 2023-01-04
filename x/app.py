from flask import Flask, jsonify, request
from webapp.demo import *
from classification.naive_bayes.naive_bayes import naive_bayes
from util.util import convert
import pandas as pd

app = Flask(__name__)


@app.route('/classification/naive_bayes', methods=['POST'])
def hello_world():  # put application's code here
    data = request.get_json()
    print(request.headers)
    print(data)

    file_name = data['fileName']
    print(file_name)

    file = pd.read_csv("datasets/FM 2023.csv")
    file = file.dropna()

    accuracy, precision, recall, f1 = naive_bayes(file)
    values = convert(['accuracy', accuracy, 'precision', precision,'recall',  recall, 'f1', f1])

    return jsonify(values)


if __name__ == '__main__':
    app.run()
