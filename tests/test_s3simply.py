import unittest

from s3simply import Client


class TestClient(unittest.TestCase):
    def test__init__(self):
        c = Client()
        self.assertEqual(c.endpoint, 'https://s3.amazonaws.com')
        self.assertIsNone(c.access_key_id)
        self.assertIsNone(c.secret_access_key)

        c = Client('a', 'b', 'c')
        self.assertNotEqual(c.endpoint, 'https://s3.amazonaws.com')
        self.assertEqual(c.endpoint, 'c')
        self.assertEqual(c.access_key_id, 'a')
        self.assertEqual(c.secret_access_key, 'b')


if __name__ == '__main__':
    unittest.main()
