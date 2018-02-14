#!flask/bin/python
import base64
from io import BytesIO

import clamd
import sys

import time
from flask import Flask, jsonify, request

app = Flask(__name__)

last_result = ""


@app.route('/')
def index():
    return "v4"


@app.route('/v1/scan', methods=['GET'])
def get_last_scan_result():
    scan = {
        'status': last_result
    }
    return jsonify(scan)


@app.route('/v1/scan', methods=['POST'])
def scan():
    sys.stderr.write("scan()")
    start = time.time()

    if not request.json:
        jsonify({'status': 'failed'}), 401

    file = request.json["file"]

    if not file:
        jsonify({'status': 'failed'}), 401

    file_data = base64.b64decode(file)

    cd = clamd.ClamdUnixSocket()

    last_result = cd.instream(BytesIO(file_data))

    scan = {
        'status': last_result
    }

    elapsed_time = time.time() - start
    sys.stderr.write(str(elapsed_time))

    return jsonify(scan)


if __name__ == '__main__':
    app.run(debug=True, port=80)
