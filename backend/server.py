from flask import Flask, jsonify,request, after_this_request
from ml_pipeline import predict


app = Flask(__name__)

@app.route('/')
def test():
    return jsonify({'it':'works'})

@app.route('/predict',methods = ['POST'])
def pred():
    #get input text  from user
    data = request.get_json()
    text = data['text']
    
    prediction = predict(text)

    #make it a string so we can jsonify it!
    prediction = str(prediction, encoding='utf-8')
    
    return jsonify({'output':prediction})

if __name__ == '__main__':
    app.run(debug=True, port=3500,host='0.0.0.0')