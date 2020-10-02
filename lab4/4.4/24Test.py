import hashlib
import unittest
from lab4 import tasks


class TestTask4(unittest.TestCase):

    def test_no_such_file(self):
        self.assertRaises(FileNotFoundError, tasks.task4("txt.txt", "txt1.txt"))

    def test_empty_file(self):
        expected_hash = hashlib.md5()
        with open(r"empty_file.txt", "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                expected_hash.update(data)

        actual_hash = hashlib.md5()
        with open(tasks.task4("empty_file.txt", "empty_result_file.txt"), "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                actual_hash.update(data)
        self.assertEqual(expected_hash.hexdigest(), actual_hash.hexdigest())

    def test_right_example(self):
        expected_hash = hashlib.md5()
        with open(r"right_example_actual.txt", "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                expected_hash.update(data)

        actual_hash = hashlib.md5()
        with open(tasks.task4("right_example_in.txt", "right_example_out.txt"), "rb") as f:
            while True:
                data = f.read(32)
                if not data:
                    break
                actual_hash.update(data)
        self.assertEqual(expected_hash.hexdigest(), actual_hash.hexdigest())


if __name__ == "__main__":
    unittest.main()