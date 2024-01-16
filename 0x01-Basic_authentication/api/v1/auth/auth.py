#!/usr/bin/env python3
""" User Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires Auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Auth Header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
