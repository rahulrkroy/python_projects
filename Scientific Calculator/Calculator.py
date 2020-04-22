from tkinter import *
from tkinter import messagebox
import math
# some variables
font1=('Verdana',22)
font2=('Ariel',13)
font3=('Verdana',18)
font4=('Verdana',14)
#some functions
def clickbutton(event):
    btn=event.widget
    text=btn['text']
    print(text)
    if text=='=':
        try:
            exp=textfield.get()
            print(exp)
            if exp.find('√')>=0:
                ans=math.sqrt(float(exp[1:]))
            elif exp.find('^')>=0:
                exp=exp.replace('^','**')
                ans=eval(exp)
            elif exp.find('ln')>=0:
                ans=math.log(float(exp[2:]))
            elif exp.find('log')>=0:
                ans=math.log10(float(exp[3:]))
            elif exp.find('e')>=0:
                r=exp.find('e')
                newexp=exp[0:r]+str(math.e)+exp[r+1:]
                ans=eval(newexp)
            else:
                ans=eval(exp)
            print(ans)
            textfield.delete(0,END)
            textfield.insert(END,ans)
        except Exception as e:
            print("Error......",e)
            messagebox.showerror("Error","Invalid Expression")

    elif text=='x':
        textfield.insert(END,'*')
    else:
        textfield.insert(END,text)

def clear():
    ex=textfield.get()
    ex=ex[:-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)


def enterClicked(event):
    e=Event()
    e.widget=equalButton
    clickbutton(e)


#create window
root=Tk()
root.title("My Calculator")
root.geometry("450x500")
#adding picture label
pic=PhotoImage(file='/home/shikari/python_projects/Scientific Calculator/Calculator-icon-64.png')
headingLabel=Label(root,image=pic)
headingLabel.pack(side=TOP, pady=10)
#heading label
heading=Label(root,text="My Calculator",font=font1,underline=0)
heading.pack(side=TOP)
# text field
textfield=Entry(root,font=font1,justify=RIGHT)
textfield.pack(side=TOP, pady=10, padx=5, fill=X)
# buttons
buttonFrame=Frame(root)
buttonFrame.pack(side=TOP)
# adding buttons in frame

temp=1
for i in range(3):
    for j in range(3):
        numButton=Button(buttonFrame,text=str(temp),font=font1,width=4, relief=GROOVE,activebackground='ORANGE', activeforeground='White')
        numButton.grid(row=2-i,column=j , padx=2, pady=5)
        temp+=1
        numButton.bind('<Button-1>',clickbutton)

zeroButton=Button(buttonFrame,text='0',font=font1,width=4, relief=GROOVE,activebackground='ORANGE', activeforeground='White')
zeroButton.grid(row=3,column=0 , padx=2, pady=5)
zeroButton.bind('<Button-1>',clickbutton)

dotButton=Button(buttonFrame,text='.',font=font1,width=4, relief=GROOVE,activebackground='ORANGE', activeforeground='White')
dotButton.grid(row=3,column=1 , padx=2, pady=5)
dotButton.bind('<Button-1>',clickbutton)

equalButton=Button(buttonFrame,text='=',font=font1,width=4, relief=GROOVE,activebackground='Blue', activeforeground='White')
equalButton.grid(row=3,column=2 , padx=2, pady=5)
equalButton.bind('<Button-1>',clickbutton)
plusButton=Button(buttonFrame,text='+',font=font1,width=3, relief=GROOVE,activebackground='Red', activeforeground='White')
plusButton.grid(row=3,column=3 , padx=5, pady=5)
plusButton.bind('<Button-1>',clickbutton)
minusButton=Button(buttonFrame,text='-',font=font1,width=3, relief=GROOVE,activebackground='Red', activeforeground='White')
minusButton.grid(row=2,column=3 , padx=5, pady=5)
minusButton.bind('<Button-1>',clickbutton)
multiplyButton=Button(buttonFrame,text='x',font=font1,width=3, relief=GROOVE,activebackground='Red', activeforeground='White')
multiplyButton.grid(row=1,column=3 , padx=5, pady=5)
multiplyButton.bind('<Button-1>',clickbutton)
divideButton=Button(buttonFrame,text='/',font=font1,width=3, relief=GROOVE,activebackground='Red', activeforeground='White')
divideButton.grid(row=0,column=3 , padx=5, pady=5)
divideButton.bind('<Button-1>',clickbutton)
delButton=Button(buttonFrame,text='<--',font=font1,width=10, relief=GROOVE,activebackground='Brown', activeforeground='White',command=clear)
delButton.grid(row=4,column=0 ,columnspan=2, padx=5, pady=5)

