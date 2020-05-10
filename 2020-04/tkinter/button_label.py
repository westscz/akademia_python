from tkinter import Tk, Label, Button


def click_action(button):
    button.config(text=f"Wow!")


root = Tk()
root.geometry("200x200")

text_label = Label(root, text="Some text")
click_button = Button(root, text="Click me!", width=8)

click_button.pack()
text_label.pack()


click_button.config(command=lambda: click_action(click_button))

root.mainloop()
