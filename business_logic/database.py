import mysql.connector

db = mysql.connector.connect(
    host = "db",
    user = "tema",
    password = "tema",
    database = "movies"
)

cursor = db.cursor(buffered = True)