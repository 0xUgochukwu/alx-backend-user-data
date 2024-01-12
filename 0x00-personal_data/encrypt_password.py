#!/usr/bin/env python3
''' Password Encryption Module
'''
from bcrypt import hashpw, gensalt, checkpw


def hash_password(password: str) -> bytes:
    ''' Returns a hashed password '''
    return hashpw(password.encode('utf-8'), gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Validates that the provided password matches the hashed password '''
    return checkpw(password.encode('utf-8'), hashed_password)
