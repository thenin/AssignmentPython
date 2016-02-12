__author__ = 'kguryanov'
import unittest


class Verifiers:
    @staticmethod
    def verify_equals(actual, expected, message="Values are not equal"):
        unittest.TestCase.assertEqual(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_type(actual, expected, message="Types not not match"):
        unittest.TestCase.assertIsInstance(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_not_equals(actual, expected, message="Values are equal"):
        unittest.TestCase.assertNotEqual(unittest.TestCase(), actual, expected, message)

    @staticmethod
    def verify_returns(expected, method, *args, message="Return value differs from expected"):
        unittest.TestCase.assertEqual(unittest.TestCase(), method(*args), expected, message)
