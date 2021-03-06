__author__ = 'kguryanov'

import unittest
from testsubjects import simplesubject
from testsubjects.simpleclasssubject import SimpleSubjectClass
from verifier import verifiers


class TestCaseNegative(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Starting negative test sequence")

    @classmethod
    def tearDownClass(cls):
        print("Finished negative test sequence")

    def setUp(self):
        print("Starting test")

    def tearDown(self):
        print("Finishing test")

    def test_simple_positive_comparison(self):
        verifiers.Verifiers.verify_equals(1, simplesubject.SimpleSubject.do_sum(1, 2, 3, 4))

    def test_simple_negative_comparison(self):
        verifiers.Verifiers.verify_not_equals(10, simplesubject.SimpleSubject.do_sum(1, 2, 3, 4), 'Comparison failed')

    def test_verify_type(self):
        verifiers.Verifiers.verify_type(1000, str, "Incorrect type")

    def test_verify_returns_int(self):
        verifiers.Verifiers.verify_returns(100, simplesubject.SimpleSubject.do_sum, 1, 2, 3, 4)

    def test_verify_returns_str(self):
        verifiers.Verifiers.verify_returns("Foo", SimpleSubjectClass().do_reverse, "Foo")


if __name__ == '__main__':
    unittest.main()
