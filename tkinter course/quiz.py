from tkinter import*
from tkinter import messagebox as msg
root=Tk()
def addfile():
    with open("records.txt","a")as f1:
        f1.write(f"the customer rating was {slidebar.get()}")
    msg.showinfo("thankyou","thankyou for visiting, have a nice day")

root.geometry("555x555")
Label(root,text="How was your experience , please rate us").pack()
slidebar=Scale(root,from_=0,to=10,orient=HORIZONTAL)
slidebar.pack()
Button(text="Submit",command=addfile).pack()
root.mainloop()