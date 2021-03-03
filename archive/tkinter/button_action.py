from tkinter import Tk, Button


def click_action():
    print("Wow!")


root = Tk()
root.geometry("200x200")

click_button = Button(root, text="Click me!", width=8, command=click_action)
click_button.pack()

root.mainloop()
