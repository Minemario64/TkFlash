from tkinter import *
from PIL import ImageTk,Image
import pages

class window:

    def __init__(self, title : str, winicon : str = "TkFlash.ico", geometry = False) -> None:
        self.cur_page = None
        self.geometry = geometry
        self.title = title
        self.icon = winicon

        self.root = Tk()
        if geometry is not False:
            self.root.geometry(geometry)
        self.root.title(title)
        self.root.config(background="#191919")

    def show_window(self, startingPage : str, loadWithPage : bool = False) -> None:
        if loadWithPage:
            cur_page = getattr(pages, startingPage) # type: ignore
            page = cur_page(self)
            self.cur_page = startingPage

        self.root.mainloop()

    def change_pages(self, new_page):
        if self.cur_page == new_page:
            return "Error : Same Page"
        for widget in self.root.winfo_children:
            widget.destroy()
        newPage = getattr(pages.new_page, new_page)
        page = newPage()