

from tkinter import *
from tkinter.ttk import Combobox

master =Tk()

master.geometry("544x529+10+10")

master.title("PHARMACY MANAGEMENT SYSTEM")

m=PhotoImage(file="picture\drug.PNG")
mlabel = Label(master, image=m)
mlabel.place(x=0,y=0)

mframe = Frame(master,width=650,height=650)
mframe.place(x=900,y=80)
titlem = Label(mframe, text="Registration Form", font=("arial", 22,"bold"),fg="gold")
titlem.grid(row=1,column=2)

firstnamelabel = Label(mframe,text="FIRST NAME",font=("times new roman",12,"bold"),fg="grey20")
firstnamelabel.grid(row=2,column=1,pady=5,padx=5)
entryfirstname = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entryfirstname.grid(row=3,column=1)

lastnamelabel = Label(mframe,text="LAST NAME",font=("times new roman",12,"bold"),fg="grey20")
lastnamelabel.grid(row=2,column=2,padx=5,pady=5)
entrylastname = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entrylastname.grid(row=3,column=2)

contactlabel = Label(mframe,text="CONTACT",font=("times new roman",12,"bold"),fg="grey20")
contactlabel.grid(row=4,column=1,padx=5,pady=5)
entrycontact = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entrycontact.grid(row=5,column=1)

emaillabel = Label(mframe,text="EMAIL",font=("times new roman",12,"bold"),fg="grey20")
emaillabel.grid(row=4,column=2,padx=5,pady=5)
entryemail = Entry(mframe,font=("times new roman",12,"bold"),bg= "lightgrey")
entryemail.grid(row=5,column=2)
# # creating combo box
securitylabel = Label(mframe,text="SECURITY QUESTION",font=("times new roman",12,"bold"),fg="grey20")
securitylabel.grid(row=6,column=1,padx=5,pady=5)
comboquestion = Combobox(mframe,font=("times new roman",16,"bold"),state="readonly")
comboquestion["values"]=("SELECT","YOUR FIRST NAME","YOUR BESTFRIENDS NAME","YOUR BIRTH PLACE","YOUR HUBBY",
"YOUR HUSBANDS NAME")
comboquestion.grid(row=7,column=1)
comboquestion.current(0)

answerlabel = Label(mframe,text="ANSWER",font=("times new roman",12,"bold"),fg="grey20")
answerlabel.grid(row=6,column=2,padx=5,pady=5)
entryanswer = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entryanswer.grid(row=7,column=2)


passwordlabel = Label(mframe,text="PASSWORD",font=("times new roman",12,"bold"),fg="grey20")
passwordlabel.grid(row=8,column=1,padx=5,pady=5)
entrypassword = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entrypassword.grid(row=9,column=1)


confirmlabel = Label(mframe,text="CONFIRM PASSWORD",font=("times new roman",12,"bold"),fg="grey20")
confirmlabel.grid(row=8,column=2,padx=5,pady=5)
entryconfirm = Entry(mframe,font=("times new roman",12,"bold"),bg="lightgrey")
entryconfirm.grid(row=9,column=2)

# Checkbutton= Checkbutton(mframe,text="I Agree  To ALL terms And CONDITIONS",onvalue=1,offvalue=0,
# font=("times new roman",12,"bold"))
# Checkbutton.grid(row=10,column=1)

# registerbutton =Button (mframe,text= "SIGNIN",pady=50,bd=0,font=("times new roman",12,"bold"),cursor="hand2")
# registerbutton.place(x=10,y=500)

# loginbutton =Button (mframe,text= "LOGIN",pady=50,bd=0,font=("times new roman",12,"bold"),cursor="hand2")
# loginbutton.place(x=10,y= 500)


# loginimg = PhotoImage(file="l.png")
# loginbutton =Button (master,image=loginimg,pady=50,bd=0,cursor="hand2")
# loginbutton.place(x=240,y=330)
    

master.mainloop()