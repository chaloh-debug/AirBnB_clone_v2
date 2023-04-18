#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/amenity.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_str(self):
        """Test __str__ representation."""
        s = self.amenity.__str__()
        self.assertIn("[Amenity] ({})".format(self.amenity.id), s)
        self.assertIn("'id': '{}'".format(self.amenity.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.amenity.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.amenity.updated_at)), s)
        self.assertIn("'name': '{}'".format(self.amenity.name), s)

    def test_to_dict(self):
        """Test to_dict method."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(dict, type(amenity_dict))
        self.assertEqual(self.amenity.id, amenity_dict["id"])
        self.assertEqual("Amenity", amenity_dict["__class__"])
        self.assertEqual(self.amenity.created_at.isoformat(),
                         amenity_dict["created_at"])
        self.assertEqual(self.amenity.updated_at.isoformat(),
                         amenity_dict["updated_at"])
        self.assertEqual(self.amenity.name, amenity_dict["name"])

    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        old = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(old, self.amenity.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + self.amenity.id, f.read())


if __name__ == "__main__":
    unittest.main()
