#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        def cities(self):
            """returns a list of city elements"""
            dct = []
            elem = models.storage.all(City)
            for i in list(elem.values()):
                if i.state_id == self.id:
                    dct.append(i)
            return dct
