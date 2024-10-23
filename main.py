from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from getfile import *

root = Tk()

is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)

root.mainloop()