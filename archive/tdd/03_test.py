"""https://docs.python.org/3/library/stdtypes.html#str.find"""

import unittest


def str_find(text, sub):
    for i, c in enumerate(text):
        if c == sub:
            return i
    # return -1


class TestStrFind(unittest.TestCase):
    def test_find_letter_in_text(self):
        text = "Python"
        sub = "P"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_letter_not_in_text(self):
        text = "Python"
        sub = "m"
        self.assertEqual(str_find(text, sub), text.find(sub))


if __name__ == "__main__":
    unittest.main()
