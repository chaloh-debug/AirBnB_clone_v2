#!/usr/bin/python3
""" module for file storage management"""
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session


class DBStorage:
    """ database storage engine
    Attr:
        __engine
        __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries on the current database session
        Return:
            returns a dictionary of __object
        """
        dct = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for i in query:
                key = "{}.{}".format(type(i).__name__, i.id)
                dct[key] = i

        else:
            classes = [State, City, User, Place, Review, Amenity]
            for i in classes:
                query = self.__session.query(i)
                for j in classes:
                    key = "{}.{}".format(type(j).__name__, j.id)
                    dct[key] = j
        return dct

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ initialize a new session"""
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
        Session = scoped_session(sessions)
        self.__session = Session()
