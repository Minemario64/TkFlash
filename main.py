from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from getfile import *

root = Tk()

def change_pages(cur_page,new_page):
    if cur_page == new_page:
        return "Error : Same Page"
    closing_page = getattr(PAGES, cur_page)
    closed = closing_page(root, "clear")

isDbEmpty= is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")

cursor = connection.cursor()
if isDbEmpty:
    cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)


connection.close()

root.mainloop()