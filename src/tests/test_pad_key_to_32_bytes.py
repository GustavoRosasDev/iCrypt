#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


from src.functions.pad_key_to_32_bytes import pad_key_to_32_bytes


def test_pad_key_to_32_bytes():
    """
    Test the `pad_key_to_32_bytes` function.

    This function tests the `pad_key_to_32_bytes` function by verifying that keys are correctly padded
    to a length of 32 bytes using spaces.

    This test function does not have any parameters and does not return anything.
    """

    # Test with string key
    assert pad_key_to_32_bytes('mykey').rstrip() == b'mykey'

    # Test with bytes key
    assert pad_key_to_32_bytes(b'mykey').rstrip() == b'mykey'

    # Test with short string key
    assert pad_key_to_32_bytes('short').rstrip() == b'short'

    # Test with already padded key
    assert pad_key_to_32_bytes('already 32 bytes long').rstrip() == b'already 32 bytes long'

    # Test with non-ASCII string (should encode to bytes correctly and strip right spaces)
    assert pad_key_to_32_bytes('äöü').rstrip() == 'äöü'.encode()
