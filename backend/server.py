from flask import Flask, jsonify,request, after_this_request
from ml_pipeline import *


app = Flask(__name__)

@app.route('/')
def test():

    #do this to deal with cors error
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    return jsonify({'it':'works'})


if __name__ == '__main__':
    app.run(debug=True, port=3500,host='0.0.0.0')