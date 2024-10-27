from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from getfile import *
from fontLoader import *

def cardselect(self):
    loadfont("Lemon Fruit.otf")
    h1style = ttk.Style()
    h1style.configure('TLabel', font=('Lemon Fruit', 32), foreground="white", background="#191919")

    menu_var = StringVar(value="Select a Flashcard Pack")
    menu_options = ["PS - Element Orders", "ESP - Verbs"]

    def export_menu(menu_var):
        print(menu_var)

    label = ttk.Label(self.root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=20)
    menu = OptionMenu(self.root, menu_var, *menu_options, command=export_menu).pack(pady=10)
    spacer_2 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=10)

    start_button = ttk.Button(self.root, text="Start A Training Session").pack()