#!/usr/bin/env python3
""" module to test client """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class to test githuborg"""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """method to test org"""

        mock_get_json.return_value = {"name": org_name}
        org_client = GithubOrgClient(org_name)
        response = org_client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(response, {"name": org_name})


if __name__ == "__main__":
    unittest.main()
