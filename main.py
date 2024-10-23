from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from getfile import *

root = Tk()

isDbEmpty= is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")

cursor = connection.cursor()
if isDbEmpty:
    cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)

root.mainloop()