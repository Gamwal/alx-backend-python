#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Class that performs 3 tests on access_nested_map
    """
    @parameterized.expand([
        ("Test 1", {"a": 1}, ("a",), 1),
        ("Test 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Test 3", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        function that tests access_nested_map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
