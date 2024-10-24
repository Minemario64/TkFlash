from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

def cards_select(root, type):
    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 16, 'bold'), foreground="white", background="#191919")

    menu_var = StringVar(value="Select a Flashcard Pack")
    menu_options = ["PS - Element Orders", "ESP - Direct Object Pronouns"]

    label = ttk.Label(root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(root, text="|", foreground="#191919").pack(pady=50)
    menu = OptionMenu(root, menu_var, *menu_options).pack(pady=10)