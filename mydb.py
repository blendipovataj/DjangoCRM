import mysql.connector



dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password = 'Blendi2003'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE scofield")

print("All Done!")

