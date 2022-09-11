import sqlite3
con =sqlite3.connect('indiv.db')  
c = con.cursor()
c.execute("""CREATE TABLE user(  
        first_name text, 
        last_name text, 
        Email text,
        Password text,
        securityA text,
        contact int
    
) """)
user = ('chuks', 'emeka', 'chuls@gmail.com','anny#','hospital',9827736636)
# # EXECUTE OUR cusor
c.executemany("INSERT INTO user VALUES (?,?,?,?,?,?)", user )  # ??? are the place holders for ech field

print('command executed successfully...')
print("connected")
con.commit()
con.close()



