#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

import os
import base64
from tkinter import filedialog

# region Cryptography

''' AES encryption '''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding

# endregion

filename = ""


def handle_aes_encryption(first_dropdown,
                          second_slider,
                          entry_key,
                          text_box,
                          first_slider_value,
                          messagebox):
    """
    Handle AES encryption and decryption based on dropdown and slider values.

    Depending on the values selected in the dropdown and slider, this function
    will process AES-128 or AES-256 encryption/decryption on either a message
    in the text box or a file.

    Args:
        first_dropdown (ctk.CTkComboBox): Dropdown for selecting AES-128 or AES-256.
        second_slider (ctk.CTkSwitch): Slider for selecting 'on' (file mode) or 'off' (message mode).
        entry_key (ctk.CTkEntry): Entry widget for the encryption key.
        text_box (ctk.CTkTextbox): Text widget for the message to be encrypted/decrypted.
        first_slider_value (tkinter.StringVar): Slider for selecting encryption ('on') or decryption ('off').
        messagebox (tkinter.messagebox): Messagebox for displaying error messages.

    Returns:
        None
    """

    # Get values
    dropdown_value = first_dropdown.get()
    second_slider_value = second_slider.get()

    if dropdown_value == "AES-128" and second_slider_value == "off":
        aes_128_message_processor(entry_key,
                                  text_box,
                                  first_slider_value,
                                  messagebox)
    elif dropdown_value == "AES-256" and second_slider_value == "off":
        aes_256_message_processor(entry_key,
                                  text_box,
                                  first_slider_value,
                                  messagebox)

    elif dropdown_value == "AES-256" and second_slider_value == "on":
        process_file(entry_key,
                     filename,
                     text_box)


def pad_key_to_length(key_text, length):
    """
        Pad a key to a specific length.

        Args:
            key_text (str): The key to pad.
            length (int): The desired length of the padded key.

        Returns:
            bytes: The padded key.

    """

    return key_text.ljust(length, '\0')[:length].encode()


# AES-128 Encryption/Decryption
def aes_128_message_processor(entry_key,
                              text_box,
                              first_slider_value,
                              messagebox):
    """
    Processes a message using AES-128 encryption (CBC mode) for encryption or decryption.

    Parameters:
    entry_key (ctk.CTkEntry): Entry field for the encryption key.
    text_box (ctk.CTkTextbox): Text box containing the message to be encrypted/decrypted.
    first_slider_value (tk.StringVar): Value of the slider determining whether to encrypt ("on") or decrypt
    (another value).
    messagebox (tk.messagebox): Object to display error messages.

    The encryption process includes:
    - Generation of a random IV (initialization vector).
    - Message completion using PKCS7.
    - Message encryption with the provided key.
    - Coding of the encrypted message and the IV in base64 to facilitate storage.

    The decryption process includes:
    - Message decoding in base64.
    - Extraction of the IV and the encrypted message.
    - Message decryption with the provided key.
    - Removed PKCS7 padding to restore the original message.

    In case of an error, an error message is displayed using the messagebox.

    Exceptions Treated:
    - ValueError: For value-related errors during the encryption/decryption process.
    - Exception: For any other unforeseen errors.

    The input key is deleted at the end of processing.

    """

    key_text = entry_key.get()
    message = text_box.get("1.0", "end-1c")

    try:
        key = pad_key_to_length(key_text, 16)  # 16 bytes for AES-128
        iv = os.urandom(16)  # Random IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        if first_slider_value.get() == "on":
            # Encrypt the message
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(message.encode()) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
            encrypted_message_base64 = base64.urlsafe_b64encode(iv + encrypted_message).decode()
            text_box.delete("1.0", "end")
            text_box.insert("1.0", encrypted_message_base64)
        else:
            # Decrypt the message
            encrypted_data = base64.urlsafe_b64decode(message.encode())
            iv = encrypted_data[:16]
            encrypted_message = encrypted_data[16:]
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_message) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            unpadded_message = unpadder.update(decrypted_data) + unpadder.finalize()
            text_box.delete("1.0", "end")
            text_box.insert("1.0", unpadded_message.decode())
    except ValueError as ve:
        messagebox.showerror("Error", f"Error processing: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Error", f"Unknown error processing: {str(e)}")
    entry_key.delete(0, "end")


