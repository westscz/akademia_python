from tkinter import Tk, Label

root = Tk()
root.title("App")
root.geometry("200x200")

label = Label(root, text="Look at me!", font=30, fg="blue")
label.pack()

root.mainloop()
