
import unittest
from modules.Http.Http import Http


class TestHttp(unittest.TestCase):
    def test_send_data(self):
        self.assertRaises(Exception('Request failed'), Http.send_data('', {}))
