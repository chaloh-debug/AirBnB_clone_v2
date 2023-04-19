#!/usr/bin/python3
""" tests"""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import


class TestDBStorage(unittest.TestCase):
    '''DBStorage tests'''

    def test_pep8_DBStorage(self):
        """Test Pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def test_save(self):
        """Test save method."""
        st = State(name="Virginia")
        self.storage._DBStorage__session.add(st)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'Texas'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(st.id, query[0][0])
        cursor.close()

    def test_delete(self):
        """Test delete method."""
        st = State(name="New_York")
        self.storage._DBStorage__session.add(st)
        self.storage._DBStorage__session.commit()
        self.storage.delete(st)
        self.assertIn(st, list(self.storage._DBStorage__session.deleted))


if __name__ == "__main__":
    unittest.main()
