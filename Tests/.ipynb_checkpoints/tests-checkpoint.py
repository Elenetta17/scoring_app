from app import predict
import json
import requests
import unittest

url = "http://127.0.0.1:3000/predict"

# testing the value of the prediction
class TestPrediction(unittest.TestCase):

    def test_should_predict_79(self):
        client_id = str(100001)
        prediction = requests.post(url, data=client_id)
        self.assertEqual(prediction.text, str(79))

    def test_should_predict_50(self):
        client_id = str(100005)
        prediction = requests.post(url, data=client_id)
        self.assertEqual(prediction.text, str(50))


if __name__ == "__main__":
    unittest.main()
