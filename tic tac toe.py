from tkinter import *
import tkinter.messagebox

root=Tk()
root.geometry('1150x760+0+0')
root.title("TIC TAC TOE")
root.configure(background='Orange')


click=True
buttons=StringVar

def checker(buttons):
    global click
    if click==True and buttons['text']=='':
        buttons['text']='X'
        click=False
        scoreckecker('X')
    elif click==False and buttons['text']=='':
        buttons['text']='O'
        click=True
        scoreckecker('O')

def scoreckecker(val):
    if button1['text']==val and button2['text']==val and button3['text']==val:
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        win(val)
    elif button4['text']==val and button5['text']==val and button6['text']==val:
        button4.configure(background='powder blue')
        button5.configure(background='powder blue')
        button6.configure(background='powder blue')
        win(val)
    elif button7['text']==val and button8['text']==val and button9['text']==val:
        button7.configure(background='powder blue')
        button8.configure(background='powder blue')
        button9.configure(background='powder blue')
        win(val)
    elif button1['text']==val and button4['text']==val and button7['text']==val:
        button1.configure(background='powder blue')
        button4.configure(background='powder blue')
        button7.configure(background='powder blue')
        win(val)
    elif button2['text']==val and button5['text']==val and button8['text']==val:
        button2.configure(background='powder blue')
        button5.configure(background='powder blue')
        button8.configure(background='powder blue')
        win(val)
    elif button3['text']==val and button6['text']==val and button9['text']==val:
        button3.configure(background='powder blue')
        button6.configure(background='powder blue')
        button9.configure(background='powder blue')
        win(val)
    elif button1['text']==val and button5['text']==val and button9['text']==val:
        button1.configure(background='powder blue')
        button5.configure(background='powder blue')
        button9.configure(background='powder blue')
        win(val)
    elif button3['text']==val and button5['text']==val and button7['text']==val:
        button7.configure(background='powder blue')
        button5.configure(background='powder blue')
        button3.configure(background='powder blue')
        win(val)
    
        

def win(val):
    if val =='X':
        n=int(playerX.get())
        playerX.set(n+1)
    else:
        n=int(playerY.get())
        playerY.set(n+1)
    tkinter.messagebox.showinfo("Winner",'Player {} has won this round'.format(val))


def reset():
    button1['text']=''
    button2['text']=''
    button3['text']=''
    button4['text']=''
    button5['text']=''
    button6['text']=''
    button7['text']=''
    button8['text']=''
    button9['text']=''
    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')

def NewGame():
    reset()
    playerX.set(0)
    playerY.set(0)








top=Frame(root,bg='Cadet Blue', pady=2,width=1150,height=850,relief=RIDGE)
top.grid(row=0,column=0)

titleLabel=Label(top,font=('arial',40,'bold'),text='My TICK TOCK TOE game',bd=10,bg='Blue',fg='Yellow',justify=CENTER,relief=RIDGE)
titleLabel.grid(row=0,column=0)

mainFrame=Frame(root,bg='Powder Blue',bd=10,width=1200,height=800,relief=RIDGE)
mainFrame.grid(row=1,column=0)

leftFrame=Frame(mainFrame,bd=10,width=680,height=600,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame=Frame(mainFrame,bd=10,width=460,height=600,pady=2,padx=10,bg='Cadet Blue',relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1=Frame(rightFrame,bd=10,width=460,height=200,padx=10,pady=2,bg='blue',relief=RIDGE)
rightFrame1.grid(row=0,column=0)
rightFramemid=Frame(rightFrame,width=460,height=100,bg='Cadet blue')
rightFramemid.grid(row=1,column=0)
rightFrame2=Frame(rightFrame,bd=10,padx=10,pady=2,bg='blue',relief=RIDGE)
rightFrame2.grid(row=2,column=0)

playerX=IntVar()
playerY=IntVar()

playerX.set(0)
playerY.set(0)


playerXLabel=Label(rightFrame1,font=('arial',20,'bold'),text='Player X   :-',bd=10,bg='Blue',fg='Yellow',justify=CENTER)
playerXLabel.grid(row=0,column=0)

scoreplayerX=Entry(rightFrame1,text=playerX,font=('arial',20,'bold'),bd=2,bg='Blue',fg='Orange',width=16,justify=LEFT)
scoreplayerX.grid(row=0,column=1)

playerYLabel=Label(rightFrame1,font=('arial',20,'bold'),text='Player O   :-',bd=10,bg='Blue',fg='Yellow',justify=CENTER)
playerYLabel.grid(row=1,column=0)
scoreplayerY=Entry(rightFrame1,text=playerY,font=('arial',20,'bold'),bd=2,bg='Blue',fg='Orange',width=16,justify=LEFT)
scoreplayerY.grid(row=1,column=1)


buttonReset=Button(rightFrame2,text='RESET',font=('Times 20 bold'),height=1,width=26,bd=5,padx=30,pady=9,bg='gainsboro',command=reset)
buttonReset.grid(row=1,column=0)
buttonNewgame=Button(rightFrame2,text='New Game',font=('Times 20 bold'),height=1,width=26,bd=5,padx=30,pady=9,bg='gainsboro',command=NewGame)
buttonNewgame.grid(row=2,column=0)


button1=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(leftFrame,text='',font=('Times 26 bold'),height=5,width=10,bg='gainsboro',command=lambda: checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)





root.mainloop()