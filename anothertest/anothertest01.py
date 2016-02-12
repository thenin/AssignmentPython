__author__ = 'kguryanov'

import unittest
from verifier import verifiers
from testsubjects.simpleclasssubject import SimpleSubjectClass


class AnotherTestCase01(unittest.TestCase):
    def setUp(self):
        print("Starting tests from alternative location test sequence")

    def test_string_types(self):
        testSUbject = SimpleSubjectClass()
        verifiers.Verifiers.verify_type(testSUbject.do_reverse("The quick brown fox jumps over the lazy dog"), str,
                                        "Types do not match")
    @unittest.expectedFailure
    def test_equals_negative(self):
        testSubject = SimpleSubjectClass()
        verifiers.Verifiers.verify_equals(testSubject.do_reverse("The quick brown fox jumps over the lazy dog"),
                                          "The quick brown fox jumps over the lazy dog")


if __name__ == '__main__':
    unittest.main()
