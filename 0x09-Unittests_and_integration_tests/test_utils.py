#!/usr/bin/env python3
""" Parameterize a unit test
"""
import unittest
from typing import Any, Sequence, Mapping
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ first unit test for utils.access_nested_map
    """
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: Any) -> Any:
        """ TestAccessNestedMap.test_access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence):
        """ Parameterize a unit test
        """
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    """ TestGetJson
    """
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url: str, test_payload: dict,
                      mock_get: Any) -> Any:
        """ method to test
        """
        mock_get.return_value = test_payload
        data = get_json(test_url)
        self.assertEqual(data, test_payload)


class TestMemoize(unittest.TestCase):
    """ Parameterize and patch
    """
    def test_memoize(self):
        """ Method memoize
        """

        class TestClass:
            """ Test class
            """
            def a_method(self):
                """ a method
                """
                return 42

            @memoize
            def a_property(self):
                """ Method with decorator
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            thing = TestClass()
            thing.a_property()

        mock_method.assert_called_once()
