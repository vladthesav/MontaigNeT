from flask import Flask, jsonify,request, after_this_request
from ml_pipeline import predict


app = Flask(__name__)

@app.route('/')
def test():

    #do this to deal with cors error
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    return jsonify({'it':'works'})

@app.route('/predict',methods = ['POST'])
def pred():
     #do this to deal with cors error
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    print('REQUEST   ',request)
    #get input text  from user
    data = request.get_json()
    text = data['text']
    
    prediction = predict(text)

    return jsonify({'output':prediction})

print("RUNNING APP")
if __name__ == '__main__':
    app.run(debug=True, port=3500,host='0.0.0.0')