from tkinter import *

root = Tk()


def myClick():
    my_label = Label(root, text="Clicked!")
    my_label.pack()


my_button = Button(root, text='Click Here', command=myClick, fg="blue")
my_button.pack()
root.mainloop()
