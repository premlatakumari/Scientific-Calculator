from tkinter import *
import math
import parser
import tkinter.messagebox
import mysql.connector

#cur.execute("create table history1 (operand1 int, operator varchar(10), operand2 int, result int)")

root=Tk()
root.geometry("407x568+500+150")
root.configure(background="gray26")
root.resizable(width=False, height=False)
root.title("Scientific Calculator")


######################################  OPTIONS ON CALCULATOR  ########################################################
def exit():
    iexit=tkinter.messagebox.askyesno("Exit","Do you want to exit from Calculator?")
    if iexit>0:
        root.destroy()
        return
def scientific():
     root.destroy()
     import interface2
   
###########################################  BUTTONS ON CALCULATOR ###################################################
calc=Frame(root).grid(row=0, column=0)
txtdis=Entry(calc, font=('arial',20,'bold'), bg="gray15", fg="white", width=23, bd=30, justify=RIGHT)
txtdis.grid(row=0, column=0, columnspan=4)
txtdis.insert(0,"0")
####################################### FUNCTIONALITY OF BUTTON  ##################################################
class calculate():
    def __init__(self):
        self.total=0
        self.curr=""
        self.inputval=True
        self.checksum=False
        self.op=""
        self.result=False
        
    def numentry(self,number):
        self.result=False
        numone=txtdis.get()
        numtwo=str(number)
        if self.inputval:
            self.curr=numtwo
            self.inputval=False
        else:
            if numtwo=='.':
                if numtwo in numone:
                    return
            self.curr=numone+numtwo
        self.display(self.curr)
        
    def sumtotal(self):
        self.result=True
        self.curr=float(self.curr)
        if self.checksum==True:
            self.valid()
        else:
            self.total=float(txtdis.get())
            
            
    def valid(self):
        if self.op=="add":
            self.total+=self.curr
        if self.op=="sub":
            self.total-=self.curr
        if self.op=="multi":
            self.total*=self.curr
        if self.op=="div":
            self.total/=self.curr
        if self.op=="mod":
            self.total%=self.curr
        self.inputval=True
        self.checksum=False
        self.display(self.total)
    def operation(self,op):
        self.curr=float(self.curr)
        if self.checksum==True:
            self.valid()
        elif not self.result:
            self.total=self.curr
            self.inputval=True
        self.checksum=True
        self.op=op
        self.result=False
        
             
    
        
    def admi(self):
        self.result=False
        self.curr=-(float(txtdis.get()))
        self.display(self.curr)
         
        
    def display(self,value):
        txtdis.delete(0,END)
        txtdis.insert(0,value)

    def square(self):
        self.result=False
        self.curr=math.sqrt(float(txtdis.get()))
        self.display(self.curr)
        
    def clear(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.inputval=True
        
    def clearall(self):
        self.clear()
        self.total=0
                        
added_val=calculate()
numbers = "789456123"
i = 0
bttn = []
for j in range(2,5):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=6,bd=4,text = numbers[i]))
        bttn[i]["bg"]= "snow2"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"]=lambda x=numbers[i]:added_val.numentry(x)
        i += 1
clear = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = "⌫",bg="red3",command=added_val.clear).grid(row = 1, column = 0,  padx=1, pady = 1)
clearall = Button(calc,height =2,width=4,padx=10, pady = 10,bd=4, text = "AC",bg="red3",command=added_val.clearall).grid(row = 1, column = 1,  padx=1, pady = 1)
bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4,text = "0",bg="snow2", command=lambda:added_val.numentry(0)).grid(row = 5, column = 0,  padx=1, pady = 1)
div = Button(calc,height =2,width=4,padx=10, pady = 10,  bd=4,text = "/",bg="snow2",command=lambda:added_val.operation("div")).grid(row = 3, column = 3,  padx=1, pady = 1)
mult = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = "X",bg="snow2",command=lambda:added_val.operation("multi")).grid(row = 4, column = 3,  padx=1, pady = 1)
add = Button(calc,height =2,width=4,padx=10, pady = 10,  bd=4,text = "+",bg="snow2",command=lambda:added_val.operation("add")).grid(row = 1, column = 3,  padx=1, pady = 1)
sub = Button(calc,height =2,width=4,padx=10, pady = 10,bd=4, text = "-",bg="snow2",command=lambda:added_val.operation("sub")).grid(row = 2, column = 3,  padx=1, pady = 1)
sqrt = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = "√",bg="snow2",command=lambda:added_val.square()).grid(row = 1, column = 2,  padx=1, pady = 1)
dec = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = ".",bg="snow2", command=lambda:added_val.numentry(".")).grid(row = 5, column = 1,  padx=1, pady = 1)
equals = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = "=",bg="red4",command=added_val.sumtotal).grid(row = 5, column = 3,  padx=1, pady = 1)
admi = Button(calc,height =2,width=4,padx=10, pady = 10, bd=4, text = "±",bg="snow2",command=lambda:added_val.admi()).grid(row = 5, column = 2,  padx=1, pady = 1)


btn=Button(root, text="Exit", height=2,pady=5,padx=5,width=10 ,command=exit,bg="goldenrod2").grid(row=7, column=0 , pady=50)
btn1=Button(root, text="Scientific",height=2,pady=5,padx=5,width=10,command=scientific,bg="goldenrod2").grid(row=7, column=1)
btn2=Button(root, text="Standard",height=2,pady=5,padx=5, width=10,bg="goldenrod2").grid(row=7, column=2, columnspan=1)






    


root.mainloop()
