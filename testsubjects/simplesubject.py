__author__ = 'kguryanov'

class SimpleSubject:
    @staticmethod
    def do_sum(*args):
        return sum(args)

    @staticmethod
    def do_multiply(a, b):
        return a * b
