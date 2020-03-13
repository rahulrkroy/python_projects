import tkinter as tk
from tkinter import filedialog,Text
import os
import subprocess, sys

root=tk.Tk()
apps=[]
savefile=r'/home/shikari/coding/python_Projects/save.txt'

if os.path.isfile(savefile):
    with open(savefile,'r')as f:
        tempapps=f.read().split(',')
        apps=[x for x in tempapps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir='/',title="Select File",filetypes=(("executables","*.exe"),("All Files dikhao","*.*")))
    if(filename!=()):
        apps.append(filename)

        for app in apps:
            label=tk.Label(frame,text=apps[-1],bg='gray')
            label.pack()

def runApp():
    #for windows,below line 
    # for app in apps:
    #     os.startfile(app)

    #for linux,below lines
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    for app in apps:
        subprocess.call([opener, app])
def deleteAll():
    if os.path.isfile(savefile):
        os.remove(savefile)
    global apps
    apps=[]
    for widget in frame.winfo_children():
        widget.destroy()

canvas=tk.Canvas(root,height=700,width=700,bg='#263D42')
canvas.pack()
frame=tk.Frame(root,bg='white')
frame.place(relwidth=0.7,relheight=0.7,relx=0.15,rely=0.15)

openfile=tk.Button(root,text="Open File", padx=10,pady=5, fg='white', bg='#263D42',command=addApp)
openfile.pack()

runapps=tk.Button(root,text="Run Apps", padx=10,pady=5, fg='white', bg='#263D42',command=runApp)
runapps.pack()

delAll=tk.Button(root,text="Delete All Apps", padx=10,pady=5, fg='white', bg='#263D42',command=deleteAll)
delAll.pack()


for app in apps:
    label=tk.Label(frame,text=apps[-1],bg='gray')
    label.pack()




root.mainloop()


with open(savefile,'w') as f:
    if apps!=[]:
        for app in apps:
            f.write(app+',')