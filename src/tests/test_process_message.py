#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from unittest.mock import Mock
from src.functions.encryption_decryption import handle_aes_encryption


class TextBoxMock:
    def __init__(self, text=""):
        """
            Initializes an instance of the class with optional text.

            Parameters:
            text (str): Text to be assigned to the `text` property of the instance. The default value is an empty
            string.

            Attributes:
            text (str): Attribute that stores the text provided during initialization.
        """

        self.text = text

    def get(self, start="1.0", end="end-1c"):
        """
            Returns a substring of text stored between the specified indexes.

            Parameters:
            start (str): Starting index of the substring in the format "line.column". The default is "1.0", which
            represents the beginning of the text.
            end (str): End index of the substring in the format "line.column". The default is "end-1c", which represents
             the end of the text, excluding the last character.

            Returns:
            str: The substring of text stored between the `start` and `end` indexes.

            Behavior:
            - If `start` and `end` are strings in the format "row.column", the function will try to extract the column
            index from the string. If the format is incorrect, the default value will be 0 for `start` and the text
            length for `end`.
            - If `end` is "end-1c", the end index will be adjusted to the length of the text minus one character.

            Exceptions:
            - If the format of the indices is invalid and cannot be converted to integers, default values are used.

        """

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
        """
            Inserts text at a specific position within existing text.

            Parameters:
            index (int or str): Position where the text should be inserted. If it is a string in the format
            'line.column',
                                the column is extracted and converted to an integer index.
            text (str): Text to be inserted at the specified index.

            The function performs the following:
            - If the `index` parameter is a string in the format 'row.column', the column is extracted and converted to
            an integer.
            - The provided text is inserted at the specified position within the existing text, shifting subsequent text
             to the right.

            Example:
            If the current text is "Hello world" and the given index is 4, then after calling `insert(4, " beautiful")`,
            the text will be "Hello beautiful world".

        """

        if isinstance(index, str):
            index = int(index.split('.')[1])
        self.text = self.text[:index] + text + self.text[index:]

    def delete(self, start, end):
        """
            Removes a portion of text based on the given start and end indices.

            Parameters:
            start (int, str): Start index or a string representing the start index (in the format 'row.column').
                              If it is a string in the format 'row.column', the index will be extracted from the part
                              after the dot.
            end (int, str): End index or a string representing the end index (in the format 'row.column').
                            If it is a string in the format 'row.column', the index will be extracted from the part
                            after the dot.
                            If the value is "end-1c", the end index will be adjusted to the total length of the text.

            The method performs the following steps:
            - Converts the `start` and `end` parameters to integer indexes. If they are strings, extract the part after
            the dot.
            - Sets `end_index` to the full length of the text if the value is "end-1c".
            - If `start_index` is greater than `end_index`, reverse the indexes.
            - Removes the part of the text that is between `start_index` and `end_index` from the current text.

            Comments:
            - If `start` or `end` is not in the expected format, the method assumes that `start` is 0 and `end` is the
            total length of the text.

        """

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


def test_handle_aes_encryption():
    """
        Tests the `handle_aes_encryption` function to ensure that AES encryption processing works correctly.

        This test uses mock objects to simulate interaction with graphical interface components and verifies the
        behavior of the `handle_aes_encryption` function in a controlled scenario.

        Steps taken:
        1. Creation of mock objects to represent the input fields (`entry_key`), text box (`text_box`), and slider and
        dropdown values.
        2. Simulation of the `messagebox.showerror` function to check whether error messages are displayed correctly.
        3. Execution of the `handle_aes_encryption` function with the configured mocks.
        4. Verification that `messagebox.showerror` was not called, indicating that no error was generated during
        processing.
        5. Validation that the content of the text box was processed correctly and corresponds to the expected value.

        Assumptions:
        - The `handle_aes_encryption` function should process the message without errors, as indicated by `assert` and
        the fact that `message_box.showerror` is not called.
        - The input value in the text box must remain unchanged after processing, as indicated by the assertion `assert
        text_box.get() == "my_secret_message"`.

        Dependencies:
        - The `handle_aes_encryption` function must be implemented correctly and must interact with the mocks as
        expected.
        - The mock module must be imported and configured correctly to simulate interactions with the graphical
        interface.
    """

    # Create mock objects
    entry_key = TextBoxMock("my_secret_key")
    text_box = TextBoxMock("my_secret_message")
    slider_value = Mock()
    slider_value.get.return_value = "off"
    dropdown = Mock()
    dropdown.get.return_value = "AES-128"

    # Mock message box to simulate messagebox functions
    message_box = Mock()
    message_box.showerror = Mock()

    # Run the function
    handle_aes_encryption(dropdown, slider_value, entry_key, text_box, slider_value, message_box.pyi)

    # Verify that message_box.showerror was called correctly
    message_box.showerror.assert_not_called()  # Adjust based on expected behavior

    # Verify if the text_box content was processed correctly
    assert text_box.get() == "my_secret_message"  # Adjust based on expected result
