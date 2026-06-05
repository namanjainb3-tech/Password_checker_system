from tkinter import *
uc =0
lc=0
ch=0
l=0
dig=0
def validate(st):
    global uc,lc,dig,ch,l
    l=len(st)
    if l<8:
        return "Please enter atleast 8 characters!"
        exit()

    for i in st:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            dig+=1
        else:
            ch+=1
    
    if uc==0:
        return "Enter atleast one Upper Case character"
    if lc==0:
        return "Enter atleast one Lower Case character"
    if ch==0:
        return "Enter atleast one special character"
    if dig==0:
        return "Enter atleast one digit"
    
    if uc>0 and lc>0 and dig>0 and ch>0 :
        return "Password accepted!"

def strength():
    global uc,lc,ch,dig
    a=0
    if uc>0:
        a+=1
    if lc>0:
        a+=1
    if dig>0:
        a+=1
    if ch>0:
        a+=1


    match a:
        case 4:
            return "Very strong"
        case 1:
            return "Poor"
        case _:
            return "Intermediate"



def check():

    new_win=Toplevel()
    new_win.geometry("400x400")

    new_win.config(bg='#E8E8E8')
    new_win.resizable(False,False)

    head3=Label(new_win,text="Enter your password!",font=("Ariel",14))
    head3.place(x=110,y=50)

    pwd_var = StringVar()
    password = Entry(new_win,textvariable=pwd_var)
    password.place(x=140,y=105)

    result_label = Label(new_win, text="", font=("Ariel", 12), fg="blue")
    result_label.place(x=100, y=150)

    strength_label = Label(new_win, text="", font=("Ariel", 12), fg="green")
    strength_label.place(x=100, y=200)
    
    def on_submit():
        msg = validate(pwd_var.get())
        result_label.config(text=msg)
        if l>=8:
            strength_label.config(text="Strength: " + strength())
    password.bind("<Return>", lambda event: on_submit())



win=Tk()
win.title("Password Checker")
win.geometry("700x400")

win.config(bg='#FFECA1')
win.resizable(False,False)

head=Label(win,text="WELCOME TO PASSWORD SECURITY CHECKER!",font=(20),relief="solid")
head.place(x=100,y=15)

ins='''A strong password must satisfy the following conditions:
1> It must contain atleast 8 characters.
2> It must contain both upper case and lower case characters.
3> It must contain atleast one special character.
4> It must also have atleast one digit in it.'''
head2=Label(win,text=ins,font=(15),relief="ridge")
head2.place(x=60,y=60)

button1 = Button(win,text="Proceed to check",command=check)
button1.place(x=300,y=250)
win.mainloop()