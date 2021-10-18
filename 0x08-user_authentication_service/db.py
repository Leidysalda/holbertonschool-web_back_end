#!/usr/bin/env python3
""" DB Module
"""
from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user method
        """
        ed_user = User(email=email, hashed_password=hashed_password)
        self._session.add(ed_user)
        self._session.commit()
        return ed_user

    def find_user_by(self, **kwargs) -> User:
        """ Find user method
        """
        if not kwarg:
            raise InvalidRequestError

        c_names = User.__table__.columns._data.keys()

        for key in kwargs.keys():
            if key in c_names:
                ed_user = self._session.query(User).filter_by(**kargs).first()
                if ed_user is None:
                    raise NoResultFound
                return ed_user
        raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update user method
        """
        columns = User.__table__.columns._data.keys()
        for key in kwargs.keys():
            if key not in columns:
                raise ValueError
        session = (update(User)
                   .where(User.id == user_id)
                   .values(**kwargs))
        self._session.execute(session)
        self._session.commit()
