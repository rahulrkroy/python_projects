from tkinter import *
import backend
root=Tk()
root.wm_title("Book Store")
selectedTuple=()

def viewFunction():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def searchFunction():
    list1.delete(0,END)
    for row in backend.search(e1.get(),e3.get(),e2.get(),e4.get()):
        list1.insert(END,row)

def addFunction():
    list1.delete(0,END)
    backend.insert(e1.get(),e3.get(),e2.get(),e4.get())
    list1.insert(END,(e1.get(),e3.get(),e2.get(),e4.get()))

def deleteFunction():
    list1.delete(0,END)
    print(selectedTuple[0])
    backend.delete(selectedTuple[0])
    viewFunction()

def updateFunction():
    list1.delete(0,END)
    backend.update(selectedTuple[0],e1.get(),e3.get(),e2.get(),e4.get())
    list1.insert(END,(e1.get(),e3.get(),e2.get(),e4.get()))

def closeFunction():
    root.destroy()


def getSelectedRow(event):
    global selectedTuple
    index=list1.curselection()[0]
    selectedTuple=list1.get(index)

    e1.delete(0,END)
    e1.insert(END,selectedTuple[1])
    e2.delete(0,END)
    e2.insert(END,selectedTuple[3])
    e3.delete(0,END)
    e3.insert(END,selectedTuple[2])
    e4.delete(0,END)
    e4.insert(END,selectedTuple[4])


l1=Label(root,text='Title')
l1.grid(row=0,column=0)
l2=Label(root,text='Year')
l2.grid(row=1,column=0)
l3=Label(root,text='Author')
l3.grid(row=0,column=2)
l4=Label(root,text='ISBN')
l4.grid(row=1,column=2)

e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
e3=Entry(root)
e3.grid(row=0,column=3)
e4=Entry(root)
e4.grid(row=1,column=3)

list1=Listbox(root,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind('<<ListboxSelect>>',getSelectedRow)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(root,text="View All",width=12,command=viewFunction)
b1.grid(row=2,column=3)
b2=Button(root,text="Close",width=12,command=closeFunction)
b2.grid(row=7,column=3)
b3=Button(root,text="Search Entry",width=12,command=searchFunction)
b3.grid(row=4,column=3)
b4=Button(root,text="Add Entry",width=12,command=addFunction)
b4.grid(row=3,column=3)
b5=Button(root,text="Update Selected",width=12,command=updateFunction)
b5.grid(row=6,column=3)
b6=Button(root,text="Delete Selected",width=12,command=deleteFunction)
b6.grid(row=5,column=3)


root.mainloop()