"""https://docs.python.org/3/library/stdtypes.html#str.find"""

import unittest


def str_find(text, sub):
    sub_len = len(sub)
    for i in range(len(text) - sub_len + 1):
        if text[i : i + sub_len] == sub:
            return i
    return -1


class TestStrFind(unittest.TestCase):
    def test_find_letter_in_text(self):
        text = "Python"
        sub = "P"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_letter_not_in_text(self):
        text = "Python"
        sub = "m"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_find_substring_in_text(self):
        text = "Python"
        sub = "hon"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_find_text_in_text(self):
        text = "Python"
        sub = "Python"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_find_sub_bigger_than_text(self):
        text = "Python"
        sub = "Pythonistas"
        self.assertEqual(str_find(text, sub), text.find(sub))

    def test_find_sub_after_start(self):
        text = "Pythoononn"
        sub = "on"
        self.assertEqual(str_find(text, sub, 7), text.find(sub, 7))


if __name__ == "__main__":
    unittest.main()
