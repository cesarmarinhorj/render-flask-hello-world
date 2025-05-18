from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def get_time():
    ct = time.localtime()
    sct = time.strftime('%Y-%m-%d %H:%M:%S', ct)
    obj = {'current_time': sct}
    return jsonify(obj)