# AES-256 Encryption/Decryption
def aes_256_message_processor(entry_key,
                              text_box,
                              first_slider_value,
                              messagebox):
    """
        Processes a message using AES-256 encryption (CBC mode) for encryption or decryption.

        Parameters:
        entry_key (ctk.CTkEntry): Entry field for the encryption key.
        text_box (ctk.CTkTextbox): Text box containing the message to be encrypted/decrypted.
        first_slider_value (tk.StringVar): Value of the slider determining whether to encrypt
        ("on") or decrypt (another value).
        messagebox (tk.messagebox): Object to display error messages.

        The encryption process includes:
        - Generation of a random IV (initialization vector).
        - Message completion using PKCS7.
        - Message encryption with the provided key.
        - Coding of the encrypted message and the IV in base64 to facilitate storage.

        The decryption process includes:
        - Message decoding in base64.
        - Extraction of the IV and the encrypted message.
        - Message decryption with the provided key.
        - Removed PKCS7 padding to restore the original message.

        In case of an error, an error message is displayed using the messagebox.

        Exceptions Treated:
        - ValueError: For value-related errors during the encryption/decryption process.
        - Exception: For any other unforeseen errors.

        The input key is deleted at the end of processing.

    """

    key_text = entry_key.get()
    message = text_box.get("1.0", "end-1c")

    try:
        key = pad_key_to_length(key_text, 32)  # 32 bytes for AES-256
        iv = os.urandom(16)  # Random IV
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        if first_slider_value.get() == "on":
            # Encrypt the message
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(message.encode()) + padder.finalize()
            encryptor = cipher.encryptor()
            encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
            encrypted_message_base64 = base64.urlsafe_b64encode(iv + encrypted_message).decode()
            text_box.delete("1.0", "end")
            text_box.insert("1.0", encrypted_message_base64)
        else:
            # Decrypt the message
            encrypted_data = base64.urlsafe_b64decode(message.encode())
            iv = encrypted_data[:16]
            encrypted_message = encrypted_data[16:]
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(encrypted_message) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            unpadded_message = unpadder.update(decrypted_data) + unpadder.finalize()
            text_box.delete("1.0", "end")
            text_box.insert("1.0", unpadded_message.decode())
    except ValueError as ve:
        messagebox.showerror("Error", f"Error processing: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Error", f"Unknown error processing: {str(e)}")
    entry_key.delete(0, "end")

# endregion


# region File Processor

def browse_file(text_box, COLOR):
    """
        Opens a dialog box for the user to select a file and displays the file path in the provided text box.

        Parameters:
        text_box (ctk.CTkTextbox): Text box where the path of the selected file will be displayed.

        Functionality:
        - Opens a file selection dialog using filedialog.askopenfilename().
        - If a file is selected, the function:
            - Sets the text box to an editable state.
            - Deletes any existing text in the text box.
            - Inserts the path of the selected file into the text box.
            - Sets the text box to a non-editable state.

        Global Variables:
        - filename (str): Stores the path of the selected file globally.

    """

    global filename

    filename = filedialog.askopenfilename()
    if filename:
        text_box.configure(state="normal")
        text_box.delete(1.0, "end")
        text_box.insert(1.0, filename)
        text_box.configure(font=("Arial", 13), text_color=COLOR, state="disabled")


