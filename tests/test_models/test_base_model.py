"""unnitest module for the file base_model.py"""
from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test module class"""

    def test_instatiation_attributes(self):
        """Test that an instance has all the required attributes"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, 'id'))
        self.assertTrue(hasattr(obj1, 'created_at'))
        self.assertTrue(hasattr(obj1, 'updated_at'))
        self.assertIsInstance(obj1.id, str)
        self.assertIsInstance(obj1.updated_at, datetime)
        self.assertIsInstance(obj1.created_at, datetime)

    def test_str(self):
        """
        Tests the __str__ method of BaseModel
        """
        obj = BaseModel()
        obj_str = obj.__str__()
        self.assertIn('BaseModel', obj_str)
        self.assertIn('({})'.format(obj.id), obj_str)
        self.assertIn(str(obj.__dict__), obj_str)
        self.assertIsInstance(obj_str, str)

    def test_to_dict(self):
        """
        Tests the to_dict() method of BaseModel
        """
        obj = BaseModel()
        obj.name = "My First Model"
        obj.number = 89
        obj_dict = obj.to_dict()

        self.assertIn('id', obj_dict)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIn('created_at', obj_dict)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(obj_dict['updated_at'], str)

        self.assertIn('name', obj_dict)
        self.assertEqual(obj_dict['name'], "My First Model")
        self.assertIn('number', obj_dict)
        self.assertEqual(obj_dict['number'], 89)

        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], obj.__class__.__name__)
        self.assertNotIn('__class__', obj.__dict__)

        for key in obj.__dict__:
            self.assertIn(key, obj_dict)

        obj_dict2 = obj.to_dict()
        self.assertEqual(obj_dict2, obj_dict)

    def test_save(self):
        """
        Test the object updated at time is updated when
        save is called.
        """
        basemodel = BaseModel()
        dict_1 = basemodel.to_dict()
        updated_at_value1 = basemodel.updated_at

        basemodel.save()
        dict_2 = basemodel.to_dict()
        updated_at_value2 = basemodel.updated_at

        self.assertIsInstance(updated_at_value1, datetime)
        self.assertIsInstance(updated_at_value1, datetime)
        self.assertNotEqual(updated_at_value1, updated_at_value2)
        self.assertNotEqual(dict_1['updated_at'], dict_2['updated_at'])

    def test__init__(self):
        """
        Test the constructor of a BaseModel object
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

        dictionary = {'size': 32, 'created_at': datetime.now().isoformat(),
                      'id': 1, 'updated_at': datetime.now().isoformat()}
        obj1 = BaseModel(**dictionary)

        for i in dictionary:
            self.assertTrue(hasattr(obj1, i))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

        dictionary['__class__'] = 'sample class'
        obj2 = BaseModel("Daniel", 2, **dictionary)
        self.assertNotEqual(obj2.__class__, 'sample class')
        self.assertFalse(hasattr(obj2, '2'))
        self.assertFalse(hasattr(obj2, 'Daniel'))
