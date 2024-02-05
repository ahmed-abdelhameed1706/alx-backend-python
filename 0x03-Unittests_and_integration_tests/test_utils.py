#!/usr/bin/env python3
""" module to test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
