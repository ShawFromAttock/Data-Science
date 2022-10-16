from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('D:/bytewise/icon.ico')


def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('D:/bytewise/icon.ico')
    my_img = ImageTk.PhotoImage(Image.open("D:/bytewise/wp4595447-joji-slow-dancing-in-the-dark-wallpapers.jpg"))
    Label(top, image=my_img).pack()
    Button(top, text="close window", command=top.destroy).pack()


Button(root, text="Open Second Window", command=open).pack()

mainloop()
