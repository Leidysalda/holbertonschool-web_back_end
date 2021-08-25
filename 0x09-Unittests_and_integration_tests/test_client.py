#!/usr/bin/env python3
""" Parameterize and patch as decorators
"""
import unittest
from typing import Any, Sequence, Mapping
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class to implement test_org method
    """
    @parameterized.expand([("google", {"payload": True}),
                           ("abc", {"payload": True})])
    @patch('client.get_json')
    def test_org(self, test_url: str, test_payload: dict,
                 mock_get: Any) -> Any:
        """ This method should test that GithubOrgClient.org
        """
        mock_get.return_value = test_payload
        test = GithubOrgClient(test_url)
        info = test.org

        self.assertEqual(test_payload, info)

    def test_public_repos_url(self):
        """ Method
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={'repos_url': "google"}) as mock_req:
            thing = GithubOrgClient('google')
            repos = thing._public_repos_url

        self.assertEqual(repos, mock_req.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Any) -> Any:
        """ Method repos
        """
        mock_get.return_value = [{"name": "google"}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="google") as mock_req:
            thing = GithubOrgClient('google')
            repos = thing.public_repos()
            self.assertEqual(repos, ['google'])
            mock_req.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}},
                            "my_license", True),
                           ({"license": {"key": "other_license"}},
                            "my_license", False)])
    def test_has_license(self, key: dict, licence_key: str,
                         result: bool) -> Any:
        """ Test Hash license
        """
        test = GithubOrgClient('google')
        test_license = test.has_license(key, license_key)
        self.assertEqual(test_license, result)
