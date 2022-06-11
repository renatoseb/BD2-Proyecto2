from flask import Flask
from flask import jsonify
from flask_cors import CORS
import postgres
import mongodb_search
import time

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/python-req/<text>/<top_k>', methods=['GET'])
def python_request(text, top_k):
    
    start = time.time()
    # response = search()
    end = time.time()
    time = round(end - start, 6)
    return response

@app.route('/postgres-req/<text>/<top_k>', methods=['GET'])
def postgres_request(text, top_k):
    response = jsonify(postgres.get_postgres_topk(text, int(top_k)))
    return response

@app.route('/mongodb-req/<text>/<top_k>', methods=["GET"])
def mongodb_request(text, top_k):
    response = jsonify(mongodb_search.get_mongodb_topk(text, int(top_k)))
    return response

if __name__ == '__main__':
    app.run(debug=True)
