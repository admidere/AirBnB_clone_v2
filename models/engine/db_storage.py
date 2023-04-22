#!/usr/bin/python3
"""A new type of storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    Database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create the engine and the session
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(user, pwd, host, db),
                                       pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session
        all objects depending of the class name
        """
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        objects = {}
        for c in classes:
            query = self.__session.query(c)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects
    def new(self, obj):
        """
        Add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """close session"""
        self.__session.close()
