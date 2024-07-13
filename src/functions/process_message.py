#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# Function to process encryption/decryption
def process_message(entry_key,
                    text_box,
                    slider_value,
                    pad_key_to_32_bytes,
                    fernet,
                    base64,
                    messagebox):
    """
    A function that processes a message by getting the key and message from entry and text boxes, padding the key to 32
    bytes, and either encrypting or decrypting the message based on a slider value. Shows error messages if there are
    exceptions during processing.
    """

    # Get the key from the entry box
    key_text = entry_key.get()
    print(f'key_text {key_text}')

    # Get the message from the text box
    message = text_box.get("1.0", "end-1c")
    print(f'message {message}')

    try:
        # Pad the key to 32 bytes
        padded_key = pad_key_to_32_bytes(key_text)

        # Create a Fernet instance with the padded key
        fernet_key = fernet(base64.urlsafe_b64encode(padded_key))

        if slider_value.get() == "on":
            # Encrypt the message
            encrypted_message = fernet_key.encrypt(message.encode())
            text_box.delete("1.0",
                            "end")  # Clear the text box
            text_box.insert("1.0",
                            encrypted_message.decode())
        else:
            # Decrypt the message
            decrypted_message = fernet_key.decrypt(message.encode())
            text_box.delete("1.0",
                            "end")  # Clear the text box
            text_box.insert("1.0",
                            decrypted_message.decode())
    except ValueError as ve:
        messagebox.showerror("Error",
                             f"Error processing: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Error",
                             f"Unknown error processing: {str(e)}")
    # Clear the key (entry box)
    entry_key.delete(0, "end")
