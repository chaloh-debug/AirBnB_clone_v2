#!/usr/bin/python3
""" """
import unittest
import os
from os import getenv
from models.place import Place
from models.base_model import BaseModel
import pep8


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/place.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes(self):
        """Check for attributes."""
        us = Place()
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "__tablename__"))
        self.assertTrue(hasattr(us, "city_id"))
        self.assertTrue(hasattr(us, "name"))
        self.assertTrue(hasattr(us, "description"))
        self.assertTrue(hasattr(us, "number_rooms"))
        self.assertTrue(hasattr(us, "number_bathrooms"))
        self.assertTrue(hasattr(us, "max_guest"))
        self.assertTrue(hasattr(us, "price_by_night"))
        self.assertTrue(hasattr(us, "latitude"))
        self.assertTrue(hasattr(us, "longitude"))

    def test_to_dict(self):
        """Test to_dict method."""
        place_dict = self.place.to_dict()
        self.assertEqual(dict, type(place_dict))
        self.assertEqual(self.place.id, place_dict["id"])
        self.assertEqual("Place", place_dict["__class__"])
        self.assertEqual(self.place.created_at.isoformat(),
                         place_dict["created_at"])
        self.assertEqual(self.place.updated_at.isoformat(),
                         place_dict["updated_at"])
        self.assertEqual(self.place.city_id, place_dict["city_id"])
        self.assertEqual(self.place.user_id, place_dict["user_id"])
        self.assertEqual(self.place.name, place_dict["name"])


if __name__ == "__main__":
    unittest.main()
