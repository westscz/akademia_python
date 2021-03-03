"""https://docs.python.org/3/library/stdtypes.html#str.find"""

import unittest


class TestStrFind(unittest.TestCase):
    def test_find_letter_in_text(self):
        text = "Python"
        sub = "P"
        self.assertEqual(str_find(sub, text), text.find(sub))


if __name__ == "__main__":
    unittest.main()
