from flask import Flask, jsonify
from webapp.demo import  *
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return jsonify(export_result())



if __name__ == '__main__':
    app.run()
