#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column, Integer
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')

    def cities(self):
        """returns a list of city elements"""
        dct = []
        val = models.storage.all(City)
        for i in list(val.values()):
            if i.state_id == self.id:
                dct.append(i)
        return dct
