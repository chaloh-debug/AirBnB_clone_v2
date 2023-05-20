#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            '''
            returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
            '''
            cts = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cts.append(city)
            return cts
