from tkinter import *
from PIL import ImageTk,Image
from questions.questionManager import *
import sqlite3
from getfile import *
import pages.pageManager as pg

isDbEmpty= is_db_empty("translates.db")

connection = sqlite3.connect("translates.db")
cursor = connection.cursor()
if isDbEmpty:
    cursor.execute("""CREATE TABLE translates (id INTEGER PRIMARY KEY, Spanish TEXT, English TEXT, Class_id INTEGER)
            """)
connection.close()

main = pg.window("Flashcard Menu", geometry="400x400")
main.show_window(loadWithPage=True, startingPage="cardselect")
test = Question(type="MC", dbColumnList=["id", "Spanish", "English", "class_id"], dbCallList=[1, 2], db="translates.db", dbTable="translates", class_id=0)
test.create_question()
main.change_pages(new_page="QuestionPage")