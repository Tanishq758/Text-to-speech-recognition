from tkinter import*

root=Tk()
def size():
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")
root.geometry("444x445")

width=Label(root,text="enter width").grid(row=0,column=1)
height=Label(root,text="enter height").grid(row=1,column=1)
widthvalue=StringVar()
heightvalue=StringVar()

widthenter=Entry(root,textvariable=widthvalue).grid(row=0,column=2)
heightenter=Entry(root,textvariable=heightvalue).grid(row=1,column=2)

Button(text="resize",command=size).grid(row=5,column=2,padx=45,pady=56)
root.mainloop()