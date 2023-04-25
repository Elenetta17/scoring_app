from app import predict
import json
import requests
import unittest

url = "https://elena-openclassrooms-predict.herokuapp.com/predict"

# testing the value of the prediction
class TestPrediction(unittest.TestCase):

    def test_should_predict_69(self):
        client_id = str(100001)
        prediction = requests.post(url, data=client_id)
        self.assertEqual(prediction.text, str(69))

    def test_should_predict_43(self):
        client_id = str(100005)
        prediction = requests.post(url, data=client_id)
        self.assertEqual(prediction.text, str(43))


if __name__ == "__main__":
    unittest.main()
