from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("SCIENTIFIC CALCULATOR")
        self.root.geometry("1000x700+250+60")
        self.filename1=ImageTk.PhotoImage(Image.open("pic.jpg"))
        self.background_label1=Label( self.root,image=self.filename1).place(x=0, y=0)
       
        
        
        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=100,y=100,width=800,height=500)
        
        title=Label(frame1,text="SCIENTIFIC CALCULATOR REGISTRATION",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=90,y=30)
        #label and entry for first name
        f_name=Label(frame1,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15), bg="aliceblue")
        self.txt_fname.place(x=50,y=130,width=250)
        #label and entry for last name
        l_name=Label(frame1,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="aliceblue")
        self.txt_lname.place(x=370,y=130,width=250)
       
        #label and entry for email
        email=Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=370,y=170)
        self.txt_email1=Entry(frame1,font=("times new roman",15),bg="aliceblue")
        self.txt_email1.place(x=370,y=200,width=250)
        #labe and combobox for security question
        
       
        password=Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=170)
        self.txt_password1=Entry(frame1,font=("times new roman",15),show="*",bg="aliceblue")
        self.txt_password1.place(x=50,y=200,width=250)
        #label and entry for confirm password
        cpassword=Label(frame1,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=260,y=250)
        self.txt_cpassword1=Entry(frame1,font=("times new roman",15),show="*",bg="aliceblue")
        self.txt_cpassword1.place(x=260,y=280,width=250)
        #creating a check button for terms and conditions
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms&Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",fg="black",font=("times new roman",14)).place(x=50,y=380)
        #creating an image as button
        #self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,bd=0,cursor="hand2",text="SIGN IN",command=self.login_window, font=("times new roman",16),bg="white", fg="black").place(x=50,y=420)
        #creating button for signin
        btn_login=Button(self.root,text="REGISTER",command=self.register_data,font=("times new roman",20),bd=0,cursor="hand2",bg="black", fg="aliceblue").place(x=450,y=535)
        #cursor=hand2 means to change the structure of cursor when we touched the button
        
        
    def login_window(self):
        self.root.destroy()
        import login
         #importing whole program file from loginpage.py
        
    
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email1.get()=="" or self.txt_password1.get()=="" or self.txt_cpassword1.get()=="" or self.var_chk.get()==0:
            messagebox.showerror("ERROR","All Fields are Required",parent=self.root) 
        elif self.txt_password1.get()!=self.txt_cpassword1.get():
            messagebox.showerror("ERROR","Password and Confirm Password must be same",parent=self.root)
        
        else:
            con=mysql.connector.connect(host="localhost",user="root",passwd="Sa@loni99",database="loggin")
            cursor=con.cursor()
            sql=("insert into signin(username, password) values (%s,%s)")
            val=(self.txt_email1.get(),self.txt_password1.get())
            cursor.execute(sql,val)
            con.commit()
            messagebox.showinfo("Register","Registered Successfully",parent=self.root)#connecting to database
                              
                              
                              
                              
                              
                              
                             
root=Tk()
obj=Register(root)
root.mainloop()