from tkinter import Tk, Button


def click_action(button):
    button.config(text=f"Wow!")


root = Tk()
root.geometry("200x200")

click_button = Button(root, text="Click me!", width=8)
click_button.pack()

click_button.config(command=lambda: click_action(click_button))

root.mainloop()
