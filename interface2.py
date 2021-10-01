from tkinter import *
import math
import parser
import tkinter.messagebox

root=Tk()
root.geometry("560x550+400+200")
root.configure(background="gray26")
root.resizable(width=False, height=False)
root.title("Scientific Calculator")


######################################  OPTIONS ON CALCULATOR  ########################################################
def exit():
    iexit=tkinter.messagebox.askyesno("Exit","Do you want to exit from Calculator?")
    if iexit>0:
        root.destroy()
        return

def standard():
     root.destroy()
     import interface
   


###########################################  BUTTONS ON CALCULATOR ###################################################
calc=Frame(root).grid(row=0, column=0)
txtdis=Entry(calc, font=('arial',20,'bold'), bg="gray15", fg="white", width=33, bd=30, justify=RIGHT)
txtdis.grid(row=0, column=0, columnspan=8)
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
        
             
    def pi(self):
        self.result=False
        self.curr=math.pi
        self.display(self.curr)
    def tau(self):
        self.result=False
        self.curr=math.tau
        self.display(self.curr)
        
    def e(self):
        self.result=False
        self.curr=math.e
        self.display(self.curr)
    
    def square(self):
        self.result=False
        self.curr=math.sqrt(float(txtdis.get()))
        self.display(self.curr)
        
    def cos(self):
        self.result=False
        self.curr=math.cos(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def cosh(self):
        self.result=False
        self.curr=math.cosh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def acosh(self):
        self.result=False
        self.curr=math.acosh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def asinh(self):
        self.result=False
        self.curr=math.asinh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def tanh(self):
        self.result=False
        self.curr=math.tanh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def tan(self):
        self.result=False
        self.curr=math.tan(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def sinh(self):
        self.result=False
        self.curr=math.sinh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def sin(self):
        self.result=False
        self.curr=math.sin(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def log(self):
        self.result=False
        self.curr=math.log(math.radians(float(txtdis.get())))
        self.display(self.curr)

   
        
    def exp(self):
        self.result=False
        self.curr=math.exp(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def lgamma(self):
        self.result=False
        self.curr=math.lgamma(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def atanh(self):
        self.result=False
        self.curr=math.atanh(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def log10(self):
        self.result=False
        self.curr=math.log10(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def log1p(self):
        self.result=False
        self.curr=math.log2(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
    def expm1(self):
        self.result=False
        self.curr=math.expm1(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
        
    def degrees(self):
        self.result=False
        self.curr=math.degrees(math.radians(float(txtdis.get())))
        self.display(self.curr)
        
        
    def admi(self):
        self.result=False
        self.curr=-(float(txtdis.get()))
        self.display(self.curr)
         
        
    def display(self,value):
        txtdis.delete(0,END)
        txtdis.insert(0,value)
        
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

pie = Button(calc,height =2,width=4,padx=10, pady = 10, text = "π",bg="orange", command=lambda:added_val.pi()).grid(row = 1, column = 4,  padx=1, pady = 1)
cos = Button(calc,height =2,width=4,padx=10, pady = 10, text = "cos",bg="orange",command=lambda:added_val.cos() ).grid(row = 1, column = 5,  padx=1, pady = 1)
tan = Button(calc,height =2,width=4,padx=10, pady = 10, text = "tan",bg="orange",command=lambda:added_val.tan()).grid(row = 1, column = 6,  padx=1, pady = 1)
sin = Button(calc,height =2,width=4,padx=10, pady = 10, text = "sin",bg="orange",command=lambda:added_val.sin()).grid(row = 1, column = 7,  padx=1, pady = 1)
πt= Button(calc,height =2,width=4,padx=10, pady = 10, text = "2π",bg="orange",command=lambda:added_val.tau()).grid(row = 2, column = 4,  padx=1, pady = 1)
cosh = Button(calc,height =2,width=4,padx=10, pady = 10, text = "cosh",bg="khaki1",command=lambda:added_val.cosh()).grid(row = 2, column = 5,  padx=1, pady = 1)
tanh = Button(calc,height =2,width=4,padx=10, pady = 10, text = "tanh",bg="khaki1",command=lambda:added_val.tanh()).grid(row = 2, column = 6,  padx=1, pady = 1)
sinh = Button(calc,height =2,width=4,padx=10, pady = 10, text = "sinh",bg="khaki1",command=lambda:added_val.sinh()).grid(row = 4, column = 5,  padx=1, pady = 1)
log = Button(calc,height =2,width=4,padx=10, pady = 10, text = "log",bg="orange",command=lambda:added_val.log()).grid(row = 3, column = 4,  padx=1, pady = 1)
Exp = Button(calc,height =2,width=4,padx=10, pady = 10, text = "Exp",bg="orange",command=lambda:added_val.exp()).grid(row = 4, column = 4,  padx=1, pady = 1)
Mod = Button(calc,height =2,width=4,padx=10, pady = 10, text = "Mod",bg="orange",command=lambda:added_val.operation("mod")).grid(row = 4, column = 7,  padx=1, pady = 1)
e = Button(calc,height =2,width=4,padx=10, pady = 10, text = "e",bg="orange", command=added_val.e).grid(row = 3, column = 7,  padx=1, pady = 1)
atanh= Button(calc,height =2,width=4,padx=10, pady = 10, text = "atanh",bg="khaki1",command=lambda:added_val.atanh()).grid(row = 4, column = 6,  padx=1, pady = 1)
deg = Button(calc,height =2,width=4,padx=10, pady = 10, text = "deg",bg="orange",command=lambda:added_val.degrees()).grid(row = 2, column = 7,  padx=1, pady = 1)
acosh = Button(calc,height =2,width=4,padx=10, pady = 10, text = "acosh",bg="khaki1",command=lambda:added_val.acosh()).grid(row = 3, column = 5,  padx=1, pady = 1)
asinh = Button(calc,height =2,width=4,padx=10, pady = 10, text = "asinh",bg="khaki1",command=lambda:added_val.asinh()).grid(row = 3, column = 6,  padx=1, pady = 1)
log10 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "log10",bg="orange",command=lambda:added_val.log10()).grid(row = 5, column = 4,  padx=1, pady = 1)
log1p = Button(calc,height =2,width=4,padx=10, pady = 10, text = "log1p",bg="orange",command=lambda:added_val.log1p()).grid(row = 5, column = 5,  padx=1, pady = 1)
expm1 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "expm1",bg="orange",command=lambda:added_val.expm1()).grid(row = 5, column = 6,  padx=1, pady = 1)
lgamma= Button(calc,height =2,width=4,padx=10, pady = 10, text = "lgamma",bg="orange",command=lambda:added_val.lgamma()).grid(row = 5, column = 7,  padx=1, pady = 1)
btn=Button(root, text="Exit", height=2,pady=5,padx=5,width=10 ,command=exit,bg="goldenrod2").grid(row=7, column=0 , columnspan=3,pady=50)
btn1=Button(root, text="Scientific",height=2,pady=5,padx=5,width=10,bg="goldenrod2").grid(row=7, column=3, columnspan=3)
btn2=Button(root, text="Standard",height=2,pady=5,padx=5, width=10,command=standard,bg="goldenrod2").grid(row=7, column=6,columnspan=3)






    


root.mainloop()