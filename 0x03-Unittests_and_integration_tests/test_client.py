#!/usr/bin/env python3
"""
Parameterize and patch as decorators
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit Test for the Github Client
    """
    @parameterized.expand([
        ('google', {'google': 'request'}),
        ('abc', {'abc': 'request'}),
    ])
    @patch('requests.get')
    def test_org(self, test_org, test_payload, mock_method):
        """
        class method to test org method of Github Client
        """
        mock_method.return_value.json.return_value = test_payload
        dummy = GithubOrgClient(test_org).org
        self.assertEqual(dummy, test_payload)
