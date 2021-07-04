from Tkinter import *
import Tkinter
import tkMessageBox

def newgame():
    global new_game
    new_game=Toplevel()
    new_game.minsize(1000,900)
    new_game.title("NEW GAME")
    #game.grid()
    game=Frame(new_game,width=1000,height=900)
    filename = PhotoImage(file = "cat.gif")
    b1 = Button(game,width=250,bd=5,height=300,image=filename,relief='raised')
    b1.grid(row = 0,column = 0)
    filename2 = PhotoImage(file = "lion.gif")
    b2= Button(game,width=250,height=300,bd=5,image=filename2,relief='raised')
    b2.grid(row=0,column=1)
    filename3 = PhotoImage(file = "elephant.gif")
    b3= Button(game,width=250,height=300,bd=5,image=filename3,relief='raised')
    b3.grid(row=0,column=2)
    filename4=PhotoImage(file = "monkey.gif")
    b4= Button(game,width=250,height=300,bd=5,image=filename4,relief='raised')
    b4.grid(row=0,column=3)
    def rfsh():
        if(tkMessageBox.askyesno("clear all","Clear cookies and cache?")):
            tkMessageBox.showinfo("Success","Cookies and cache cleared!")
        else:
            tkMessageBox.showinfo("Failure","Cookies and cache not cleared!")
    #refresh,change and ok button
    b5=Button(game,fg="white",bg="red",width=10,height=3,text="OK",command=submit,relief='raised')
    b5.grid(row=1,column=1)
    b6=Button(game,fg="black",bg="green",width=10,height=3,text="CHANGE",command=new1,relief='raised')
    b6.grid(row=1,column=2)
    b7=Button(game,fg="white",bg="black",width=10,height=3,text="REFRESH",command=rfsh,relief='raised')
    b7.grid(row=1,column=3)
    game.grid()
    game.mainloop()

def new1():
    global new1
    new1=Toplevel(main)
    new1.minsize(1000,900)
    new1.title("refresh images")
    new_game.destroy()
    game=Frame(new1,width=1000,height=900)
    filename5 = PhotoImage(file = "cow.gif")
    b7 = Button(game,width=250,bd=5,height=300,image=filename5,relief='raised')
    b7.grid(row = 0,column = 0)
    filename8 = PhotoImage(file = "zebra.gif")
    b8= Button(game,width=250,height=300,bd=5,image=filename8,relief='raised')
    b8.grid(row=0,column=1)
    filename9 = PhotoImage(file = "dog.gif")
    b9= Button(game,width=250,height=300,bd=5,image=filename9,relief='raised')
    b9.grid(row=0,column=2)
    filename10=PhotoImage(file = "tiger.gif")
    b10= Button(game,width=250,height=300,bd=5,image=filename10,relief='raised')
    b10.grid(row=0,column=3)
    #change and ok button
    b11=Button(game,fg="black",bg="green",width=10,height=3,text="CHANGE",command=new2,relief='raised')
    b11.grid(row=1,column=0)
    b12=Button(game,fg="white",bg="red",width=10,height=3,text="OK",command=submit1,relief='raised')
    b12.grid(row=1,column=2)
    game.grid()
    game.mainloop()


def new2():
    new2=Toplevel(main)
    new2.minsize(1000,900)
    new2.title("refresh images")
    new1.destroy()
    game=Frame(new2,width=1000,height=900)
    filename5 = PhotoImage(file = "cat.gif")
    b7 = Button(game,width=250,bd=5,height=300,image=filename5,relief='raised')
    b7.grid(row = 0,column = 0)
    filename8 = PhotoImage(file = "monkey.gif")
    b8= Button(game,width=250,height=300,bd=5,image=filename8,relief='raised')
    b8.grid(row=0,column=1)
    filename9 = PhotoImage(file = "deer.gif")
    b9= Button(game,width=250,height=300,bd=5,image=filename9,relief='raised')
    b9.grid(row=0,column=2)
    filename10=PhotoImage(file = "goat.gif")
    b10= Button(game,width=250,height=300,bd=5,image=filename10,relief='raised')
    b10.grid(row=0,column=3)
    #change and ok button
    b11=Button(game,fg="black",bg="green",width=10,height=3,text="CHANGE",command=alert,relief='raised')
    b11.grid(row=1,column=0)
    b12=Button(game,fg="white",bg="red",width=10,height=3,text="OK",command=submit2,relief='raised')
    b12.grid(row=1,column=2)
    game.grid()
    game.mainloop()

    #further more change button will not work
