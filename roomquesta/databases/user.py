import sqlite3

con = sqlite3.connect('user.db')

c = con.cursor()

c.execute("CREATE TABLE users VALUES")
