
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import register




register.





class Login_window:
    def __init__(self,master):
        self.master= master
        self.master.title("LOGIN")
        self.master.geometry("1550x800")


        self.bg=ImageTk.PhotoImage(file="picture/pot.png")
        lbl_bg=Label(self.master,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        mframe = Frame(self.master,bg="white")
        mframe.place(x=500, y=95, width=340, height=450)


        img1 = Image.open(r"C:\Users\User\Desktop\python\project\picture\download.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1= ImageTk.PhotoImage(img1)
        labelimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        labelimg1.place(x=625,y=100, width=100, height=100) 
        getstring= Label(mframe, text="GET STARTED",font=("arial",20,"bold"),fg="green",bg='white')
        getstring.place(x=80,y=110)

        # lABEL

        username = Label(mframe, text="Username", font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=40, y=155)
        self.entryuser = Entry(mframe, font=("times new roman",15),bd=3,fg="grey")
        self.entryuser.place(x=40, y=180, width=270)
        

        
        password = Label(mframe, text="Password", font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=40, y=225)
        self.txtpass = Entry(mframe, font=("times new roman",15),bd=3,fg="grey",show="*")
        self.txtpass.place(x=40, y=250, width=270)
        
    

        img2 = Image.open(r"C:\Users\User\Desktop\python\project\picture\user.png")
        img2=img2.resize((45,45),Image.ANTIALIAS)
        self.photoimage2= ImageTk.PhotoImage(img2)
        labelimg1 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        labelimg1.place(x=512,y=280, width=25, height=25) 

        
        img3 = Image.open(r"C:\Users\User\Desktop\python\project\picture\padd.png")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3= ImageTk.PhotoImage(img3)
        labelimg1 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        labelimg1.place(x=512,y=350, width=25, height=25) 

        #  login button
        loginbtn =Button(mframe,command=self.login, text="LOGIN",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="white",bg='green',activeforeground="white",activebackground="green",cursor="hand2")
        loginbtn.place(x=110,y=300, width=100,height=50)


        # registerbutton
        registerbutton =Button(mframe, text="New User Register",command=Register,font=("times new roman",10,"bold"),padx=5,pady=5,borderwidth=0,fg="white",bg="green",activeforeground="white",activebackground="green",cursor="hand2")
        registerbutton.place(x=30,y=400, width=120)


        # forgetpasswordbutton
        registerbutton =Button(mframe, text="Forgot Password",font=("times new roman",10,"bold"),padx=5,pady=5,borderwidth=0,fg="white",bg="green",activeforeground="white",activebackground="green",cursor="hand2")
        registerbutton.place(x=205,y=400, width=120)

    def login(self):
        if self.entryuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        if self.entryuser.get()!= "anny"and self.txtpass.get()=="2590":
            messagebox.showerror("Invalid","Invalid username")
        if self.txtpass.get()!="2590"and self.entryuser.get()=="anny":
            messagebox.showerror("Invalid","Input the correct password")
        
        elif self.entryuser.get()=="anny" and self.txtpass.get()=="2590":
         messagebox.showinfo("Success","Welcome to Ani pharmaceutical limited")
          
         master.destroy()
         top = Tk()
         top.configure(bg="white")
         master.title("DASHBOARD")
         label = Label(top,text="WELCOME TO THE DASHBOARD!",font=("Areal",30))
         label.place(x=1400,y=500)

        elif self.entryuser.get()!="anny" and self.txtpass.get()!="2590":
         messagebox.showerror("Invalid","Invalid username and password")
          

         



    


        


    
if __name__== "__main__":
    master=Tk()
    form =Login_window(master)
    master.mainloop()



