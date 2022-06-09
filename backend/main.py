from crypt import methods
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/python-req/<text>/<top_k>', methods=['GET'])
def python_request(text, top_k):
    print(text)
    print(top_k)
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/postgres-req/<text>/<top_k>', methods=['GET'])
def postgres_request(text, top_k):
    print(text)
    print(top_k)
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
