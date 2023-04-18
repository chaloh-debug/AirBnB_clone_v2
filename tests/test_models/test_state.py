#!/usr/bin/python3
""" """
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_to_dict(self):
        """Test to_dict method."""
        state_dict = self.state.to_dict()
        self.assertEqual(dict, type(state_dict))
        self.assertEqual(self.state.id, state_dict["id"])
        self.assertEqual("State", state_dict["__class__"])
        self.assertEqual(self.state.created_at.isoformat(),
                         state_dict["created_at"])
        self.assertEqual(self.state.updated_at.isoformat(),
                         state_dict["updated_at"])
        self.assertEqual(self.state.name, state_dict["name"])


if __name__ == "__main__":
    unittest.main()
