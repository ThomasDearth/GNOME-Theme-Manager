#
# Thomas Dearth
# August 5, 2021
# Window class as an enclosure for a tkinter Frame
#

from tkinter import ttk

from widgets import sidebar, theme_pane


class Window(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master = master

        # Create child frames
        self.__menu_sidebar = sidebar.Sidebar(self)
        self.__theme_pane = theme_pane.ThemePane(self)

        # Define grid
        self.rowconfigure(index=0, weight=1, minsize=500)
        self.columnconfigure(index=0, weight=1, minsize=170)
        self.__menu_sidebar.grid(column=0, row=0, sticky="news")
        self.columnconfigure(index=1, weight=3, minsize=510)
        self.__theme_pane.grid(column=1, row=0, sticky="news")
        self.grid(row=0, column=0, sticky="news")

    def update_size(self, width, height):
        self.configure(width=width, height=height)


