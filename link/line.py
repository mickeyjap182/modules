import os
import requests

class Subscriber():
    """
    send notification for line SNS. 
    """
    line_notify_api = 'https://notify-api.line.me/api/notify'
    def __init__(self, token):
        """
        setup line's authentication header payload.
        """
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def send(self, message, *args):
        """
        line notification sender (message and image)
        """
        # payload of line notification.
        payload = {
            'data': {'message': message},
            'headers': self.headers,
        }
        # with a image file.
        if len(args) > 0:
            payload['files'] = {"imageFile": open(args[0], "rb")}
        requests.post(Subscriber.line_notify_api, **payload)
