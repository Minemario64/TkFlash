from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from getfile import *
from pages import *

root = Tk()
root.title("Flashcard Menu")
root.config(background="#191919")
root.geometry("400x400")

def change_pages(cur_page,new_page):
    if cur_page == new_page:
        return "Error : Same Page"
    closing_page = getattr(pages, cur_page) # type: ignore
    closed = closing_page(root, "clear")

isDbEmpty= is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")

cursor = connection.cursor()
if isDbEmpty:
    cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)

cards_select(root, 1)

connection.close()

root.mainloop()