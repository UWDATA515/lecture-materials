"""
Example of using mocking within test cases
"""

import unittest
from unittest import mock

from requests import Timeout

from google.doodle import load_google_doodle_title


class DoodleTest(unittest.TestCase):

    # The following line marks the requests.get function for mocking, which
    # means that you can access the mock version of the function as an
    # argument to the test function - `mock_get` below.
    @mock.patch('requests.get')
    def test_doodle_response_with_doodle(self, mock_get):
        """Validates that load_google_doodle_title correctly parses a title"""
        mock_response = mock.Mock(status_code=200)
        mock_response.text = """<!doctype html><html><meta content="Valentine's Day 2024" property="twitter:title"><meta content="Happy Valentine's Day! #GoogleDoodle" property="twitter:description"></html>"""
        mock_get.return_value = mock_response

        title = load_google_doodle_title()
        self.assertEqual(title, "Valentine's Day 2024")

    @mock.patch('requests.get')
    def test_calls_requests_get(self, mock_get):
        """Validates that load_google_doodle_title calls requests.get with the correct url"""
        mock_get.return_value = 'foobar'
        load_google_doodle_title()
        mock_get.assert_called_with('https://google.com')

    @mock.patch('requests.get')
    def test_no_text_in_response(self, mock_get):
        """Validates that if there is no text in the response, returns None"""
        mock_response = mock.Mock(status_code=200)
        mock_response.text = ''
        mock_get.return_value = mock_response

        title = load_google_doodle_title()
        self.assertIsNone(title)

    @mock.patch('requests.get')
    def test_doodle_response_without_doodle(self, mock_get):
        """Validates that if the twitter:title meta content tag is missing, returns None"""
        mock_response = mock.Mock(status_code=200)
        mock_response.text = """<!doctype html><html><meta content="Valentine's Day 2024"><meta content="Happy Valentine's Day! #GoogleDoodle" property="twitter:description"></html>"""
        mock_get.return_value = mock_response

        title = load_google_doodle_title()
        self.assertIsNone(title)

    @mock.patch('requests.get')
    def test_timeout_error(self, mock_get):
        """Validates that the function returns `None` if the request raises a timeout error"""
        mock_get.return_value = mock_get.side_effect = Timeout
        title = load_google_doodle_title()
        self.assertIsNone(title)

if __name__ == '__main__':
    unittest.main()
