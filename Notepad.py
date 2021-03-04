from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.geometry("644x788")
root.title("Untitled - Notepad")
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    text.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"- Notepad")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Shiv")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

text=Text(root,yscrollcommand=scrollbar.set,font="lucida 13")
file=None
text.pack(fill=BOTH,expand=True)
scrollbar.config(command=text.yview)

mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)
#To open new file
m1.add_command(label="New",command=newFile)
#To open already exsiting file
m1.add_command(label="Open",command=openFile)
#to save the current file
m1.add_command(label="Save",command=saveFile)
m1.add_separator()

#m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Exit",command=quitApp)
mainmenu.add_cascade(label="File",menu=m1)

#EDit menu starts
m2=Menu(mainmenu,tearoff=0)
#cut fature,copy,paste
#m2.add_command(label="Undo",command=myfunc)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
#m2.add_command(label="Delete",command=myfunc)
mainmenu.add_cascade(label="Edit",menu=m2)

#Help Menu
m3=Menu(mainmenu,tearoff=0)
#m3.add_command(label="View Help",command=myfunc)
m3.add_command(label="About Notepad",command=about)
mainmenu.add_cascade(label="Help",menu=m3)


root.config(menu=mainmenu)

root.mainloop()