"""unnitest module for the file base_model.py"""
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Test module class"""

    def test_instatiation_attributes(self):
        """Test that an instance has all the required attributes"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, id))
        self.assertTrue(hasattr(obj1, created_at))
        self.assertTrue(hasattr(obj1, updated_at))
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj1.updated_at, datetime)
        self.assertIsInstance(obj1.created_at, datetime)

    def test_str(self):
        pass

    def test_to_dict(self):
        pass

    def test_save(self):
        pass
