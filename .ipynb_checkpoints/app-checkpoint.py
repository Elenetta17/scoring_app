from flask import Flask, render_template, jsonify, request
import json
import numpy as np
#import requests
import pandas as pd
import pickle

app = Flask(__name__)
app.app_context().push()


@app.route("/predict", methods= ["POST", "GET"])
def predict():
    if request.method == 'POST':
        client_id = request.get_data()
        data = pd.read_csv('../X_test_reduced.csv', index_col=0)
        loaded_model = pickle.load(open('model.pkl', 'rb'))
        result =  loaded_model.predict_proba(data.loc[int(client_id)].values.reshape(1,-1))
        proba_remboursement = np.int(result[0][0]*100)
        return str(proba_remboursement)

if __name__ == "__main__":
    app.run(debug=True, port=3000)





    
    