from flask import Flask, render_template, jsonify, request

import json
import numpy as np
import pandas as pd
import pickle

# app instanciation
app = Flask(__name__)

# push context while testing
app.app_context().push()


# prediction function
@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        client_id = request.get_data()  # get client_id
        data = pd.read_csv('test_kaggle_reduced.csv', index_col=0)  # read data
        loaded_model = pickle.load(open('model.pkl', 'rb'))  # load model
        result = loaded_model.predict_proba(
            data.loc[int(client_id)].values.reshape(1, -1))  # prediction
        proba_remboursement = np.int64(result[0][0]*100)  # prediction as %
        return str(proba_remboursement)


if __name__ == "__main__":
    app.run(debug=True, port=3000)





    
    