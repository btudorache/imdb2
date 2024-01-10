import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "tema",
    password = "tema",
    database = "movies"
)

cursor = db.cursor(buffered = True)