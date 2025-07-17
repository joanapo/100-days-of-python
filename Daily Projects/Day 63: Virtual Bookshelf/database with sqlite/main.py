import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

"""
create a new table:

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
               "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
"""

cursor.execute("INSERT INTO books VALUES(1, 'Lie with Me', 'Philippe Besson', '3.75')")
db.commit()