#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


from src.functions.change_switch_name import change_first_slider_name


def test_change_switch_name():
    """
        Test the `change_switch_name` function.

        This function tests the `change_switch_name` function by creating two instances of the `SliderMock` class,
        one with the initial switch name "Decryption" and the other with the switch name "Encryption".
        It then calls the `change_switch_name` function on each instance and asserts that the switch name
        has been correctly changed.

        This test function does not have any parameters and does not return anything.

        Example:
        test_change_switch_name()
    """

    class SliderMock:
        def __init__(self, text):
            """
                Initializes a new SliderMock instance.

                Parameters:
                text (str): The text value to associate with the slider.
            """
            self.text = text

        def cget(self, attribute):
            """
                Returns the value of the requested attribute.

                Parameters:
                attribute (str): Name of the attribute to be returned.

                Returns:
                str: Value of the requested attribute, currently only "text" is supported.
            """
            if attribute == "text":
                return self.text

        def configure(self, **kwargs):
            """
                Sets the 'text' attribute to the given value.

                Parameters:
                **kwargs: Named arguments, where 'text' is the only argument supported.

                Example:
                slider.configure(text="New Name")
            """

            self.text = kwargs.get("text")

    # Test initial switch name "Decryption"
    slider_decryption = SliderMock("Decryption")
    change_first_slider_name(slider_decryption)
    assert slider_decryption.text == "Encryption"

    # Test switch name "Encryption"
    slider_encryption = SliderMock("Encryption")
    change_first_slider_name(slider_encryption)
    assert slider_encryption.text == "Decryption"
