from tkinter import*
from tkinter import messagebox as msg
root=Tk()
root.title("notepad")
root.geometry("766x566")
def hello():
    print("hello")

def help():
    value=msg.askquestion("experience","how was your experience")
    if(value=="yes"):
        msg.showinfo("rate","please rate us on appstore")
    else:
        msg.showinfo("help","tell us what went wrong")

# mainmenu=Menu(root)
# mainmenu.add_command(label="file",command=hello)
# mainmenu.add_command(label="save",command=hello)
# root.config(menu=mainmenu)

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="file",command=hello)
m1.add_command(label="save",command=hello)
m1.add_command(label="save as",command=hello)
m1.add_separator()
m1.add_command(label="new",command=hello)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=hello)
m2.add_command(label="copy",command=hello)
m2.add_command(label="paste",command=hello)
m2.add_separator()
m2.add_command(label="bold",command=hello)
m2.add_command(label="paste",command=hello)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Font",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="help",menu=m3)
root.mainloop()