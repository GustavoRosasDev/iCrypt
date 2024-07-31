#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


def banner():
    """
    A function that returns the banner text.
    """

    banner_text = "      𝐢𝐂𝐫𝐲𝐩𝐭"
    return banner_text


def remove_placeholder(_event, text_box, banner_text, WHITE_COLOR):
    if text_box.get("1.0", "end-1c") == banner_text:
        text_box.delete("1.0", "end")
        text_box.configure(font=("Arial", 13), text_color=WHITE_COLOR)


def add_placeholder(_event, text_box, banner_text, GRAY_90_COLOR):
    if text_box.get("1.0", "end-1c") == "":
        text_box.insert("1.0", banner_text)
        text_box.configure(font=("Arial", 70), text_color=GRAY_90_COLOR)
