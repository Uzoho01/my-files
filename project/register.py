
from tkinter import*
from tkinter import ttk
from unicodedata import name
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from  assign import insert_into_db



class Register:
        def __init__(self,master):
                self.master=master
                self.master.title("REGISTER")
                self.master.geometry("1800x800")

                # variables
                
                self.var_fname = StringVar()
                self.var_lname = StringVar()
                self.var_contact = StringVar()
                self.var_email = StringVar()
                self.var_securityQ = StringVar()
                self.var_securityA = StringVar()
                self.var_password = StringVar()
                self.var_confirmpassword = StringVar()
                


        #      bd image
                self.bg=ImageTk.PhotoImage(file= "picture\pot.png")
                bglbl= Label(self.master,image=self.bg)
                bglbl.place(x=0,y=0,relwidth=1,relheight=1)


                # leftimage
                
                # self.bg1=ImageTk.PhotoImage(file= "picture\p.png")
                # leftimage= Label(self.master,image=self.bg1)
                # leftimage.place(x=50,y=100,width=170,height=400)


                frame = Frame(self.master,bg="white")
                frame.place(x=7,y=100,width=400,height=1000)

                registerlbl =Label (frame,text="REGISTERE HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
                registerlbl.place(x=70,y=20)
                # label and entries
                fname =Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
                fname.place(x=0,y=100)
               

                fname_entry = ttk.Entry(frame,textvariable = self.var_fname,font=("times new roman",15,"bold"))
                fname_entry.place(x=0,y=130,width=160)

                lname =Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
                lname.place(x=230,y=100)
                
                self.txt_l_name = ttk.Entry(frame,textvariable = self.var_lname,font=("times new roman",15,"bold"))
                self.txt_l_name.place(x=230,y=130,width=160)
# # # row 2
                
                contact =Label(frame,text="Contact N0",font=("times new roman",15,"bold"),fg="black")
                contact.place(x=0,y=170)
                
                self.contactentry = ttk.Entry(frame,textvariable= self.var_contact,font=("times new roman",15,"bold"))
                self.contactentry.place(x=0,y=200,width=160)

                
                
                email =Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
                email.place(x=230,y=170)
                
                self.emailentry = ttk.Entry(frame,textvariable= self.var_email,font=("times new roman",15,"bold"))
                self.emailentry.place(x=230,y=200,width=160)

        #     row3
                
                security_Q =Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=0,y=240)

                
                
                self.combo_security_Q = ttk.Combobox(frame,textvariable= self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"] = ("SELECT" ,"Your Birth Place","Your Boyfriend Name","Your Hubby","Your First Name")
                self.combo_security_Q.place(x=0,y=270,width=160)
                self.combo_security_Q.current(0)
                
                security_A = Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place (x=230,y=240)
                self.txt_security = ttk.Entry(frame,textvariable= self.var_securityA,font=("times new roman",15,"bold"))
                self.txt_security.place(x=230 ,y=270,width= 160)
                #      row4
                
                password =Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                password.place(x=0,y=310)
                
                self.passwordentry = ttk.Entry(frame,textvariable= self.var_password,font=("times new roman",15,"bold"))
                self.passwordentry.place(x=0,y=340,width=160)

                
                
                confirm_password =Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                confirm_password.place(x=230,y=310)
                
                self.confirm_passwordentry = ttk.Entry(frame,textvariable= self.var_confirmpassword,font=("times new roman",15,"bold"))
                self.confirm_passwordentry.place(x=230,y=340,width=160)

                
                # check button
                self.var_check = IntVar()
                Checkbut = Checkbutton(frame,variable= self.var_check,text="I Agree To Terms And Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
                Checkbut.place(x=50,y=380)
                

                # buttons
                img =Image.open(r"C:\Users\User\Desktop\python\project\picture\g.png")
                img = img.resize((150,75),Image.ANTIALIAS)
                self.photoimage = ImageTk.PhotoImage(img)
                b1 = Button (frame,command = self.registration,image=self.photoimage,borderwidth=0,cursor="hand2")
                b1.place(x=0,y=420,width = 160)


                
                img1 =Image.open(r"C:\Users\User\Desktop\python\project\picture\Login.png")
                img1 = img1.resize((150,75),Image.ANTIALIAS)
                self.photoimage1 = ImageTk.PhotoImage(img1)
                b1 = Button (frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
                b1.place(x=200,y=420,width = 160)
# printing the names out
                # functio declaration:
        def password_validation(password):
                specialsym = ["@","#","$","%","^","&","*","=","+","(",")","?",">","<",",","!"]
                val = True
                if len (password)<8:
                        print("password invalid it is less than 8 characters")
                        val = False
                if len (password)>15:
                        print("password should not be greater than 20 characters")
                        val= False
                if not any(char . isdigit() for char in password):
                        print("password should have at leaste one number")
                        val = False
                if not any(char . isupper()for char in password):
                        print("password should have at leaste one upper case letter")
                        val = False
                if not any(char . islower()for char in password):
                        print("password should hav e at leaste one lowercase letter")
                        val = False
                if not any (char in specialsym for char in password):
                        print("password should have have of the specialsym")
                        val = False
                if val:
                        return val
        


                
                        



        def registration(self):
                        
                if self.var_fname.get()==""or self.var_email.get()==""or self.var_securityA.get()=="SELECT":
                         messagebox.showerror("ERROR","ALL Field Required")

                elif self.var_password.get()!=self.var_confirmpassword.get():
                        messagebox.showerror("Error","Password & Confirm Password Must Be They Same")
                elif self.var_check.get()==0:
                         messagebox.showerror("Error","Please Agree Our Terms And Conditions")
                else: 
                        
                        messagebox.showinfo("Success","Welcome To Ani Pharmaceutical Limited ")

                        first_name= self.var_fname.get()
                        last_name = self.var_lname.get()
                        email = self.var_email.get()
                        pwd = self.var_password.get()
                        securty_ans= self.var_securityA.get()
                        contact = self.var_contact.get()

                        insert_into_db(first_name, last_name, email, pwd, securty_ans, contact)
                  
        
       
                
        
                                        


                        

    
if __name__== "__main__":
    master=Tk()
    form =Register(master)
    master.mainloop()








