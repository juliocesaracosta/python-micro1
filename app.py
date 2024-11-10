# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/service', methods=['GET'])
def service():
    return jsonify({"message": "Hello from Service Number 1!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)