#!/usr/bin/env python3
''' Password Encryption Module
'''
from bcrypt import hashpw, gensalt


def hash_password(password: str) -> str:
    ''' Returns a hashed password '''
    return hashpw(password.encode('utf-8'), gensalt())