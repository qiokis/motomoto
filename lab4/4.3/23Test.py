import unittest
from lab4 import tasks


class TestTask3(unittest.TestCase):

    def test_no_such_file(self):
        self.assertRaises(FileNotFoundError, tasks.task3("txt.txt"))

    def test_empty_file(self):
        self.assertEqual([], tasks.task3("empty_file.txt"))

    def test_right_example(self):
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], tasks.task3("right_example.txt"))


if __name__ == "__main__":
    unittest.main()