#!/usr/bin/env python3
""" Auth Methods
"""
from bcrypt import checkpw, hashpw, gensalt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ Hashes a password and returns hash
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """ Generate UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a User and returns the user object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if login credentials are valid
        """
        try:
            user = self._db.find_user_by(email=email)
            if checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> str:
        """ Creates a session for the user and returns the session ID
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
    
    def get_user_from_session_id(self, session_id: str) -> str:
        """ Finds user by session ID
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                pass
        return None