import sqlite3

con = sqlite3.connect('user.db')

c = con.cursor()

# Create Table
c.execute('''CREATE TABLE IF NOT EXISTS users (
            rollno real, 
            name text,
            email text,
            
        )''')
