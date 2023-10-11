#!/usr/bin/python3
import datetime
import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.my_model.created_at, dt))
        self.assertTrue(isinstance(self.my_model.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.my_model.id)
        self.assertIsNotNone(self.my_model.created_at)
        self.assertIsNotNone(self.my_model.updated_at)

    def test_right_value(self):
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model.name, "My First Model")
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(old_updated_at, self.my_model.updated_at)
        self.assertGreater(self.my_model.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        my_model_json = self.my_model.to_dict()
        self.assertIsNotNone(my_model_json.get("id"))
        self.assertIsNotNone(my_model_json.get("name"))
        self.assertIsNotNone(my_model_json.get("my_number"))
        self.assertIsNotNone(my_model_json.get("__class__"))
        self.assertIsNotNone(my_model_json.get("updated_at"))
        self.assertIsNotNone(my_model_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        my_model_json = self.my_model.to_dict()
        new_class_from_json = BaseModel(**my_model_json)
        self.assertTrue(isinstance(new_class_from_json, BaseModel))
        self.assertEqual(my_model_json.get('id'), new_class_from_json.id)
        self.assertEqual(my_model_json.get('name'), new_class_from_json.name)
        self.assertEqual(my_model_json.get('my_number'), new_class_from_json.my_number)
        self.assertEqual(my_model_json.get('created_at'), new_class_from_json.created_at.isoformat())
        self.assertEqual(my_model_json.get('updated_at'), new_class_from_json.updated_at.isoformat())

    def test_exception(self):
        pass
