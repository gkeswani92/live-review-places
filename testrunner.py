import optparse
import sys
import unittest


USAGE = """%prog TEST_PATH
Run unit tests for Map Nearby Places App.
TEST_PATH   Path to package containing test modules"""


def run_test_suite(test_path):
    # Discover and run tests.
    suite = unittest.loader.TestLoader().discover(test_path, pattern="*test.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Fail the build if the suite was not successful!
    if not result.wasSuccessful():
        sys.exit(result)


if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    if len(args) != 1:
        print 'Error: Exactly 1 arguments required.'
        parser.print_help()
        sys.exit(1)
    TEST_PATH = args[0]
    run_test_suite(TEST_PATH)
