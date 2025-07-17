from tkinter import*
root=Tk()
root.geometry("555x456")

def getvals():
    print(f"{namevalue.get(),numbervalue.get(),addressvalue.get(),destinationvalue.get(),checkvalue.get()}\n")
    with open("records.txt","a") as fl:
        fl.write(f"{namevalue.get(),numbervalue.get(),addressvalue.get(),destinationvalue.get(),checkvalue.get()}\n")

heading=Label(root,text="welcome to Tanishq travells",font="comicsansms 13 bold italic underline")
heading.grid(row=0,column=3,pady=34)

name=Label(root,text="enter your name")
number=Label(root,text="enter your number")
address=Label(root,text="enter your address")
destinaion=Label(root,text="enter your destination")


name.grid(row=1,column=1)
number.grid(row=2,column=1)
address.grid(row=3,column=1)
destinaion.grid(row=4,column=1)

namevalue=StringVar()
numbervalue=StringVar()
addressvalue=StringVar()
destinationvalue=StringVar()
checkvalue=IntVar()

nameenter=Entry(root,textvariable=namevalue).grid(row=1,column=3)
numberenter=Entry(root,textvariable=numbervalue).grid(row=2,column=3)
addressenter=Entry(root,textvariable=addressvalue).grid(row=3,column=3)
destinationenter=Entry(root,textvariable=destinationvalue).grid(row=4,column=3)

checkenter=Checkbutton(text="do you agree with the terms",variable=checkvalue)
checkenter.grid(row=5,column=3)

button=Button(text="submit",command=getvals)
button.grid(row=6,column=3)






root.mainloop()