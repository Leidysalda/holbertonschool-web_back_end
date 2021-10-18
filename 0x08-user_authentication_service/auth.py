#!/usr/bin/env python3
"""
Hash password
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """
    hash password method
    """
    passwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def _generate_uuid() -> str:
    """
    generate uuid method
    """
    return str(uuid.uuid4())


class Auth:
    """
    Class Auth
    """
    def __init__(self):
        """
        Constructor method
        """
        self._db = DB()

    def register_user(self, mail: str, password: str) -> User:
        """
        Register method
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user
        raise ValueError('User {} alredy exists'.format(user.email))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user with login method
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, mail: str) -> str:
        """
        Create session method
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        user.session_id = _generate_uuid()
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Get user method
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy session method
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """
        Reset password method
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        new_uuid = _generate_uuid()
        user.reset_token = new_uuid
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update password method
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed = _hash_password(password)
        user.hashed_password = hashed
        user.reset_token = None
