#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column, Integer


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
