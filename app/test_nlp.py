import unittest
from nlp import process_input

class TestNlp(unittest.TestCase):

    def test_process_input_create_file(self):
        command = process_input("create a file named my_file.txt")
        self.assertEqual(command, {"command": "create_file", "filename": "my_file.txt"})

    def test_process_input_create_file_no_filename(self):
        command = process_input("create a file")
        self.assertEqual(command, {"command": "error", "message": "Could not determine filename."})

    def test_process_input_greet(self):
        command = process_input("hello there")
        self.assertEqual(command, {"command": "greet"})

    def test_process_input_unknown(self):
        command = process_input("I want to build a rocketship")
        self.assertEqual(command, {"command": "unknown"})

if __name__ == '__main__':
    unittest.main()
