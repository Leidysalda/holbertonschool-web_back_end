#!/usr/bin/env python3
"""Auth class
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """class Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require Authentication
        """
        route = '/api/v1/status'
        if path is None or excluded_paths in [None, []]:
            return True
        elif path in excluded_paths or path + '/' in excluded_paths \
                or route in excluded_paths:
            return False
        elif path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request
        """
        if request is None:
            return None
        SESSION_NAME = getenv('SESSION_NAME')
        cookie_name = request.cookies.get(SESSION_NAME)
        return cookie_name
