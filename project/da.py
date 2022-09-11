from multiprocessing import connection
import MySQLdb as mdb
DBNAME="it" 
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"
db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
print('database connected')

db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)  #CONNECTING TO THE DATABASE
cur = db.cursor()    #CREATING CURSOR

# cur.execute("DROP TABLE IF EXISTS Register")  #creating tables

# # # creating query
# sqlquery = """
# CREATE TABLE Register(
#     first_Name varchar(20) NOT NULL,
#     last_name varchar(20) NOT NULL,
#     contact int (11),
#     Email varchar(20) NOT NULL,
#     SECURITYA varchar (10) NOT NULL,
#     password varchar (10) NOT NULL
# )
# """

# cur.execute(sqlquery)
insertquery = """
INSERT INTO Register(first_Name,last_name,contact,Email,SECURITYA,password) VALUES('Victor','Godwin',08105953704,'Victor@gmail.com','hospital','anita2590')
  """
cur.execute(insertquery)
db.commit()
print('database well commited')