#!/usr/bin/env python3
""" Basic User Authentication Module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Basic Authentication Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts Base64 Authorization Header
        """

        auth = authorization_header
        if auth and type(auth) is str and auth.startswith("Basic "):
            return auth.split(" ")[1]

        return None
