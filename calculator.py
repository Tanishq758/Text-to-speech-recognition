# from tkinter import *
# root=Tk()
# root.title("calculator")
# root.geometry("677x666")

# def click(event):
#     global scalval
#     text=event.widget.cget("text")
#     if text =="=":
#         if scalval.get().isdigit():
#             value= int(scalval.get())
#         else:
#             value=eval(screen.get())
#         scalval.set(value)
#         scalval.update()
#     elif text=="C":
#         scalval.set("")
#         scalval.update()
#     else:
#         scalval.set(scalval.get()+text)
#         scalval.update()

# scalval=StringVar()
# scalval.set("")
# screen=Entry(root,textvar=scalval,font="lucida 40 bold")
# screen.pack(fill=X,ipadx=8,padx=10,pady=10)

# bpadx=2

# f=Frame(root,bg="grey",width="400",height="600")
# b=Button(f,text="9",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="8",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="7",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)

# f=Frame(root,bg="grey")
# b=Button(f,text="6",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="5",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="4",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)

# f=Frame(root,bg="grey")
# b=Button(f,text="3",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="2",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="1",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)

# f=Frame(root,bg="grey")
# b=Button(f,text="0",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="=",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="C",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)

# f=Frame(root,bg="grey")
# b=Button(f,text="+",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="-",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="*",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)


# f=Frame(root,bg="grey")
# b=Button(f,text="/",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="%",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# b=Button(f,text="",padx=bpadx, pady=2,font="lucida 35 bold")
# b.pack(side=LEFT,padx=bpadx,pady=1)
# b.bind("<Button-1>",click)

# # f.pack_propagate(0)
# f.pack()
# # f.pack_propagate(0)








# root.mainloop()



from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("400x550")
root.configure(bg="black")

# Entry field
expression = StringVar()
entry = Entry(root, textvar=expression, font="lucida 30 bold", bd=10, relief=SUNKEN, justify=RIGHT)
entry.pack(fill=X, ipadx=8, padx=10, pady=20)

# Button click handler
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression.get()))
            expression.set(result)
        except:
            expression.set("Error")
    elif text == "C":
        expression.set("")
    else:
        expression.set(expression.get() + text)

# Button layout
button_rows = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# Create buttons row by row
for row in button_rows:
    frame = Frame(root, bg="black")
    for item in row:
        btn = Button(frame, text=item, font="lucida 20 bold", padx=20, pady=20, bd=4, width=4, bg="#333", fg="white", activebackground="orange")
        btn.pack(side=LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack(pady=5)

root.mainloop()
