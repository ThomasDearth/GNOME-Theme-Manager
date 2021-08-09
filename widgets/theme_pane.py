#
# Thomas Dearth
# August 5, 2021
# Main pane for selecting themes
#

from tkinter import ttk


class ThemePane(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        apply_theme_pane_style(self)


def apply_theme_pane_style(ttk_object):
    """Applies theme-pane-standard styling to a ttk object.
    
    :param ttk_object: a TTK object to style
    :type ttk_object: ttk.Widget
    """
    object_style = ttk.Style()
    object_style.configure("ThemePane.TFrame", background="#3e3e3e")
    ttk_object.configure(style="ThemePane.TFrame")
