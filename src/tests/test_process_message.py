#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from unittest.mock import Mock
from src.functions.process_message import process_message


class TextBoxMock:
    def __init__(self, text=""):
        self.text = text

    def get(self, start="1.0", end="end-1c"):
        start_index = 0
        end_index = len(self.text)

        if isinstance(start, str):
            try:
                start_index = int(start.split('.')[1])
            except IndexError:
                start_index = 0

        if isinstance(end, str):
            if end == "end-1c":
                end_index = len(self.text)
            else:
                try:
                    end_index = int(end.split('.')[1])
                except IndexError:
                    end_index = len(self.text)

        return self.text[start_index:end_index]

    def insert(self, index, text):
        if isinstance(index, str):
            index = int(index.split('.')[1])
        self.text = self.text[:index] + text + self.text[index:]

    def delete(self, start, end):

        if isinstance(start, str):
            try:
                start_index = int(start.split('.')[1])
            except IndexError:
                start_index = 0
        else:
            start_index = start

        if isinstance(end, str):
            if end == "end-1c":
                end_index = len(self.text)
            else:
                try:
                    end_index = int(end.split('.')[1])
                except IndexError:
                    end_index = len(self.text)
        else:
            end_index = end

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        self.text = self.text[:start_index] + self.text[end_index:]


def test_process_message():
    entry_key = TextBoxMock("my_secret_key")
    text_box = TextBoxMock("my_secret_message")
    slider_value = "on"

    def pad_key_to_32_bytes(key):
        return key[:32].ljust(32, b' ')

    def fernet(key):
        return key

    def base64_encode(key):
        return key

    # Create a mock object for MessageBox
    message_box = Mock()

    # Simulate the process_message function
    process_message(entry_key, text_box, slider_value, pad_key_to_32_bytes, fernet, base64_encode, message_box)

    # Verify if the text_box variable was correctly set
    assert text_box.get() == "my_secret_message"
