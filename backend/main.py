from flask import Flask
from flask import jsonify
from flask_cors import CORS
import postgres

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/python-req/<text>/<top_k>', methods=['GET'])
def python_request(text, top_k):
    #response = jsonify(postgres.get_postgres_topk(text, int(top_k)))
    response = jsonify({'message': 'success'})
    return response

@app.route('/postgres-req/<text>/<top_k>', methods=['GET'])
def postgres_request(text, top_k):
    response = jsonify(postgres.get_postgres_topk(text, int(top_k)))
    return response

if __name__ == '__main__':
    app.run(debug=True)
