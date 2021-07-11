import requests
import json
class WebClient():
    """
    it is Web(HTTP) API Client for Nature Remo. 
    @see https://swagger.nature.global/
    """
    def __init__(self, token):
        """
        setup authentication header payload.
        """
        if token is None:
            raise ValueError("The Token is no value.")
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}
        # TODO: make it enable to set addtional header.

    def getMessage(self):
        """ A API error message.   """
        return self.message

    def getResult(self):
        """ A API response value.   """
        return self.result

    def setResult(self, result, message):
        """ A API response value.   """
        self.result = result
        self.message = message

    def send(self, resource_path, *args, **kwargs) -> bool:
        """
        request and respond. for target resource_path
        """
        if (WebClient.METHOD in kwargs is False) or (not kwargs[WebClient.METHOD] in WebClient.VALID_METHODS):
            self.setResult(None, "please take kwargs parameter as valid http method e.g.'Client.METHOD={}') ".format(" or ".join(list(s.__name__ for s in Client.VALID_METHODS))))  
            return False  
        self.result =  eval("self.{}(resource_path, *args, **kwargs)".format(kwargs[WebClient.METHOD].__name__))
        self.message = None
        return True

    def get(self, resource_path, *args, **kwargs):
        """ connect via HTTP GET Method   """
        response = requests.get(WebClient.API_SERVER_URL + resource_path, headers=self.headers)
        response = json.loads(response.text)
        return response

    def post(self, *args, **kwargs):
        """ connect via HTTP POST Method   """
        pass

    METHOD = 'Method'
    VALID_METHODS = (get, post)
    API_SERVER_URL = 'https://api.nature.global'

class LocalClient():
    """
    Remo using Bonjour, and then send a HTTP request to the IP.. 
    @see https://local-swagger.nature.global/
    """
    pass
