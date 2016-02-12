__author__ = 'kguryanov'

class SimpleSubject:
    @staticmethod
    def do_sum(*args):
        return sum(args)

    @staticmethod
    def do_reverse(in_str):
        return in_str[::-1]
