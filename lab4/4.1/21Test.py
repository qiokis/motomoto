import unittest
from lab4 import tasks


class TestTask1(unittest.TestCase):

    def test_empty_string(self):
        assert tasks.task1("") == ""

    def test_right_example(self):
        assert tasks.task1("asd dsa") == ["asd dsa"]

    def test_one_word(self):
        assert tasks.task1("asd") == ""

    def test_notright_example(self):
        assert tasks.task1("as6 6sa") == ""

    def test_three_words(self):
        assert tasks.task1("asd dsa abc") == ["asd dsa", "dsa abc"]


if __name__ == "__main__":
    unittest.main()
