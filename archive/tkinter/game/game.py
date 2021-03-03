from random import choice
from tkinter import Tk, Label, Button


available_choices = ["paper", "rock", "scissors"]


def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text="Tie! Try again!", fg="blue")
    elif is_user_winner:
        text_label.config(text="You win... Let's play again", fg="green")
    else:
        text_label.config(text="I win, I win!", fg="red")


root = Tk()
root.title("Paper, Rock, Scissors")
root.geometry("300x150")

text_label = Label(root, font=40, text="Let's play paper, rock, scissors!")
text_label.pack()

Button(
    root,
    anchor="w",
    text="📃 Paper",
    font=40,
    width=10,
    command=lambda: play_cmd("paper"),
).pack()

Button(
    root, anchor="w", text="🤘 Rock", font=40, width=10, command=lambda: play_cmd("rock")
).pack()

Button(
    root,
    anchor="w",
    text="✂️ Scissors",
    font=40,
    width=10,
    command=lambda: play_cmd("scissors"),
).pack()

root.mainloop()
