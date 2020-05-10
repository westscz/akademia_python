from tkinter import Tk, Button

root = Tk()
root.geometry("200x200")

click_button = Button(root, text="Click me!", width=8)
click_button.pack()

root.mainloop()
