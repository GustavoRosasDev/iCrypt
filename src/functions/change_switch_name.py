#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# Function to change the switch name
def change_switch_name(slider):
    """
    Change the name of the switch between "Encryption" and "Decryption".
    """

    current_text = slider.cget("text")
    if current_text == "Decryption":
        slider.configure(text="Encryption")
    elif current_text == "Encryption":
        slider.configure(text="Decryption")

