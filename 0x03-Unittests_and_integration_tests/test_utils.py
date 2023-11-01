#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Class that performs 3 tests on access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        function that tests access_nested_map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        function that tests access_nested_map for exceptions
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test Class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        function that tests get_json
        """
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_with(test_url)
        self.assertDictEqual(response, test_payload)


class TestClass:
    """
    TestClass copied from exercise
    """
    def a_method(self):
        """
        Arbitrary method that returns 42
        """
        return 42

    @memoize
    def a_property(self):
        """
        Method to execute a_method on instance
        """
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    Class to test memoize function of utils
    """
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method) -> None:
        """
        Method that does the testing
        """
        obj = TestClass()
        mock_method.return_value = 42

        result1 = obj.a_property
        result2 = obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()
