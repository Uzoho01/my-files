
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3



class Register:
        def __init__(self,master):
                self.master=master
                self.master.title("REGISTER")
                self.master.geometry("1800x800")

#                 # variables
                
            

            #  bd image
                self.bg=ImageTk.PhotoImage(file= "picture\pot.png")
                bglbl= Label(self.master,image=self.bg)
                bglbl.place(x=0,y=0,relwidth=1,relheight=1)


#                 # leftimage
                
                self.bg1=ImageTk.PhotoImage(file= "picture\p.png")
                leftimage= Label(self.master,image=self.bg1)
                leftimage.place(x=50,y=100,width=170,height=400)


                frame = Frame(self.master,bg="white")
                frame.place(x=7,y=100,width=400,height=1000)

                registerlbl =Label (frame,text="REGISTERE HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
                registerlbl.place(x=70,y=20)
#                 # label and entries
                f_name_label =Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
                f_name_label.place(x=0,y=100)

                f_name = ttk.Entry(frame,font=("times new roman",15,"bold"))
                f_name.place(x=0,y=130,width=160)

                l_name_label =Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
                l_name_label.place(x=230,y=100)
                
                l_name = ttk.Entry(frame,font=("times new roman",15,"bold"))
                l_name.place(x=230,y=130,width=160)
# # # # row 2
                
                contact_label =Label(frame,text="Contact N0",font=("times new roman",15,"bold"),fg="black")
                contact_label.place(x=0,y=170)
                
                contact = ttk.Entry(frame,font=("times new roman",15,"bold"))
                contact.place(x=0,y=200,width=160)

                
                
                email_label =Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
                email_label.place(x=230,y=170)
                
                email = ttk.Entry(frame,font=("times new roman",15,"bold"))
                email.place(x=230,y=200,width=160)

#         #     row3
                
                security_Q_label =Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q_label.place(x=0,y=240)

                
                
                combo_security_Q = ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
                combo_security_Q["values"] = ("SELECT" ,"Your Birth Place","Your Boyfriend Name","Your Hubby","Your First Name")
                combo_security_Q.place(x=0,y=270,width=160)
                combo_security_Q.current(0)
                
                security_A_label = Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A_label.place (x=230,y=240)
                security_A = ttk.Entry(frame,font=("times new roman",15,"bold"))
                security_A.place(x=230 ,y=270,width= 160)
#                 #      row4
                
                password_label =Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                password_label.place(x=0,y=310)
                
                password = ttk.Entry(frame,font=("times new roman",15,"bold"))
                password.place(x=0,y=340,width=160)

                
                
                confirm_password_label =Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                confirm_password_label.place(x=230,y=310)
                
                c_password = ttk.Entry(frame,font=("times new roman",15,"bold"))
                c_password.place(x=230,y=340,width=160)

                
#                 # check button
                var_check = IntVar()
                Checkbut = Checkbutton(frame,text="I Agree To Terms And Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
                Checkbut.place(x=50,y=380)


#                 # buttons
                img =Image.open(r"C:\Users\User\Desktop\python\project\picture\g.png")
                img = img.resize((150,75),Image.ANTIALIAS)
                self.photoimage = ImageTk.PhotoImage(img)
                b1 = Button (frame,command = self.submit,image=self.photoimage,borderwidth=0,cursor="hand2")
                b1.place(x=0,y=420,width = 160)


                
                img1 =Image.open(r"C:\Users\User\Desktop\python\project\picture\Login.png")
                img1 = img1.resize((150,75),Image.ANTIALIAS)
                self.photoimage1 = ImageTk.PhotoImage(img1)
                b1 = Button (frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
                b1.place(x=200,y=420,width = 160)
# # printing the names out
               

#                 # functio declaration:


        def registration(self):
                        
                if self.var_f_name.get()==""or self.var_email.get()==""or self.var_securityA.get()=="SELECT":
                         messagebox.showerror("ERROR","ALL Field Required")

                elif self.var_password.get()!=self.var_confirmpassword.get():
                        messagebox.showerror("Error","Password & Confirm Password Must Be They Same")
                elif self.var_check.get()==0:
                         messagebox.showerror("Error","Please Agree Our Terms And Conditions")
                else: 
                        messagebox.showinfo("Success","Welcome To Ani Pharmaceutical Limited ")
                

                  
                # create a database 
        def submit(self):

         conn = sqlite3.connect("address.db")
         c = conn.cursor()
# c .execute("""CREATE TABLE addresses(
#         first_name text, 
#         last_name text, 
#         Email text,
#         Password text,
#         securityA text,
#         contact integer)""")

         c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :Email, :Password, :securityA, :contact)",
  
  {"f_name":self.var_f_name.get(),
    "l_name": self.var_l_name.get(),
    "Email": self.var_Email.get(),
    "Password": self.var_password.get(),
    "securityA": self.var_security_A.get(),
    "contact": self.var_contact.get()} )






         conn.commit()
         conn.close()
 

                
        
                                        


                        

    
if __name__== "__main__":
    master=Tk()
    form =Register(master)
    master.mainloop()








