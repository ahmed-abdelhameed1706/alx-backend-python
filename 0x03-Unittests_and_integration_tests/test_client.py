#!/usr/bin/env python3
""" module to test client """
import unittest
from unittest.mock import Mock, patch, PropertyMock
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

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )  # no pep8

        self.assertEqual(response, {"name": org_name})

    def test_public_repos_url(self):
        """method to test puclic repos"""

        mock_payload = {"repos_url": "url"}

        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload

            gh_client = GithubOrgClient("repos_url")
            repos_url = gh_client._public_repos_url

            result = "url"

            self.assertEqual(repos_url, result)


if __name__ == "__main__":
    unittest.main()