clearButton=Button(buttonFrame,text='AC',font=font1,width=9, relief=GROOVE,activebackground='Maroon', activeforeground='White',command=lambda:textfield.delete(0,END))
clearButton.grid(row=4,column=2 ,columnspan=2, padx=5, pady=5)

textfield.bind('<Return>',enterClicked)

#################################################################################################################################################
# Scientific part

def calculateSc(event):
    btn=event.widget
    text=btn['text']
    print(text)
    ans=''
    if text=='√': 
        ans='√'
    elif text=='^':
        exp=textfield.get()
        ans=str(exp)+'^'
    elif text=='x!':
        exp=float(textfield.get())
        ans=str(math.factorial(exp))
    elif text=='sin':
        exp=float(textfield.get())
        ans=str(math.sin(math.radians(exp)))
    elif text=='cos':
        exp=float(textfield.get())
        ans=str(math.cos(math.radians(exp)))
    elif text=='tan':
        exp=float(textfield.get())
        ans=str(math.tan(math.radians(exp)))
    elif text=='e':
        exp=textfield.get()
        ans=exp+'e'
    elif text=='ln':
        ans='ln'
    elif text=='log':
        ans='log'
    elif text=='|x|':
        exp=float(textfield.get())
        if(exp>0):
            ans=str(exp)
        else:
            ans=str((0-exp))
    elif text=='rad':
        exp=float(textfield.get())
        ans=str(math.radians(exp))
    elif text=='deg':
        exp=float(textfield.get())
        ans=str(math.degrees(exp))
    textfield.delete(0,END)
    textfield.insert(0,ans)




scFrame=Frame(root)
sqrtButton=Button(scFrame,text='√',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
sqrtButton.grid(row=0,column=0,padx=5, pady=5)
powButton=Button(scFrame,text='^',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
powButton.grid(row=0,column=1,padx=5, pady=5 )
factButton=Button(scFrame,text='x!',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
factButton.grid(row=0,column=2,padx=5, pady=5 )
sinButton=Button(scFrame,text='sin',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
sinButton.grid(row=0,column=3,padx=5, pady=5 )
cosButton=Button(scFrame,text='cos',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
cosButton.grid(row=0,column=4,padx=4, pady=5 )
tanButton=Button(scFrame,text='tan',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
tanButton.grid(row=0,column=5,padx=4, pady=5 )

eButton=Button(scFrame,text='e',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
eButton.grid(row=1,column=0,padx=5, pady=5)
lnButton=Button(scFrame,text='ln',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
lnButton.grid(row=1,column=1,padx=5, pady=5 )
logButton=Button(scFrame,text='log',font=font3,width=2, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
logButton.grid(row=1,column=2,padx=5, pady=5 )
modButton=Button(scFrame,text='|x|',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
modButton.grid(row=1,column=3,padx=5, pady=5 )
radButton=Button(scFrame,text='rad',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
radButton.grid(row=1,column=4,padx=4, pady=5 )
degButton=Button(scFrame,text='deg',font=font3,width=3, relief=GROOVE,activebackground='Red', activeforeground='White', bg='gray',fg='white')
degButton.grid(row=1,column=5,padx=4, pady=5 )

powButton.bind('<Button-1>',calculateSc)
sqrtButton.bind('<Button-1>',calculateSc)
factButton.bind('<Button-1>',calculateSc)
sinButton.bind('<Button-1>',calculateSc)
cosButton.bind('<Button-1>',calculateSc)
tanButton.bind('<Button-1>',calculateSc)
eButton.bind('<Button-1>',calculateSc)
lnButton.bind('<Button-1>',calculateSc)
logButton.bind('<Button-1>',calculateSc)
modButton.bind('<Button-1>',calculateSc)
radButton.bind('<Button-1>',calculateSc)
degButton.bind('<Button-1>',calculateSc)


normalcalc=True

def scientificMode():
    global normalcalc
    if normalcalc:
        # Scietific mode on
        normalcalc=False
        print("SCclick")
        # remove buttonframe
        buttonFrame.pack_forget()
        # add scframe
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        root.geometry("450x600")
    else:
        # Normal mode on
        normalcalc=True
        print("show normal")
        scFrame.pack_forget()
        root.geometry("450x500")

menubar=Menu(root,relief=SUNKEN)
mode=Menu(menubar,font=font2,tearoff=0,relief=RAISED)
mode.add_checkbutton(label='Scientific Mode',command=scientificMode)
menubar.add_cascade(label='Mode',menu=mode)
root.config(menu=menubar)


root.mainloop()
