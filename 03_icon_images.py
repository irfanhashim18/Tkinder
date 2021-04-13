from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title(" Learning Tkinder ")

# adding icon

root.iconbitmap("E:/tkinder/Project-ImageViewer/imageViewer.ico")


#import images
# tkinder support very little image formats to be usered..like gif etc
# for using other formats of the images we need to import Pillow(its a python image library)
# for tkinder its always two step process (1- you define a thing and then you pack it windows on screen or give location )
# 2- for images its a 2 step process


image1 = ImageTk.PhotoImage(Image.open(
    "E:/tkinder/Project-ImageViewer/image_2.png"))
image2 = ImageTk.PhotoImage(Image.open(
    "E:/tkinder/Project-ImageViewer/image_2.png"))
image3 = ImageTk.PhotoImage(Image.open(
    "E:/tkinder/Project-ImageViewer/image_3.png"))
image4 = ImageTk.PhotoImage(Image.open(
    "E:/tkinder/Project-ImageViewer/image_4.png"))
mylebal = Label(image=image1)
mylebal.grid(row=0, column=0, columnspan=3)


def forward():
    pass


def back():
    pass


# creating a exit program button
exit_button = Button(root, text="Exit Program", command=root.quit)
exit_button.grid(row=2, column=1)

forward_button = Button(root, text=">>", command=lambda: forward())
forward_button.grid(row=2, column=2)

back_button = Button(root, text="<<", command=lambda: back())
back_button.grid(row=2, column=0)

root.mainloop()
