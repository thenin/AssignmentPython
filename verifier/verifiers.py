__author__ = 'kguryanov'
import unittest


def verify_equals(actual, expected, message=None):
    unittest.TestCase.assertEqual(unittest.TestCase(), actual, expected, message)


def verify_type(actual, expected, message=None):
    unittest.TestCase.assertIsInstance(unittest.TestCase(), actual, expected, message)


def verify_not_equals(actual, expected, message=None):
    unittest.TestCase.assertNotEqual(unittest.TestCase(), actual, expected, message)
