# import mysql.connector

# dataBase = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password123"
# )

# cursorObject = dataBase.cursor()

# cursorObject.execute("CREATE DATABASE elderco")

# print("All done!")

import sqlite3
con = sqlite3.connect("dcrm.db")
cur = con.cursor()
print('DB Init')