def generate_key(password, salt):
    """
    Generates a cryptographic key derived from a password using PBKDF2-HMAC-SHA256.

    Parameters:
    password (str): The password to use to derive the key.
    salt (bytes): The cryptographic salt to be used in the key derivation process.

    Returns:
    bytes: The 32-byte derived key.

    The key derivation process includes:
    - Use of the PBKDF2 (Password-Based Key Derivation Function 2) algorithm with HMAC-SHA256.
    - The password is encoded in bytes and combined with the salt.
    - 100000 iterations of the algorithm are performed to increase security.
    - The backend used is the default one provided by the cryptography library.

    The combination of a password and a unique salt ensures that the derived key is strong and resistant to brute force
    attacks and precomputation (rainbow table) attacks.
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


# Function to encrypt or decrypt a file based on the file extension
def process_file(password, file_path, text_box):
    """
    Processes a file for encryption or decryption based on the file extension.

    Parameters:
    password (ctk.CTkEntry): Input field containing the password for encryption/decryption.
    file_path (str): Path of the file to be processed.
    text_box (ctk.CTkTextbox): Text box to display status messages or results.

    The process is determined by the file extension:
    - If the file extension is '.enc', the file will be decrypted using the decrypt_file function.
    - Otherwise, the file will be encrypted using the encrypt_file function.

    The input password is extracted from the input widget and passed to the encryption or decryption functions.

    """

    # Extract the text from the entry_key widget
    entry_key = password.get()

    if file_path.endswith('.enc'):
        # Decrypt
        decrypt_file(entry_key, file_path, text_box)
    else:
        # Encrypt
        encrypt_file(entry_key, file_path, text_box)


def encrypt_file(password, file_path, text_box):
    """
    Encrypts a file using AES-256 in GCM mode and displays a success message in a text box.

    Parameters:
    password (str): Password used to generate the encryption key.
    file_path (str): Path of the file to be encrypted.
    text_box (ctk.CTkTextbox): Text box to display the success message.

    The encryption process includes:
    - Generation of a 16-byte salt.
    - Derivation of a 256-bit key from the password and salt.
    - Generation of a 12-byte IV (initialization vector) for GCM mode.
    - Reading the file contents.
    - Filling in file data using PKCS7.
    - Creation of a Cipher object to encrypt data.
    - Writing encrypted data to the file with '.enc' extension, including the salt, IV and tag.

    At the end of the process, a success message is displayed in the text box.
    """

    # Generate a salt and a 256-bit key
    salt = os.urandom(16)
    key = generate_key(password, salt)

    # Generate a 12-byte IV (initialization vector) for GCM
    iv = os.urandom(12)

    # Read the contents of the file
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Add padding to the file data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Create the Cipher object and encrypt the data
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted data to the file with salt, iv, and tag
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encryptor.tag + ciphertext)

    text_box.configure(state="normal")
    text_box.delete("1.0", "end")
    text_box.insert("1.0", "File successfully encrypted.")
    text_box.tag_add("red_text", "1.17", "1.27")  # Colorful tag for "encrypted"
    text_box.tag_config("red_text", foreground="red")
    text_box.configure(state="disabled")


def decrypt_file(password, file_path, text_box):
    """
    Decrypts a file using the AES-256 algorithm in GCM mode.

    Parameters:
    password (str): Password used to generate the decryption key.
    file_path (str): Path of the encrypted file that will be decrypted.
    text_box (ctk.CTkTextbox): Text box used to display success or error messages.

    The decryption process includes:
    - Reading the contents of the encrypted file.
    - Extraction of salt, IV (initialization vector), authentication tag and encrypted data from the file.
    - Generation of the 256-bit key from the password and salt.
    - Creation of the Cipher object and data decryption.
    - Removed PKCS7 padding to restore original data.
    - Writing the decrypted data to the original file, replacing the ".enc" suffix.

    After decryption, the function updates the text_box to inform you that the file was successfully decrypted.

    Exceptions Treated:
    - There is no explicit exception handling in this function. Any error during the process will result in an exception
    being raised.
    """

    # Read the contents of the encrypted file
    with open(file_path, 'rb') as f:
        data = f.read()

    # Extract the salt, iv, tag, and encrypted data
    salt = data[:16]
    iv = data[16:28]
    tag = data[28:44]
    ciphertext = data[44:]

    # Generate the 256-bit key from the password and salt
    key = generate_key(password, salt)

    # Create the Cipher object and decrypt the data
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove the padding from the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()

    # Write the decrypted data to the original file
    original_file_path = file_path.rsplit('.enc', 1)[0]
    with open(original_file_path, 'wb') as f:
        f.write(plaintext)

    text_box.configure(state="normal")
    text_box.delete("1.0", "end")
    text_box.insert("1.0", f"File successfully decrypted.")
    text_box.tag_add("green_text", "1.17", "1.27")  # Colorful tag for "decrypted"
    text_box.tag_config("green_text", foreground="green")
    text_box.configure(state="disabled")

# endregion
