import time
import requests

from config import BASE_URL, REQUEST_TIMEOUT


class DeltaClient:

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

        self.session = requests.Session()

    def get(self, endpoint, params=None):

        url = BASE_URL + endpoint

        response = self.session.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint, payload=None):

        url = BASE_URL + endpoint

        response = self.session.post(
            url,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()