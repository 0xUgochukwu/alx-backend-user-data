#!/usr/bin/env python3
""" Basic User Authentication Module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 Authorization Header
        """
        b64auth = base64_authorization_header
        if b64auth and type(b64auth) is str:
            try:
                decoded = b64decode(b64auth.encode('utf-8'))
                return decoded.decode('utf-8')
            except Exception:
                return None

