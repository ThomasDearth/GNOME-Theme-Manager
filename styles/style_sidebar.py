#
# Thomas Dearth
# August 5, 2021
# Contains styling information for the sidebar
#
from tkinter import ttk

from styles.generic_style import BasicStyle


class SidebarStyle(BasicStyle):
    def __init__(self):
        super().__init__()
        self.__background_color = "#343434"

    def style_frame(self, frame):
        self._style_object.configure("Sidebar.TFrame",
                                     background=self.__background_color)
        frame.configure(style="Sidebar.TFrame")

    def style_label(self, label):
        self._style_object.configure("Sidebar.TLabel",
                                     background=self.__background_color)
        self._style_object.configure("Sidebar.TLabel", foreground="#e7fcf3")
        label.configure(style="Sidebar.TLabel")
