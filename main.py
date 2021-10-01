from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("700x400")
root.title("JOIN US!!!")
root.resizable(False,False)
root.geometry('700x400+400+100')
filename=ImageTk.PhotoImage(Image.open("main.jpg"))
background_label=Label(root, image=filename).place(x=0, y=0)


def login():
    root.destroy()
    import login
def signup():
    root.destroy()
    import registration
h2=Label(root, text="SCIENTIFIC CALCULATOR", font=("Times New Roman (Times)", 20), bg="goldenrod2", fg="black").place(x=200,y=25)
h1=Label(root, text="Be a part of us to make the most of what we serve!!!",font=("Times", 17), width=60, bg="steelblue", fg="white").place(x=5,y=100)
text = Text(root, width=87, height=5,font=("Verdana", 10), bg="cadetblue", fg="aliceblue")
text.place(x=0, y=150)

text.insert(INSERT, "We always keep trying to serve best to our customers. In order to ensure that you don't miss out with any of our features, we would suggest you to REGISTER yourself with us.If you are already a satisfied registered user please click on LOGIN to continue")
text.place(x=0, y=150)
bt=Button(root, text="LOGIN", command=login, cursor='hand2', width=10, height=3, bg="black", fg="white").place(x=200, y=250)
bt1=Button(root, text="REGISTER", command=signup,cursor='hand2', width=10, height=3, bg="black", fg="white").place(x=400,y=250) 
root.mainloop()