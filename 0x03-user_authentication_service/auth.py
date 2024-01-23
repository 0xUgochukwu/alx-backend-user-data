#!/usr/bin/env python3
""" Auth Methods
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """ Hashes a password and returns hash
    """
    return hashpw(password.encode('utf-8'), gensalt())