def alert():
    tkMessageBox.showinfo("select ok button","change will not work further more")




    
def submit():
    submit=Toplevel(main)
    submit.minsize(1300,800)
    submit.title("NAME OF IMAGES")
    new_game.destroy()
    #frame.grid()
    frame=Frame(submit,width=1000,height=900)
    print "THERE WILL BE NEGATIVE MARKING"
   
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10= IntVar()

    def total():
        submit.destroy()
        check1=CheckVar1.get()
        check2= CheckVar2.get()
        check3= CheckVar3.get()
        check4= CheckVar4.get()
        check5= CheckVar5.get()
        check6= CheckVar6.get()
        check7= CheckVar7.get()
        check8= CheckVar8.get()
        check9= CheckVar9.get()
        check10= CheckVar10.get()
        marks = 4*(check1+check3+check4+check5)-1*(check2+check6+check7+check8+check9+check10)
        tkMessageBox.showinfo("Total Score","your score is "+str(marks))

    
    
    C1 = Checkbutton(frame, text = "cat", variable = CheckVar1, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C1.grid(row=0,column=0)
    C2 = Checkbutton(frame, text = "cow", variable = CheckVar2, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C2.grid(row=1,column=0)
    C3= Checkbutton(frame, text =  "lion", variable = CheckVar3,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C3.grid(row=2,column=0)
    C4= Checkbutton(frame, text=   "elephant", variable = CheckVar4,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C4.grid(row=3,column=0)
    C5= Checkbutton(frame, text=   "monkey", variable = CheckVar5,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C5.grid(row=4,column=0)
    C6 = Checkbutton(frame, text = "zebra", variable = CheckVar6, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C6.grid(row=5,column=0)
    C7 = Checkbutton(frame, text = "dog", variable = CheckVar7, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C7.grid(row=6,column=0)
    C8= Checkbutton(frame, text =  "tiger", variable = CheckVar8,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C8.grid(row=7,column=0)
    C9= Checkbutton(frame, text =  "deer", variable = CheckVar9,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C9.grid(row=8,column=0)
    C10= Checkbutton(frame, text = "goat", variable = CheckVar10,
         onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C10.grid(row=9,column=0)

    submitbutton= Button(frame, text="submit",fg="white",bg="red",
                 width=20, height=3,command=total,relief='raised')
    submitbutton.grid(row=5,column=1)
    frame.grid()
    frame.mainloop()


def submit1():
    submit=Toplevel(main)
    submit.minsize(1300,800)
    submit.title("NAME OF IMAGES")
    new1.destroy()
    #frame.grid()
    frame=Frame(submit,width=1000,height=900)
   
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10= IntVar()

    def total():
        submit.destroy()
        check1=CheckVar1.get()
        check2= CheckVar2.get()
        check3= CheckVar3.get()
        check4= CheckVar4.get()
        check5= CheckVar5.get()
        check6= CheckVar6.get()
        check7= CheckVar7.get()
        check8= CheckVar8.get()
        check9= CheckVar9.get()
        check10= CheckVar10.get()
        marks = 4*(check2+check6+check7+check8)-1*(check1+check3+check4+check5+check9+check10)
        tkMessageBox.showinfo("Total Score","your score is "+str(marks))

    
    
    C1 = Checkbutton(frame, text = "cat", variable = CheckVar1, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C1.grid(row=0,column=0)
    C2 = Checkbutton(frame, text = "cow", variable = CheckVar2, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C2.grid(row=1,column=0)
    C3= Checkbutton(frame, text =  "lion", variable = CheckVar3,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C3.grid(row=2,column=0)
    C4= Checkbutton(frame, text=   "elephant", variable = CheckVar4,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C4.grid(row=3,column=0)
    C5= Checkbutton(frame, text=   "monkey", variable = CheckVar5,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C5.grid(row=4,column=0)
    C6 = Checkbutton(frame, text = "zebra", variable = CheckVar6, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C6.grid(row=5,column=0)
    C7 = Checkbutton(frame, text = "dog", variable = CheckVar7, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C7.grid(row=6,column=0)
    C8= Checkbutton(frame, text =  "tiger", variable = CheckVar8,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C8.grid(row=7,column=0)
    C9= Checkbutton(frame, text =  "deer", variable = CheckVar9,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C9.grid(row=8,column=0)
    C10= Checkbutton(frame, text = "goat", variable = CheckVar10,
         onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C10.grid(row=9,column=0)

    submitbutton= Button(frame, text="submit",fg="white",bg="red",
                 width=20, height=3,command=total,relief='raised')
    submitbutton.grid(row=5,column=1)
    frame.grid()
    frame.mainloop()



def submit2():
    submit=Toplevel(main)
    submit.minsize(1300,800)
    submit.title("NAME OF IMAGES")
    new_game.destroy()
    #frame.grid()
    frame=Frame(submit,width=1000,height=900)
   
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10= IntVar()

    def total():
        submit.destroy()
        check1=CheckVar1.get()
        check2= CheckVar2.get()
        check3= CheckVar3.get()
        check4= CheckVar4.get()
        check5= CheckVar5.get()
        check6= CheckVar6.get()
        check7= CheckVar7.get()
        check8= CheckVar8.get()
        check9= CheckVar9.get()
        check10= CheckVar10.get()
        marks = 4*(check1+check5+check9+check10)-1*(check2+check3+check4+check6+check7+check8)
        tkMessageBox.showinfo("Total Score","your score is "+str(marks))

    
    
    C1 = Checkbutton(frame, text = "cat", variable = CheckVar1, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C1.grid(row=0,column=0)
    C2 = Checkbutton(frame, text = "cow", variable = CheckVar2, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C2.grid(row=1,column=0)
    C3= Checkbutton(frame, text =  "lion", variable = CheckVar3,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C3.grid(row=2,column=0)
    C4= Checkbutton(frame, text=   "elephant", variable = CheckVar4,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C4.grid(row=3,column=0)
    C5= Checkbutton(frame, text=   "monkey", variable = CheckVar5,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C5.grid(row=4,column=0)
    C6 = Checkbutton(frame, text = "zebra", variable = CheckVar6, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C6.grid(row=5,column=0)
    C7 = Checkbutton(frame, text = "dog", variable = CheckVar7, 
         onvalue = 1, offvalue = 0, height=3, width = 20,relief='raised')
    C7.grid(row=6,column=0)
    C8= Checkbutton(frame, text =  "tiger", variable = CheckVar8,
        onvalue= 1, offvalue = 0, height=3, width = 20,relief='raised')
    C8.grid(row=7,column=0)
    C9= Checkbutton(frame, text =  "deer", variable = CheckVar9,
        onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C9.grid(row=8,column=0)
    C10= Checkbutton(frame, text = "goat", variable = CheckVar10,
         onvalue =1, offvalue = 0, height=3, width =20,relief='raised')
    C10.grid(row=9,column=0)

    submitbutton= Button(frame, text="submit",fg="white",bg="red",
                 width=20, height=3,command=total,relief='raised')
    submitbutton.grid(row=5,column=1)
    frame.grid()
    frame.mainloop()


                                #main
main = Tk()
main.title('Kids Learning Game')
main.minsize(700,500)
main.maxsize(700,500)
new= Button(main,text='NEW GAME',width=40,fg='white',height=3,bd=5,bg='black',command=newgame)
new.pack(side= TOP)
exits= Button(main,text='EXIT',width=40,bg='red',fg='white',height=3,bd=5,command=main.destroy)
exits.pack(side=BOTTOM)
c1 = Canvas(main,width=1000,height=900)
one=PhotoImage(file='covers.gif')
c1.create_image(900,0,anchor=NE,image=one)
c1.pack()
main.mainloop()
