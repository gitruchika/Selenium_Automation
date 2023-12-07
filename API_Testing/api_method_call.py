import requests


class APICall:
    def __init__(self, api_path, server='reqres.in', protocol='http'):
        self.server = server
        self.uri = api_path
        self.protocol = protocol
        self.api_uri = f"{self.protocol}://{self.server}{self.uri}"

    def get_api_call(self):
        response = requests.get(self.api_uri)
        return response

    def post_api_call(self, request_data):
        response = requests.post(self.api_uri, data=request_data)
        return response

    def put_api_call(self, request_data):
        response = requests.put(self.api_uri, data=request_data)
        return response

    def patch_api_call(self, request_data):
        response = requests.patch(self.api_uri, data=request_data)
        return response

    def delete_api_call(self, request_data=None):
        if request_data is not None:
            response = requests.delete(self.api_uri, data=request_data)
        else:
            response = requests.delete(self.api_uri)
        return response
