import MySQLdb as mdb
DBNAME="pharmacy" 
DBHOST = "localhost"
DBPASS = ""
DBUSER = "root"
db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
print('database connected')

db=mdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)  #CONNECTING TO THE DATABASE
cur = db.cursor()    #CREATING CURSOR


# cur.execute("DROP TABLE IF EXISTS Register_form")  #creating tables
# # creating query
# sqlquery = """
# CREATE TABLE Register_form(
#     first_Name varchar(20) NOT NULL,
#     last_name varchar(20) NOT NULL,
#     contact int (11),
#     Email varchar(20) NOT NULL,
#     SECURITYQ varchar (20) NOT NULL,
#     SECURITYA varchar (10) NOT NULL,
#     password varchar (10) NOT NULL
# )
# """


# # cur.execute(sqlquery)
# # print('Table created successfully connected')
def insertdata():


  insertquery = """
  INSERT INTO Register_form(first_Name,last_name,contact,Email,SECURITYA,password) VALUES('Victor','Godwin',09076543211,'Victor@gmail.com', 'Your Birth Place','hospital','anita2590')
  """

  cur.execute(insertquery)
  db.commit()
  print('database well commited')