import customtkinter
import pymysql
import bcrypt
from tkinter import*
from tkinter import messagebox
import ast


def clear():
    email.delete(0,END)
    fullname.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    confirm_password.delete(0,END)


window=Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)
#-------------#----------------------------------------------------------------------------------------------------------------
def connect_database():
    if email.get()==''or fullname.get()==''or username.get()==''or password.get()=='' or confirm_password.get()=='':
        messagebox.showerror('Error','All fields must be filled')
    elif password.get() != confirm_password.get():
        messagebox.showerror('Error','Password mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='santosh') 
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), fullname varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(username.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username already exists')

        else:
             query='insert into data(email,fullname,username,password) values(%s,%s,%s,%s)'
             mycursor.execute(query,(email.get(),fullname.get(),username.get(),password.get()))
             con.commit()
             con.close()
             messagebox.showinfo('Success','Signed up')
             clear()
             window.destroy()
             import signin
     
#######-----------------------------------------------------------------------------------------------------------------------------
def login_page():
    window.destroy()
    import signin

#########-----------------------------------------------------------------------------------------------------------------------------------


window.iconbitmap(r'melody.ico')

img=PhotoImage(file='logo.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=50)

frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=500,y=50)

heading=Label(frame,text='Sign Up',fg="Black",bg='white',font=('roboto',23,'bold'))
heading.place(x=110,y=2)
############--------------------------------------------------------------------------------------

def on_enter(e):
    email.delete(0,'end')

def on_leave(e):
    if email.get()=='':
        email.insert(0,'Email')

email=Entry(frame,width=35,fg='black',border=0,bg='white',font=('roboto',11))
email.place(x=30,y=60)
email.insert(0,'Email')
email.bind("<FocusIn>",on_enter)
email.bind("<FocusOut>",on_leave)

Frame(frame,width=290,height=2,bg='black').place(x=30,y=80)
##########----------------------------------------------------------------------------------------------


def on_enter(e):
    fullname.delete(0,'end')

def on_leave(e):
    if fullname.get()=='':
        fullname.insert(0,'Fullname')

fullname=Entry(frame,width=35,fg='black',border=0,bg='white',font=('roboto',11))
fullname.place(x=30,y=100)
fullname.insert(0,'Fullname')
fullname.bind("<FocusIn>",on_enter)
fullname.bind("<FocusOut>",on_leave)
Frame(frame,width=290,height=2,bg='black').place(x=30,y=120)
##########----------------------------------------------------------------------------------------------

def on_enter(e):
    username.delete(0,'end')

def on_leave(e):
    if username.get()=='':
        username.insert(0,'Username')

username=Entry(frame,width=35,fg='black',border=0,bg='white',font=('roboto',11))
username.place(x=30,y=140)
username.insert(0,'Username')
username.bind("<FocusIn>",on_enter)
username.bind("<FocusOut>",on_leave)
Frame(frame,width=290,height=2,bg='black').place(x=30,y=160)
##########----------------------------------------------------------------------------------------------

def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    if password.get()=='':
        password.insert(0,'Password')

password=Entry(frame,width=35,fg='black',border=0,bg='white',font=('roboto',11))
password.place(x=30,y=180)
password.insert(0,'Password')
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
Frame(frame,width=290,height=2,bg='black').place(x=30,y=200)
#############-----------------------------------------------------------------------------------------------------

def on_enter(e):
    confirm_password.delete(0,'end')

def on_leave(e):
    if confirm_password.get()=='':
        confirm_password.insert(0,'Confirm Password')

confirm_password=Entry(frame,width=35,fg='black',border=0,bg='white',font=('roboto',11))
confirm_password.place(x=30,y=220)
confirm_password.insert(0,'Confirm Password')
confirm_password.bind("<FocusIn>",on_enter)
confirm_password.bind("<FocusOut>",on_leave)
Frame(frame,width=290,height=2,bg='black').place(x=30,y=240)
############------------------------------------------------------------------------------------------------------

def hide():
    show_eye.config(file='hide.png')
    password.config(show='*')
    eye_button.config(command=show)
def show():
    show_eye.config(file='show.png')
    password.config(show='')
    eye_button.config(command=hide)

show_eye=PhotoImage(file='show.png')
eye_button=Button(window,image=show_eye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eye_button.place(x=800,y=230)


def close():
    open_eye.config(file='hide.png')
    confirm_password.config(show='*')
    eyes_button.config(command=open)
def open():
    open_eye.config(file='show.png')
    confirm_password.config(show='')
    eyes_button.config(command=close)

open_eye=PhotoImage(file='show.png')
eyes_button=Button(window,image=open_eye,bd=0,bg='white',activebackground='white',cursor='hand2',command=close)
eyes_button.place(x=800,y=270)



#############------------------------------------------------------------------------------------------------------
button=Button(frame,width=39,pady=5,text='Sign up',bg='#3776ab',fg='White',border=0,command=connect_database)
button.place(x=36,y=280)

Label=Label(frame,text='Already have an account ?',fg='black',bg='white',font=('roboto',9))
Label.place(x=85,y=340)

signin=Button(frame,width=6,text='Log In',border=0,bg='white',cursor='hand2',fg='#3776ab',command=login_page)
signin.place(x=230,y=340)


window.mainloop()