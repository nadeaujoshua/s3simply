import urllib.parse
import urllib.request


class Client:
    """A client object for basic S3 operations."""

    def __init__(self, access_key_id=None, secret_access_key=None, endpoint=None):
        if not endpoint:
            endpoint = 'https://s3.amazonaws.com'
        self.endpoint = endpoint
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
