from tkinter import*

root=Tk()
root.geometry("4444x333")

def getvalue():
    print(f"the value of username is{uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
username=Label(text="username",bg="black",fg="white")
password=Label(text="password",bg="red")
username.grid()
password.grid(row=1)


uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable= uservalue)
passentry=Entry(root, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="submit",command=getvalue).grid()
root.mainloop()