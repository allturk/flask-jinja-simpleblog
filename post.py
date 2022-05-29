import requests


class Post:
    def __init__(self):
        self.api_url="https://api.npoint.io/c790b4d5cab58020d391"
        self.response=requests.get(self.api_url).json()

    def return_response(self):
        return self.response