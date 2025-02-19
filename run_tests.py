import unittest


# runs all tests in the test directory with the right naming convention
# python3 run_tests.py
def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="test", pattern="*_tests.py")

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()
