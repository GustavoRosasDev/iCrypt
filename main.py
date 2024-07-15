#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.manager import *
from src.function_manager import *

# Declare global variables
first_slider = None
second_slider = None
first_slider_value = None
second_slider_value = None
first_button = None
entry_key = None
text_box = None
start_button = None


def main():
    """
    A function that sets up the main user interface elements for the application.
    """

    global first_slider, second_slider, first_slider_value, second_slider_value, first_button, entry_key, text_box, \
        start_button

    # region 🟢 Tabs

    # region 🟩 Initial Setup (margins and borders)

    # Creation of the 'tab' Element
    tab = ctk.CTkTabview(APP,
                         width=APP_WIDTH - 0,
                         height=APP_HEIGHT - 0,
                         fg_color=GRAY_90_COLOR,
                         border_color=LIGHT_GREEN_COLOR,
                         segmented_button_selected_color=LIGHT_BLUE_COLOR,
                         segmented_button_selected_hover_color=DARK_BLUE_COLOR, )  # Bordas laterais = 10px
    tab.pack(padx=0,
             pady=0)

    # endregion

    # region 🟩 Main Tab Names
    # Defining names for the main interface tabs
    tab_1 = 'Home'
    tab_2 = "Info"

    # Adding tabs to the interface
    tab.add(tab_1)
    tab.add(tab_2)

    # Variables representing the tabs
    first_tab = tab.tab(tab_1)
    second_tab = tab.tab(tab_2)

    # endregion

    # Define the main tab
    tab.set(tab_1)

    # endregion

    # region 1️⃣ First Tab (Home)

    # Container ▶️ "Create" Button
    first_tab_header_container = ctk.CTkFrame(
        master=first_tab,
        fg_color=TRANSPARENT_COLOR,
        bg_color=TRANSPARENT_COLOR)
    first_tab_header_container.pack(side=ctk.TOP,
                                    fill=ctk.X,
                                    expand=False,
                                    anchor="n",
                                    padx=5)

    # region 🟩 Sliders + Button (Container)

    # Create a slider for choosing between encryption and decryption
    first_slider_value = ctk.StringVar()
    first_slider = ctk.CTkSwitch(master=first_tab_header_container,
                                 text="Decryption",
                                 variable=first_slider_value,
                                 onvalue="on",
                                 offvalue="off",
                                 progress_color=LIGHT_BLUE_COLOR,
                                 command=lambda: change_first_slider_name(first_slider))
    first_slider.pack(pady=10,
                      side=ctk.LEFT)

    # Create a slider for choosing between text and file
    second_slider_value = ctk.StringVar()
    second_slider = ctk.CTkSwitch(master=first_tab_header_container,
                                  text="Text",
                                  variable=second_slider_value,
                                  onvalue="on",
                                  offvalue="off",
                                  progress_color=LIGHT_BLUE_COLOR,
                                  command=lambda: change_second_slider_name(second_slider,
                                                                            first_button,
                                                                            text_box,
                                                                            copy_button))
    second_slider.pack(pady=10,
                       padx=20,
                       side=ctk.LEFT)

    first_button = ctk.CTkButton(master=first_tab_header_container,
                                 text="Search File",
                                 height=30,
                                 width=100,
                                 fg_color=LIGHT_RED_COLOR,
                                 hover_color=DARK_RED_COLOR,
                                 command=process_file)
    first_button.pack(side=ctk.RIGHT)
    first_button.pack_forget()

    # endregion

    # region 🟥 Entry Fields
    
    # Create an entry field for the encryption key
    entry_key = ctk.CTkEntry(master=first_tab,
                             placeholder_text="Enter the key here")
    entry_key.pack(pady=5,
                   padx=5,
                   fill=ctk.X)

    # Create a text box for displaying encrypted/decrypted content
    text_box = ctk.CTkTextbox(master=first_tab,
                              height=110)
    text_box.pack(pady=5,
                  padx=5,
                  fill=ctk.BOTH)

    # endregion

    # region 🟦 Footer (Container)

    # Container ▶️ "Create" Button
    first_tab_footer_container = ctk.CTkFrame(
        master=first_tab,
        fg_color=TRANSPARENT_COLOR,
        bg_color=TRANSPARENT_COLOR)
    first_tab_footer_container.pack(side=ctk.BOTTOM,
                                    fill=ctk.X,
                                    expand=False,
                                    anchor="n")

    # Create a button to start the encryption/decryption process
    start_button = ctk.CTkButton(master=first_tab_footer_container,
                                 text="Start",
                                 height=40,
                                 fg_color=LIGHT_BLUE_COLOR,
                                 hover_color=DARK_BLUE_COLOR,
                                 font=HIGHLIGHT_FONT,
                                 command=lambda: process_message(entry_key,
                                                                 text_box,
                                                                 first_slider_value,
                                                                 pad_key_to_32_bytes,
                                                                 fernet,
                                                                 base64,
                                                                 messagebox))
    start_button.pack(pady=5,
                      padx=5,
                      side=ctk.LEFT,
                      fill=ctk.X,
                      expand=True)

    # Create a button to copy the content of the text boxI
    copy_button = ctk.CTkButton(master=first_tab_footer_container,
                                text="🗐",
                                font=("Material Symbols Outlined", 24),
                                height=40,
                                width=40,
                                fg_color=LIGHT_GREEN_COLOR,
                                hover_color=DARK_GREEN_COLOR,
                                command=lambda: copy_content_to_clipboard(APP, text_box))
    copy_button.pack(pady=5,
                     padx=5,
                     side=ctk.RIGHT)

    # endregion
    
    # endregion

    # region 2️⃣ Second Tab (Info)

    # region 🟨 Frame of Frames (smaller groups)
    info_tab_container = ctk.CTkFrame(master=second_tab,
                                      border_width=1,
                                      border_color=GRAY_50_COLOR)
    info_tab_container.pack(side=ctk.TOP,
                            padx=5,
                            pady=5,
                            fill=ctk.X,
                            expand=True,
                            anchor="n")
    # endregion

    # region 🟨 First group

    # FRAME: Desenvolvedor

    info_tab_first_frame_group = ctk.CTkFrame(master=info_tab_container,
                                              fg_color=TRANSPARENT_COLOR)
    info_tab_first_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    anchor="n", pady=2, padx=2)

    info_tab_first_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_first_frame_group, text="DEVELOPER",
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_first_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                    anchor='w', expand=False,
                                                    ipadx=20)

    info_tab_first_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_first_frame_group, text=DEVELOPER_NAME,
        text_color=LIGHT_BLUE_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_first_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                     anchor='w', expand=True,
                                                     ipadx=20)

    # endregion

    # region 🟨 Second group

    # FRAME: App Name

    info_tab_second_frame_group = ctk.CTkFrame(master=info_tab_container,
                                               fg_color=TRANSPARENT_COLOR)
    info_tab_second_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                     anchor="n", padx=2)

    info_tab_second_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_second_frame_group, text="APP NAME",
        text_color=GRAY_COLOR,
        font=SMALL_FONT)
    info_tab_second_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                     anchor='w', expand=False,
                                                     ipadx=20)

    info_tab_second_frame_group_first_info_text_space = ctk.CTkLabel(
        master=info_tab_second_frame_group, text='   ',
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_second_frame_group_first_info_text_space.pack(side=ctk.LEFT,
                                                           fill=ctk.X,
                                                           anchor='w',
                                                           expand=False)

    info_tab_second_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_second_frame_group, text=APP_NAME,
        text_color=LIGHT_BLUE_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_second_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                      anchor='w', expand=True,
                                                      ipadx=20)

    # endregion

    # region 🟨 Third group

    # FRAME: Version

    info_tab_third_frame_group = ctk.CTkFrame(master=info_tab_container,
                                              fg_color=TRANSPARENT_COLOR)
    info_tab_third_frame_group.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                    anchor="n", pady=2, padx=2)

    info_tab_third_frame_group_first_info_text = ctk.CTkLabel(
        master=info_tab_third_frame_group, text="VERSION",
        text_color=GRAY_COLOR,
        font=SMALL_FONT)
    info_tab_third_frame_group_first_info_text.pack(side=ctk.LEFT, fill=ctk.X,
                                                    anchor='w', expand=False,
                                                    ipadx=20)

    info_tab_third_frame_group_first_info_text_space = ctk.CTkLabel(
        master=info_tab_third_frame_group, text='      ',
        text_color=GRAY_COLOR, font=SMALL_FONT)
    info_tab_third_frame_group_first_info_text_space.pack(side=ctk.LEFT,
                                                          fill=ctk.X,
                                                          anchor='w',
                                                          expand=False)

    info_tab_third_frame_group_first_text_value = ctk.CTkLabel(
        master=info_tab_third_frame_group,
        text=APP_VERSION,
        text_color=LIGHT_RED_COLOR,
        font=HIGHLIGHT_FONT)
    info_tab_third_frame_group_first_text_value.pack(side=ctk.RIGHT,
                                                     anchor='w', expand=True,
                                                     ipadx=20)

    # endregion

    # region 🚫 Optional Spacer
    info_tab_third_frame_group_end_spacer = ctk.CTkLabel(master=second_tab,
                                                         text='')
    info_tab_third_frame_group_end_spacer.pack(expand=True, fill=ctk.Y)
    # endregion

    # region 🟨 FOOTER (Text + action button)
    # Info text
    info_tab_footer_info_text = ctk.CTkLabel(master=second_tab,
                                             text="Automations, Upgrades or Support?",
                                             text_color=GRAY_COLOR,
                                             font=MEDIUM_FONT)
    info_tab_footer_info_text.pack(side=ctk.TOP, fill=ctk.X, expand=True,
                                   anchor="s")

    # "Contact" Button
    info_tab_footer_button = ctk.CTkButton(master=second_tab,
                                           text="Contact Developer",
                                           command=open_profile,
                                           height=40,
                                           fg_color=LIGHT_BLUE_COLOR,
                                           hover_color=DARK_BLUE_COLOR)
    info_tab_footer_button.pack(side=ctk.BOTTOM, fill=ctk.X, padx=5, pady=5)
    # endregion

    # endregion

    # Run the main customtkinter event loop
    APP.mainloop()


# Run the program
if __name__ == "__main__":
    main()
