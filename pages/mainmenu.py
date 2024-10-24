from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

def cards_select(root, type):
    h1style = ttk.Style()
    h1style.configure('TLabel', font=('Helvetica', 20, 'bold'), foreground="white", background="#191919")

    menu_var = StringVar(value="Select a Flashcard Pack")
    menu_options = ["PS - Element Orders", "ESP - Direct Object Pronouns"]

    label = ttk.Label(root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(root, text="|", foreground="#191919").pack(pady=30)
    menu = OptionMenu(root, menu_var, *menu_options).pack(pady=10)
    spacer_2 = ttk.Label(root, text="|", foreground="#191919").pack(pady=10)

    def export_menu(menu):
        print(menu.get)

    start_button = ttk.Button(root, text="Start A Training Session", command=lambda: export_menu(menu)).pack()