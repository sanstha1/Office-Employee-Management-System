Call me here


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import customtkinter
import bcrypt
import pymysql
import ast
root = Tk()

def clear():
    username.delete(0,END)
    password.delete(0,END)


def signup_page():
    root.destroy()
    import signup

def database4_page():
    root.destroy()
    import database4

root.iconbitmap(r'melody.ico')

root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='logo.png')
Label(root,image=img,bg='white').place(x=40,y=30)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=90)

heading=Label(frame,text='LOG IN',fg='black',bg='white',font=('roboto',23,'bold'))
heading.place(x=115,y=5)
#################---------------------------------------------------------------------------------

def login_user():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('Error','All fields must be filled')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='santosh')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username.get(),password.get()))  
        row=mycursor.fetchone()
        if row is not None:
            messagebox.showinfo('Welcome','Login is successful')
            root.destroy()
            import database4
        else:
            messagebox.showerror('Error','Invalid username or password')
        



#################-----------------------------------------------------------
def hide():
    show_eye.config(file='hide.png')
    password.config(show='*')
    eye_button.config(command=show)
def show():
    show_eye.config(file='show.png')
    password.config(show='')
    eye_button.config(command=hide)

#################-------------------------------------------------------------

def on_enter(e):
    username.delete(0,'end')

def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'Username')

username = Entry(frame,width=35,fg='black',border=0,bg="White",font=('roboto',11))
username.place(x=30,y=80)

username.insert(0,'Username')

username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

Frame(frame,width=294,height=2,bg='Black').place(x=25,y=107)

#################---------------------------------------------------------------

def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')

password = Entry(frame,width=35,fg='black',border=0,bg="White",font=('roboto',11))
password.place(x=30,y=150)

password.insert(0,'Password')

password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=294,height=2,bg='Black').place(x=25,y=177)

#######################-------------------------------------------------------------------------------------

show_eye=PhotoImage(file='show.png')
eye_button=Button(root,image=show_eye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eye_button.place(x=775,y=240)


#########################---------------------------------------------------------------------------------
button=Button(frame,width=40,pady=7,text='Log in',bg='#3776ab',fg='White',border=0,command=login_user)
button.place(x=32,y=210)
label=Label(frame,text="Don't have an account?",fg='black',bg='White',font=('roboto',10))
label.place(x=75,y=270)
#########################--------------------------------------------------------------------------------------

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#3776ab',command=signup_page)    
sign_up.place(x=215,y=270)



root.mainloop()