from tkinter import*
root=Tk()
root.geometry("344x445")

def sayname():
    print("my name is god")
l1=Label(text="testing out buttons",bg="black",fg="yellow",borderwidth=5,relief="sunken")
l1.pack(side=LEFT,padx=34,pady=34)

frame=Frame(root,bg="red",borderwidth=3,relief="sunken")
frame.pack(side=LEFT)
l2=Label(frame,text="hello")
l2.pack()
# l1.grid()
# l2.grid(row=2)
frame2=Frame(root,bg="red",borderwidth=3,relief="sunken")
frame2.pack()
button=Button(frame2,text="click now",command=sayname)
button.pack()
root.mainloop()