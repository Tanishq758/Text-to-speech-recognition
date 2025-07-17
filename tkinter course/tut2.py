from tkinter import*
from PIL import Image,ImageTk

tut1_root=Tk()
tut1_root.geometry("733x344")
tanishq=Label(text="this is the first gui made by me")
tanishq.pack()

image=Image.open("D:\\vsc\\tkinter course\\Photo.jpg")
photo=ImageTk.PhotoImage(image)

labelimage=Label(image=photo)
labelimage.pack()

tut1_root.mainloop()

