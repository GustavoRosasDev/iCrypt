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


