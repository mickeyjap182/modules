import os, sys, unittest
import json
from requests import api

module_path  = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

class TestRequest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    @staticmethod
    def char_len(chars):
        return len(chars)

    def test_pole_temp_humi(self):
        # set your api token on your environment variable from issued at official site.
        token = os.getenv('NATURE_REMO_TOKEN')
        apiClient = WebClient(token)
        result = False
        # # if you wanna run, disable comment out following code. 
        # result = apiClient.send('/1/devices', Method=WebClient.get)
        # if result is False:
        #     print(apiClient.getMessage())
        #     self.assertFalse(True)
        # response = apiClient.getResult()
        # print(json.dumps(response, indent=4))
        """
        '/1/devices'
        response[0]
        temperature = response[0]["newest_events"]["te"]["val"]
        humidity = response[0]["newest_events"]["hu"]["val"]
        """
        self.assertTrue(True)

    def test_get_and_change_aircon_status(self):
        # set your api token on your environment variable from issued at official site.
        token = os.getenv('NATURE_REMO_TOKEN')
        apiClient = WebClient(token)
        result = False
        # # if you wanna run, disable comment out following code. 
        # result = apiClient.send('/1/appliances', Method=WebClient.get)
        # if result is False:
        #     print(apiClient.getMessage())
        #     self.assertFalse(True)
        # response = apiClient.getResult()
        # print(json.dumps(response, indent=4))
        """
        '/1/appliances'
        response[n]
        registered_appliance_id = response[n]["id"]
        registered_appliance_nickname = response[n]["nickname"]
        signals = response[n]["signals"]
        signals[n]["id"]
        signals[n]["name"]
        """
        self.assertTrue(True)

if __name__ == '__main__':
    print(module_path) 
    if module_path not in sys.path:
        sys.path.append(module_path)
    from link.nature.remo import WebClient
    unittest.main()
