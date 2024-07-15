#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# Function to change the first_slider (Encryption-Decryption) name
def change_first_slider_name(first_slider):
    """
    Change the name of the switch between "Encryption" and "Decryption".
    """

    current_text = first_slider.cget("text")
    if current_text == "Decryption":
        first_slider.configure(text="Encryption")
    elif current_text == "Encryption":
        first_slider.configure(text="Decryption")


# Function to change the second_slider (Text-File) name
def change_second_slider_name(second_slider, first_button, text_box, copy_button):
    """
    Change the name of the switch between "Encryption" and "Decryption".
    """

    current_text = second_slider.cget("text")
    if current_text == "Text":
        second_slider.configure(text="File")
        first_button.pack(side="right")
        text_box.delete("1.0", "end")
        text_box.configure(state="disabled")
        copy_button.pack_forget()
    elif current_text == "File":
        second_slider.configure(text="Text")
        first_button.pack_forget()
        text_box.configure(state="normal")
        copy_button.pack(side="right", padx=5)
