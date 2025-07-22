import unittest
from codegen import generate_code

class TestCodegen(unittest.TestCase):

    def test_generate_code_create_file(self):
        command = {"command": "create_file", "filename": "my_file.txt"}
        code = generate_code(command)
        self.assertEqual(code, "with open('my_file.txt', 'w') as f:\n    f.write('Hello, World!')")

    def test_generate_code_unknown_command(self):
        command = {"command": "unknown"}
        code = generate_code(command)
        self.assertIsNone(code)

if __name__ == '__main__':
    unittest.main()
