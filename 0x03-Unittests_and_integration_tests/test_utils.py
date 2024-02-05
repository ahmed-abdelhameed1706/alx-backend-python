#!/usr/bin/env python3
""" module to test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
import requests
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """class to test test access nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )  # no pep8
    def test_access_nested_map(self, input, path, expected):
        """method to test access nested map"""
        self.assertEqual(access_nested_map(input, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, input, path):
        """method to test exceptions raised"""
        with self.assertRaises(KeyError):
            access_nested_map(input, path)


class TestGetJson(unittest.TestCase):
    """class to test getjson"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test get_json"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


if __name__ == "__main__":
    unittest.main()
