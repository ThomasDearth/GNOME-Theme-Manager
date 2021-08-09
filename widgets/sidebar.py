#
# Thomas Dearth
# August 5, 2021
# Sidebar class used for managing themes
#

from tkinter import ttk

from styles.style_sidebar import SidebarStyle


class Sidebar(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=master)
        self.master = master
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        style = SidebarStyle()
        style.style_frame(frame=self)

        content = []

        label_select_picture = ttk.Label(master=self, text="Select Picture:")
        content.append(label_select_picture)
        label_select_picture.grid(column=0, row=0)

        for widget in content:
            widget.configure(padding=(0, (150-widget.winfo_width())/2))
            style.style_label(widget)

        self.pack()

