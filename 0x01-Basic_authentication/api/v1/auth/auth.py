#!/usr/bin/env python3
""" User Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if a path requires Authentication
        """
        if path and excluded_paths:
            if path[-1] != '/':
                path = path + '/'
            return path in excluded_paths
        return True

    def authorization_header(self, request=None) -> str:
        """ Auth Header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
