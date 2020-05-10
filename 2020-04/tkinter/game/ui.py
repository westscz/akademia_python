from tkinter import Tk, Label, Button


root = Tk()
root.title("Paper, Rock, Scissors")
root.geometry("300x150")

text_label = Label(root, font=40, text="Let's play paper, rock, scissors!")
text_label.pack()

Button(root, text="📃 Paper", font=40, width=10).pack()

Button(root, text="🤘 Rock", font=40, width=10).pack()

Button(root, text="✂️ Scissors", font=40, width=10).pack()

root.mainloop()
