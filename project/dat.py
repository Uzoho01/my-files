import MySQLdb as md
from MySQLdb import Error

conn = md.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "data"
)
