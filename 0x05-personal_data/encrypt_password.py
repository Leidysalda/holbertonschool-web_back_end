#!/usr/bin/env python3
""" Encrypting passwords
"""
import logging
import re
from os import getenv
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash password
    """
    pwd = bytes(password, encoding="utf-8")
    hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validate
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
