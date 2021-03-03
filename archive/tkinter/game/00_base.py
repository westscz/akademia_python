from tkinter import Tk, Label, Button

root = Tk()
root.title("Paper, Rock, Scissors")
root.geometry("300x150")

text_label = Label(root, font=40, text="Let's play paper, rock, scissors!")
text_label.pack()

root.mainloop()
