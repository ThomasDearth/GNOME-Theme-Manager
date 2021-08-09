#
# Thomas Dearth
# August 5, 2021
# Generic template for a themed style
#

from tkinter import ttk


class BasicStyle:
    def __init__(self):
        self._style_object = ttk.Style()

    def style_frame(self, frame):
        """Applies a style to a Frame.

        :param frame: the Frame to be assigned properties
        :type frame: ttk.Frame
        """
        raise NotImplementedError

    def style_label(self, label):
        """Applies a style to a Label.

        :param label: the Label to be assigned properties
        :type label: ttk.Label
        """
        raise NotImplementedError

