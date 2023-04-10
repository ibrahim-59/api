import json
from flask import Flask,request,render_template,url_for,jsonify,session
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib as joblib
import os

model= joblib.load("model_pickle")


app = Flask(__name__)
aa='1'
print(type(int(aa)))


@app.route('/')
def index():
    return render_template('jhj.html')

@app.route('/')
@app.route("/api",methods=['POST','GET'])
def api():
    d1 = request.json['d1']
    d2 = request.json['d2']
    d3 = request.json['d3']
    d4 = request.json['d4']
    d5 = request.json['d5']

    disease = []
    disease.append(int(d1))
    disease.append(int(d2))
    disease.append(int(d3))
    disease.append(int(d4))
    disease.append(int(d5))


    f = disease[0]
    b = disease[1]
    c = disease[2]
    d = disease[3]
    e = disease[4]
    print(disease[4])

 # This is the output that was stored in the JSON within the browser

     #this converts the json output to a python dictionary


    a = []
    i = 0
    while i < 134:
        a.append(0)
        i += 1

        if i == 134:
            break

    a[f] = 1
    a[b] = 1
    a[c] = 1
    a[d] = 1
    a[e] = 1
    input_data_as_numpy_array = np.asarray(a)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)

    d = dict(enumerate(prediction.flatten(), 1))
    print(d)

    #this shows the json converted as a python dictionary
    return jsonify({"result": prediction[0]})


@app.route("/test", methods=['POST','GET'])
def test():

    output = request.get_json()
 # This is the output that was stored in the JSON within the browser

    result = json.loads(output) #this converts the json output to a python dictionary


    a = []
    i = 0
    while i < 134:
        a.append(0)
        i += 1

        if i == 134:
            break
    f= result[0]
    b = result[1]
    c= result[2]
    d = result[3]
    e = result[4]
    a[f] = 1
    a[b] = 1
    a[c] = 1
    a[d] = 1
    a[e] = 1
    input_data_as_numpy_array = np.asarray(a)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)

    d = dict(enumerate(prediction.flatten(), 1))
    print(d)




    #this shows the json converted as a python dictionary
    return (d)

if __name__ == "__main__":
    app.run(debug=True)