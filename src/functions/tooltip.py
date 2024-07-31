#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

import tkinter as tk


class ToolTip:
    def __init__(self, widget, text):
        """
            Initializes an instance of the Tooltip class.

            Parameters:
            widget (tk.Widget): The widget to which the tooltip is associated.
            text (str): The text to be displayed in the tooltip.

            Attributes:
            widget (tk.Widget): Stores the associated widget.
            text (str): Stores the text to be displayed in the tooltip.
            tip_window (tk.Toplevel or None): Tooltip window, initially set to None.

        """

        self.widget = widget
        self.text = text
        self.tip_window = None

    def show_tip(self, _event=None):
        """
            Displays a tooltip window for the widget that called the event.

            This function creates a `Toplevel` window to show a contextual tip when the user interacts with the associated widget. The window is positioned close to the mouse cursor and is only displayed if a hint (`self.text`) is available and if there is no hint window already visible.

            Parameters:
            _event (tk.Event, optional): Event that triggered the tip to be displayed. This parameter is ignored if provided.

            The function performs the following actions:
            - Calculates the position of the hint window based on the position of the mouse cursor relative to the widget.
            - Creates a borderless `Toplevel` window and defines its position on the screen.
            - Adds a `Label` to the tip window, displaying the tip text, with basic formatting.

            The tip window will be positioned slightly offset from the mouse cursor to ensure it does not overlap the cursor itself.

            Comments:
            - If a hint window is already visible, it will not be recreated.
            - If `self.text` is not defined, the tooltip will not be displayed.

        """

        if self.tip_window or not self.text:
            return
        x, y, _cx, _cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 40
        y = y + self.widget.winfo_rooty() - 10
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffff", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, _event=None):
        """
            Hides the tooltip window associated with the object.

            Parameters:
            _event (optional): Event that can trigger hiding the tip. This parameter is optional and not used in the function.

            The function checks if the tip window (tip_window) is present. If so, the window is destroyed and the reference to the tip window is removed by setting the `tip_window` attribute to `None`.

            Example:
            This function can be called, for example, when the user moves the cursor away from the element displaying the tip, or when a specific action requires hiding the tip.

        """

        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


def create_tooltip(widget, text):
    """
    Creates and associates a tooltip with a widget.

    Parameters:
    widget (tk.Widget): The widget to which the tooltip will be associated.
    text (str): The tooltip text that will be displayed when the mouse cursor is over the widget.

    The function creates a `ToolTip` object with the provided text and associates it with the widget. It also links the
    events of input ('<Enter>') and output ('<Leave>') of the cursor to the widget to show and hide the tooltip
    respectively.

    Example:
    ```python
    create_tooltip(my_button, "Click me to perform an action")
    ```
    """
    tool_tip = ToolTip(widget, text)
    widget.bind('<Enter>', tool_tip.show_tip)
    widget.bind('<Leave>', tool_tip.hide_tip)
