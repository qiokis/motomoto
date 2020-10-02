from lab4 import tasks
import unittest

class TestTask5(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual("", tasks.task5(""))

    def test_only_letters(self):
        self.assertEqual("", tasks.task5("asdad afashwgw asdasda"))

    def test_right_example(self):
        self.assertEqual("1231312", tasks.task5("afagaga1231312 safhasdfhdsfh4652165fdfg"))

if __name__ == "__main__":
    unittest.main()