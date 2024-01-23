#!/usr/bin/env python3
""" Auth Methods
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Hashes a password and returns hash
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a User and returns the user object
        """
        user = self._db.find_user_by(email=email)

        if user:
            raise ValueError(f"User {email} already exists")

        user = self._db.add_user(email, str(_hash_password(password)))

        return user
