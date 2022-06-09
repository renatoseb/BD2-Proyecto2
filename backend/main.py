from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/python-req/<text>/<top_k>', methods=['GET'])
def python_request(text, top_k):
    print(text)
    print(top_k)
    response = jsonify({'message': 'success'})
    return response

@app.route('/postgres-req/<text>/<top_k>', methods=['GET'])
def postgres_request(text, top_k):
    print(text)
    print(top_k)
    response = jsonify({'message': 'success'})
    return response

if __name__ == '__main__':
    app.run(debug=True)
