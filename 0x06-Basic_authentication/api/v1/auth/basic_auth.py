#!/usr/bin/env python3
"""Basic auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Basic - Base64 part
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Basic - Base64 part
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base = base64_authorization_header.encode('utf-8')
            decoded = b64decode(base)
            info = decoded.decode('utf-8')
            return info
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Basic - User credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' in decoded_base64_authorization_header:
            data = decoded_base64_authorization_header.split(':')
            return data[0], data[1]
        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Basic - User object
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            list_search = User.search({'email': user_email})
            for item in list_search:
                if item.is_valid_password(user_pwd):
                    return item
                return None
        except Exception:
            return None

        def current_user(self, request=None) -> TypeVar('User'):
            """ Basic - Overload current_user - and BOOM!
            """
            auth = self.authorization_header(request)
            code = self.extract_base64_authorization_header(auth)
            decoded = self.decode_base64_authorization_header(code)
            mail, password = self.extract_user_credentials(decoded)
            return self.user_object_from_credentials(mail, password)
