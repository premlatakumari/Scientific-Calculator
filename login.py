from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
ton=mysql.connector.connect(host="localhost",
                       user="root",
                       passwd="Sa@loni99", database="loggin")
curs=ton.cursor()
#cursor.execute("create database loggin")
#cursor.execute("create table signin (username varchar(255), password varchar(255))")
from tkinter import messagebox
class loogin:
    def __init__(self,root):
        self.root=root
        self.root.geometry('900x600+200+100')
        self.filename=ImageTk.PhotoImage(Image.open("cal.jpg"))
        self.background_label=Label( self.root,image=self.filename).place(x=0, y=0)
       
        self.root.title("login system")
        self.root.resizable(False,False)
        
       
        
        def register():
            self.root.destroy()
            import registration
            
    
    #Login Frame#
        
        Frame_login=Frame(self.root, bg="white")
       
        Frame_login.place(x=180,y=115,height=340,width=500)
    
        title=Label(Frame_login,text='Login Here',font=('Impact',35,'bold'),fg='#d72631',bg='white')
        title.place(x=90,y=30)
        title2=Label(Frame_login,text='Simplify your Calculation with us...',font=('Times',12,'bold'),fg='#d72631',bg='white')
        title2.place(x=90,y=100)

        
        lb1=Label(Frame_login,text='Email Id:',font=('Goudy old style',15,'bold'),fg='#e75874',bg='white')
        lb1.place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lb2=Label(Frame_login,text='Password:',font=('Goudy old style',15,'bold'),fg='#e75874',bg='white')
        lb2.place(x=90,y=210)
        self.txt_password=Entry(Frame_login, show="*", font=("times new roman",15),bg='lightgray')
        self.txt_password.place(x=90,y=240,width=350,height=35)
        
        register_button=Button(Frame_login,text=' Not Registered? Register here',bg='white',command=register,fg='#e75874',bd=0,cursor='hand2',font=('times new roman',14)).place(x=140,y=280)
        
        login_button=Button(self.root,text='Login',command=self.login1,cursor='hand2',width=10, height=1,bg="#d72631", fg="white",font=('times new roman',20)).place(x=350,y=430)
       
    
    def login1(self):
        if self.txt_password.get()=="" or self.txt_user.get()=='':
            messagebox.showerror("Login Error",'All fields are required',parent=self.root)
        else:

            try:
                curs.execute("select * from signin where username= %s AND password = %s",(self.txt_user.get(), self.txt_password.get()))
                row=curs.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid username or password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Welcome", "WELCOME",parent=self.root)
                    self.root.destroy()
                    import interface
            except Exception as es:
                messagebox.showerror("Error", "Authentication Failed!!!", parent=self.root)
            
root=Tk()
obj=loogin(root)
root.mainloop()
