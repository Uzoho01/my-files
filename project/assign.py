
import sqlite3



# c.execute("""CREATE TABLE users(  
#         first_name text, 
#         last_name text, 
#         Email text,
#         Password text,
#         securityA text,
#         contact int
    
# ) """)

def insert_into_db(first_name, last_name, email, pwd, securty_ans, contact):
    # # # EXECUTE OUR cusor
    con = sqlite3.connect('customer.db')  # when you run this program like this it is going to create a db file\
    c = con.cursor()
    c.execute("INSERT INTO users  (first_name, last_name, email, password, securityA, contact)VALUES(?,?,?,?,?,?)",(first_name, last_name, email, pwd, securty_ans, contact))  #sqlite3 COMMAND TO INSERT TABLE

    print('command executed successfully...')

    # print("check if users table exists in the database: ")
    # listoftables = c.execute(
    #     """SELECT name FROM sqlite_master WHERE type ="table"
    #     AND name = "users" ; """)
    # if listoftables ==[]:
    #      print("These database and tables exists does not exist")
        
    # else:
    #     print("These database and tables exists ")

    con.commit() 
    con.close()

