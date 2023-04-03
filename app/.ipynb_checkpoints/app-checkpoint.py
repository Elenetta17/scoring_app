from flask import Flask, render_template, jsonify, request
import json
#import requests
import pandas as pd

app = Flask(__name__)
app.app_context().push()

@app.route("/get_clients_id")
def get_clients_id_list():
    data = pd.read_csv('../../train_ab.csv', index_col=0)
    return jsonify({'data': list(data.index)[:200]})

@app.route("/predict", methods= ["POST", "GET"])
def predict():
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        return 'hello'

if __name__ == "__main__":
    app.run(debug=True, port=3000)





    
    