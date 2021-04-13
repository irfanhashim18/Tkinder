from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer")
#this is for fixing the size of the windows
# if we not use this the window will adjust auto
root.geometry("500x500")
root.iconbitmap("imageViewer.ico")

#close program button

button_quit =Button(root, text= "End Program", command = root.quit)
button_quit.pack()

#for using the picture in python we need to install a full module call pillow
#pip install pillow
#for calling it we will use from PIL(python image Library) import things

image_1 = ImageTk.PhotoImage(Image.open("image_1.png"))
lebal_1 = Label(image=image_1)
lebal_1.pack()








root.mainloop()
