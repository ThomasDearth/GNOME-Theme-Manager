#
# Thomas Dearth
# August 8, 2021
# Class object for tkinter.Tk()
#

import tkinter as tk

from window import Window


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set title and dimensions
        self.wm_title("GNOME Theme Manager")
        self._width = 680
        self._height = 500
        self.minsize(self._width, self._height)

        # Create and initialize main Frame object
        self._app = Window(self)

        # Bind the "on-resize" function to when the window is resized
        self.bind("<Configure>", self.__on_resize)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_width(self, width):
        if width < 0:
            raise ValueError
        else:
            self._width = width

    def set_height(self, height):
        if height < 0:
            raise ValueError
        else:
            self._height = height

    def __on_resize(self, event):
        """Resizes the root object and the window within.

        :param event: the window resizing event
        """
        # Cite your sources, kids
        # https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width

        # Check if the event changes anything
        if (event.width != self.get_width()) or (event.height !=
                                                 self.get_height()):
            # Update the Tk's width and height
            width = self.winfo_width()
            height = self.winfo_height()
            self.configure(width=event.width, height=event.height)
            self.set_width(event.width)
            self.set_height(event.height)

            # Update main Frame's size (and, since components within are
            # sticky, everything within it)
            self._app.update_size(width, height)
