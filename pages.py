from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

def cardselect(self):
    h1style = ttk.Style()
    h1style.configure('TLabel', font=('Helvetica', 20, 'bold'), foreground="white", background="#191919")

    menu_var = StringVar(value="Select a Flashcard Pack")
    menu_options = ["PS - Element Orders", "ESP - Direct Object Pronouns"]

    def export_menu(menu_var):
        print(menu_var)

    label = ttk.Label(self.root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=30)
    menu = OptionMenu(self.root, menu_var, *menu_options, command=export_menu).pack(pady=10)
    spacer_2 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=10)

    start_button = ttk.Button(self.root, text="Start A Training Session", command=lambda: export_menu(menu_var)).pack()