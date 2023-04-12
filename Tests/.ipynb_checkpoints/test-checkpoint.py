import unittest
from app import predict
import json

class TestApp(unittest.TestCase):
    def test_should_return_client_list(self):
        client_list = get_clients_id_list().json
        expected_length = 200
        self.assertEqual(len(client_list['data']), 200)
        
class TestPrediction(unittest.TestCase):
    def test_should_predict_1(self):
        client_id = str(12345)
        prediction = requests.post(url, data = client_id)
        self.assertEqual(len(client_list['data']), 200)
        
        
if __name__ == "__main__":
    unittest.main()
