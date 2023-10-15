#!/usr/bin/python3
"""Test the amenity model"""
import datetime
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "My First Model"
        self.amenity.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.amenity, Amenity))
        self.assertTrue(isinstance(self.amenity.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.amenity.created_at, dt))
        self.assertTrue(isinstance(self.amenity.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_right_value(self):
        self.assertEqual(self.amenity.my_number, 89)
        self.assertEqual(self.amenity.name, "My First Model")
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        amenity_json = self.amenity.to_dict()
        self.assertIsNotNone(amenity_json.get("id"))
        self.assertIsNotNone(amenity_json.get("name"))
        self.assertIsNotNone(amenity_json.get("my_number"))
        self.assertIsNotNone(amenity_json.get("__class__"))
        self.assertIsNotNone(amenity_json.get("updated_at"))
        self.assertIsNotNone(amenity_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        amenity_json = self.amenity.to_dict()
        class_from_json = Amenity(**amenity_json)
        self.assertTrue(isinstance(class_from_json, Amenity))
        self.assertEqual(amenity_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(amenity_json.get('name'), name)
        self.assertEqual(amenity_json.get('my_number'), my_number)
        self.assertEqual(amenity_json.get('created_at'), formatted_created_at)
        self.assertEqual(amenity_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
