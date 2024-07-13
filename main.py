#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.manager import *
from src.function_manager import *

# Declare global variables
slider = None
slider_value = None
entry_key = None
text_box = None
start_button = None


def main():
    """
    A function that sets up the main user interface elements for the application.
    """

    global slider, slider_value, entry_key, text_box, start_button
    
    # Create the main frame
    main_frame = ctk.CTkFrame(master=APP)
    main_frame.pack(pady=20,
                    padx=20, 
                    fill="both",
                    expand=True)

    # Create a slider for choosing between encryption and decryption
    slider_value = ctk.StringVar()
    slider = ctk.CTkSwitch(master=main_frame,
                           text="Decryption",
                           variable=slider_value,
                           onvalue="on",
                           offvalue="off",
                           progress_color=LIGHT_BLUE_COLOR,
                           command=lambda: change_switch_name(slider))
    slider.pack(pady=10, 
                padx=10)

    # Create an entry field for the encryption key
    entry_key = ctk.CTkEntry(master=main_frame,
                             placeholder_text="Enter the key here")
    entry_key.pack(pady=5,
                   padx=10,
                   fill=ctk.X)

    # Create a text box for displaying encrypted/decrypted content
    text_box = ctk.CTkTextbox(master=main_frame,
                              height=100)
    text_box.pack(pady=5,
                  padx=10,
                  fill=ctk.BOTH)

    # region 🟦 "Footer Container"

    # Container ▶️ "Create" Button
    main_tab_footer_container = ctk.CTkFrame(
        master=main_frame,
        fg_color=GRAY_80_COLOR,
        bg_color=TRANSPARENT_COLOR)
    main_tab_footer_container.pack(side=ctk.BOTTOM,
                                   fill=ctk.X,
                                   expand=False,
                                   anchor="n",
                                   padx=5)

    # Create a button to start the encryption/decryption process
    start_button = ctk.CTkButton(master=main_tab_footer_container,
                                 text="Start",
                                 height=40,
                                 width=340,
                                 fg_color=LIGHT_BLUE_COLOR,
                                 hover_color=DARK_BLUE_COLOR,
                                 font=HIGHLIGHT_FONT,
                                 command=lambda: process_message(entry_key,
                                                                 text_box,
                                                                 slider_value,
                                                                 pad_key_to_32_bytes,
                                                                 fernet,
                                                                 base64,
                                                                 messagebox))
    start_button.pack(pady=10,
                      padx=5,
                      side=ctk.LEFT,
                      fill=ctk.X)

    # Create a button to copy the content of the text box
    copy_button = ctk.CTkButton(master=main_tab_footer_container,
                                text="🗐",
                                font=("Material Symbols Outlined", 24),
                                height=40,
                                fg_color=LIGHT_GREEN_COLOR,
                                hover_color=DARK_GREEN_COLOR,
                                command=lambda: copy_content_to_clipboard(APP, text_box))
    copy_button.pack(pady=10,
                     padx=5,
                     side=ctk.RIGHT)

    # endregion

    # Run the main customtkinter event loop
    APP.mainloop()


# Run the program
if __name__ == "__main__":
    main()
