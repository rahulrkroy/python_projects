import json
from difflib import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=1000,bg='#263D42')
canvas.pack()
frame=tk.Frame(root,bg='white')
frame.place(relwidth=0.95,relheight=0.9,relx=0.025,rely=0.05)

frame2=tk.Frame(frame,bg='white')
frame2.place(relheight=0.5,relx=0.5,rely=0.55,anchor='center')


label1=tk.Label(frame,text='Enter the word')
label1.pack()

filepath='/home/shikari/python_projects/working dictionery/dict_data.json'
data=json.load(open(filepath))


def findMeaning(s):
    for widget in frame2.winfo_children():
        widget.destroy()
    if s in data:
        lab=tk.Label(frame2,text=s,bg='white',font=("Ariel",20))
        lab.pack()
        for i in range(len(data[s])):
            label=tk.Label(frame2,text=str(i+1)+'.  '+data[s][i],bg='white', wraplength=900)
            label.pack()
    elif(len(get_close_matches(s,data.keys()))>0):
        word=get_close_matches(s,data.keys())[0]
        display=s+" not found. Did you mean "+word
        
        msgbox=messagebox.askquestion('Not Found',display)
        if(msgbox=='yes'):
            findMeaning(word)
        else:
            text="The word {} doesnt exist. Please recheck".format(s)
            messagebox.showinfo("Error",text)
            
    else:
        text="The word {} doesnt exist. Please recheck".format(s)
        messagebox.showinfo("Error",text)

def meaning():
    w=enterWord.get().lower()
    findMeaning(w)

    
enterWord=Entry(frame)
enterWord.pack()

getword=tk.Button(frame,text="Search Meaning", padx=10,pady=5, fg='white', bg='#263D42',command=meaning)
getword.pack()

#enterWord=input("Enter the word whose meaning you wanna find \n").lower()
#findMeaning(enterWord)


root.mainloop()