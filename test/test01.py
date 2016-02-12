__author__ = 'kguryanov'

import unittest
from verifier.verifiers import verify_equals, verify_not_equals, verify_type


class TestCase01(unittest.TestCase):
    def test_simple_positive_comparison(self):
        verify_equals(1, 1, 'Comparison failed')

    def test_simple_negative_comparison(self):
        verify_not_equals(1, 0, 'Comparison failed')

    def test_verify_type(self):
        verify_type("Simple string", str, "Incorrect type")


if __name__ == '__main__':
    unittest.main()
