import re
import hashlib
import unittest
from lab4 import tasks


class TestTask2(unittest.TestCase):

    def test_no_such_file(self):
        self.assertRaises(FileNotFoundError, tasks.task2("txt.txt"))

    def test_right_example(self):
        expected_hash = hashlib.md5()
        with open(r"test_right_example_expected.txt", "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                expected_hash.update(data)

        actual_hash = hashlib.md5()
        with open(tasks.task2("test_right_example_actual.txt"), "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                actual_hash.update(data)
        self.assertEqual(expected_hash.hexdigest(), actual_hash.hexdigest())

    def test_empty_file(self):
        expected_hash = hashlib.md5()
        with open(r"test_empty_file_expected.txt", "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                expected_hash.update(data)

        actual_hash = hashlib.md5()
        with open(tasks.task2(r"test_empty_file_actual.txt"), "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                actual_hash.update(data)
        self.assertEqual(expected_hash.hexdigest(), actual_hash.hexdigest())


if __name__ == "__main__":
    unittest.main()