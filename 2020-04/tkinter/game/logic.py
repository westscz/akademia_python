available_choices = ["paper", "rock", "scissors"]


def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


import unittest

paper = "paper"
rock = "rock"
scissors = "scissors"


class PlayTest(unittest.TestCase):
    def test_user_win(self):
        self.assertTrue(play(paper, rock))
        self.assertTrue(play(rock, scissors))
        self.assertTrue(play(scissors, paper))

    def test_cpu_win(self):
        self.assertFalse(play(rock, paper))
        self.assertFalse(play(scissors, rock))
        self.assertFalse(play(paper, scissors))

    def test_tie(self):
        self.assertIsNone(play(rock, rock))
        self.assertIsNone(play(paper, paper))
        self.assertIsNone(play(scissors, scissors))


if __name__ == "__main__":
    unittest.main()
