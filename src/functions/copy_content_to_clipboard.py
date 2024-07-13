#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


def copy_content_to_clipboard(app, text_box):
    """
    Copy the content of a text_box to the clipboard and clear the same field.

    Args:
        app: The application object.
        text_box: The text box widget.

    Returns:
        None
    """

    text_box_start = "1.0"  # Start index of the content
    text_box_end = "end"  # End index of the content

    # Copy the content of the text_box to the clipboard
    content = text_box.get(text_box_start, text_box_end)
    app.clipboard_clear()  # Clear the clipboard before adding new content
    app.clipboard_append(content)  # Add the content to the clipboard

    # Clear the existing content in the text_box
    text_box.delete(text_box_start, text_box_end)
