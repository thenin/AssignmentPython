__author__ = 'kguryanov'

import pkgutil
import unittest
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--package', metavar='T', type=str, nargs='*', default=['test'],
                    help='List of locations for test modules search.')

args = parser.parse_args()
print(vars(args)['package'])

def main():
    modules = []
    for package in vars(args)['package']:
        print(package)
        modules = modules + ([package + "." + name for _, name, _ in pkgutil.iter_modules([package])])

    print("Found modules: " + str(modules))

    suite = unittest.TestSuite()

    for module in modules:
        try:
            mod = __import__(module, globals(), locals(), ['suite'])
            suitefinal = getattr(mod, 'suite')
            suite.addTest(suitefinal())
        except (ImportError, AttributeError):
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(module))

    unittest.TextTestRunner().run(suite)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
