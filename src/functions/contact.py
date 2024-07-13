#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.etc.imports import webbrowser


def open_profile():
    """
    Opens the LinkedIn profile of Developer in the default web browser.

    Returns:
        None
    """
    profile_url = 'linkedin.com/in/gustavorosas-'
    webbrowser.open(profile_url)
