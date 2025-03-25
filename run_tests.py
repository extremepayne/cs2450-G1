import unittest


# runs all tests in the test directory with the right naming convention
# python3 run_tests.py
def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="test", pattern="*_tests.py")

    runner = unittest.TextTestRunner()
    runner.run(suite)


def parse_flags() -> None:
    pass  # will be implemented later


"""
    flags = {
        "-h": "help",
        "-v": "verbose",
    }
"""


if __name__ == "__main__":
    print("Running test suite via unittest...")
    print()
    parse_flags()
    run_all_tests()
