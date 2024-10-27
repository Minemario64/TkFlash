from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from getfile import *
import pageManager as pg

isDbEmpty= is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")
cursor = connection.cursor()
if isDbEmpty:
    cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)
connection.close()

main = pg.window("Flashcard Menu", geometry="400x400")
main.show_window(loadWithPage=True, startingPage="cardselect")