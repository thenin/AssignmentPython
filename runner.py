__author__ = 'kguryanov'

import pkgutil
import unittest

default_package_name = "test"


def main():
    modules = []
    package_name = default_package_name

    modules = modules + ([package_name + "." + name for _, name, _ in pkgutil.iter_modules([package_name])])
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
