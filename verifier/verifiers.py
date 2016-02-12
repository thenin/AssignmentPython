__author__ = 'kguryanov'
import unittest


class Verifiers:
    @staticmethod
    def verify_equals(actual, expected, message=None):
        unittest.TestCase.assertEqual(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_type(actual, expected, message=None):
        unittest.TestCase.assertIsInstance(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_not_equals(actual, expected, message=None):
        unittest.TestCase.assertNotEqual(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_returns(expected, method, *args, message=None):
        unittest.TestCase.assertEqual(unittest.TestCase(), method(*args), expected, message)
