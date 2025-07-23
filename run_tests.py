import unittest
import sys

# Add the app directory to the path so we can import the modules
sys.path.append("app")

# Discover and run the tests
loader = unittest.TestLoader()
suite = loader.discover("tests")
runner = unittest.TextTestRunner()
runner.run(suite)
