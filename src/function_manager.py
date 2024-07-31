#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

# noinspection PyUnresolvedReferences
from src.functions.change_switch_name import (change_first_slider_name,
                                              change_second_slider_name)
# noinspection PyUnresolvedReferences
from src.functions.pad_key_to_32_bytes import pad_key_to_32_bytes
# noinspection PyUnresolvedReferences
from src.functions.encryption_decryption import (aes_128_message_processor,
                                                 aes_256_message_processor,
                                                 handle_aes_encryption,
                                                 browse_file)
# noinspection PyUnresolvedReferences
from src.functions.copy_content_to_clipboard import copy_content_to_clipboard
# noinspection PyUnresolvedReferences
from src.functions.tooltip import create_tooltip
# noinspection PyUnresolvedReferences
from src.functions.banner import banner, remove_placeholder, add_placeholder
