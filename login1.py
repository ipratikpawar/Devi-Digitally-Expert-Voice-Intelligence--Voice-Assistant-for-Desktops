from tkinter import *
import tkinter.messagebox
import os
import mysql.connector
import subprocess
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="logindb"
)
def run():
    os.system('python main.py') 
def login():  
	global root2
	root2 = Toplevel(root4)
	root2.title("Account Login for DEVI")
	root2.geometry("400x300")
	root2.config(bg="white")
	global username_verification
	global password_verification
	Label(root2, text='Please Enter your Account Details', bd=5,relief="groove", font=('arial', 12, 'bold'), fg="white",
	bg="purple",width=300).pack()
	username_verification = StringVar()
	password_verification = StringVar()
	Label(root2, text="").pack()
	Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root2, textvariable=username_verification).pack()
	Label(root2, text="").pack()
	Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root2, textvariable=password_verification, show="*").pack()
	Label(root2, text="").pack()
	Button(root2, text="Login", bg="purple", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
	Label(root2, text="")
def register():
	global root3
	root3 = Toplevel(root4)
	root3.title("Account register for DEVI")
	root3.geometry("500x500")
	root3.config(bg="white")
	global username_reg
	global password_reg
	global phone_reg
	global email_reg
	Label(root3, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
	bg="purple",width=500).pack()
	username_reg = StringVar()
	password_reg = StringVar()
	phone_reg = StringVar()
	email_reg = StringVar()
	Label(root3, text="").pack()
	Label(root3, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=username_reg).pack()
	Label(root3, text="").pack()
	Label(root3, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=password_reg, show="*").pack()
	Label(root3, text="").pack()
	Label(root3, text="phone no :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=phone_reg).pack()
	Label(root3, text="").pack()
	Label(root3, text="Email id :", fg="black", font=('arial', 12, 'bold')).pack()
	Entry(root3, textvariable=email_reg).pack()
	Label(root3, text="").pack()
	Button(root3, text="Register", bg="purple", fg='white', relief="groove", font=('arial', 12, 'bold'),command=reg_verification).pack()
	Label(root3, text="") 
def logged_destroy():
	logged_message.destroy()
	root2.destroy()
def failed_destroy():
	failed_message.destroy()
def logged():
	global logged_message
	logged_message = Toplevel(root2)
	logged_message.title("Welcome")
	logged_message.geometry("500x100")
	Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
	Button(logged_message, text="Exit", bg="purple", fg='white', relief="groove", font=('arial', 12, 'bold'), command=run).pack()
	
def failed():
	global failed_message
	failed_message = Toplevel(root2)
	failed_message.title("Invalid Message")
	failed_message.geometry("500x100")
	Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
	Label(failed_message, text="").pack()
	Button(failed_message,text="Ok", bg="purple", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()
 
def login_verification():
    user_verification =username_verification.get()
    pass_verification= password_verification.get()
    if(user_verification == "" or pass_verification == ""):
            print("Oops!","Your information can't be empty!")
            return
    mycursor = mydb.cursor()
    sql = "select username, password from usertable where username=%s and password=%s"
    val = (user_verification,pass_verification)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        logged()
    else:
        failed()
def reg_verification():
	user_verification = username_reg.get()
	pass_verification = password_reg.get()
	phone_verification = phone_reg.get()
	email_verification=email_reg.get()
	mycursor = mydb.cursor()
	sql = "INSERT INTO usertable(username, password, phone, email) VALUES (%s, %s, %s, %s)"
	val = (user_verification, pass_verification, phone_verification, email_verification)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")    
	root3.destroy() 
def mainS():
    global root4
    root4 =Tk()
    root4.config(bg="white")
    root4.title("DEVI Login Page ")
    root4.geometry("400x278")
    Label(root4,text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",bg="purple",width=300).pack()
    Label(root4,text="").pack()
    Button(root4,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="purple",command=login).pack()
    Label(root4,text="").pack()
    Button(root4,text='Register', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="purple",command=register).pack()
    Label(root4,text="").pack()
    Button(root4,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",bg="purple",command=exit).pack()
    Label(root4,text="").pack()
mainS()
root4.mainloop()
def exit():
    root4.destroy()
    exit()