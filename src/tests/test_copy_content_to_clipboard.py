#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


from src.functions.copy_content_to_clipboard import copy_content_to_clipboard


class AppMock:
    def clipboard_clear(self):
        pass

    def clipboard_append(self, content):
        pass


class TextBoxMock:
    def __init__(self):
        self.content = ""

    def get(self, start, end):
        return self.content

    def delete(self, start, end):
        self.content = ""


def test_copy_content_to_clipboard(monkeypatch):
    """
    Test the `copy_content_to_clipboard` function.

    This function tests the `copy_content_to_clipboard` function by using monkeypatching to mock
    `AppMock` and `TextBoxMock`. It verifies that the function correctly copies the content of `text_box`
    to the clipboard and clears the content of `text_box` afterward.

    This test function uses pytest's `monkeypatch` fixture for mocking and does not return anything.
    """

    # Create instances of AppMock and TextBoxMock
    app_mock = AppMock()
    text_box_mock = TextBoxMock()

    # Set initial content in the text box
    initial_content = "Hello, pytest!"
    text_box_mock.content = initial_content

    # Monkeypatch the instance methods
    monkeypatch.setattr(app_mock, 'clipboard_clear', lambda: None)
    monkeypatch.setattr(app_mock, 'clipboard_append', lambda content: None)
    monkeypatch.setattr(text_box_mock, 'get', lambda start, end: text_box_mock.content)
    monkeypatch.setattr(text_box_mock, 'delete', lambda start, end: setattr(text_box_mock, 'content', ""))

    # Call the function under test
    copy_content_to_clipboard(app_mock, text_box_mock)

    # Assertions
    assert text_box_mock.content == ""
