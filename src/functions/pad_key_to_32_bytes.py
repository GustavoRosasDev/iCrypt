#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# Function to ensure that the key is exactly 32 bytes
def pad_key_to_32_bytes(key_text):
    """
    Pad a key to a length of 32 bytes.

    Args:
        key_text (Union[str, bytes]): The key to be padded. If it is a string, it will be encoded to bytes.

    Returns:
        bytes: The padded key.

    Raises:
        None.

    Examples:
        >>> pad_key_to_32_bytes('mykey')
        b'mykey                '
        >>> pad_key_to_32_bytes(b'mykey')
        b'mykey                '
    """

    # Convert the key to bytes if it's not already
    key_bytes = key_text.encode() if isinstance(key_text, str) else key_text

    # Use a padding character, for example ' ' (space)
    key_padding = key_bytes.ljust(32, b' ')

    return key_padding
