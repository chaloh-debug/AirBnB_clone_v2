#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1028), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade='all, delete, delete-orphan')
        amenities = relationship("Amenity", backref="place_amenities",
                                 viewonly=False, secondary=place_amenity)

    else:
        def reviews(self):
            """ List of Review intsnces with Place_id"""
            from models import storage
            lists = []
            rvs = storage.all(Review)
            for rev in rvs.values():
                if rev.place_id == self.id:
                    lists.append(rev)
            return lists

        def amenities(self, arg):
            """method for adding an Amenity.id to the
                attribute amenity_ids.
            """
            if type(arg) is Amenity:
                Place.amenity_ids.append(arg.id)

        def amenities(self):
            """returns the list of Amenity instances
                based on the attribute amenity_ids that
                contains all Amenity.id linked to the Place
            """
            from models import storage
            amens = storage.all(Amenity)
            lists = []
            for amen in amens.values():
                if amen.id in self.amenity_ids:
                    lists.append(amen)
            return lists
