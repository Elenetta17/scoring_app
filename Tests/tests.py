import unittest
from app import predict
import json
import requests
url = 'http://127.0.0.1:3000/predict'
        
class TestPrediction(unittest.TestCase):
    def test_should_predict_60(self):
        client_id = str(100001)
        prediction = requests.post(url, data = client_id)
        self.assertEqual(prediction.text, str(60))
    def test_should_predict_31(self):
        client_id = str(100005)
        prediction = requests.post(url, data = client_id)
        self.assertEqual(prediction.text, str(31))
        
        
if __name__ == "__main__":
    unittest.main()
