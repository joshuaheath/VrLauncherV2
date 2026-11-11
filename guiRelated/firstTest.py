from tkinter import *

root = Tk()
root.title("My First GUI")
root.geometry("300x200")


lbl = Label(root, text="Hello, Tkinter!")
lbl.pack()

def clicked():
    lbl.config(text="Button clicked!")

btn = Button(root, text="Click Me", command=clicked)
btn.pack()

entry = Entry(root)
entry.pack()

root.mainloop()