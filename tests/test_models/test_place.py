#!/usr/bin/python3
""" Test the place model"""
import datetime
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()
        self.place.name = "My First Model"
        self.place.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.place, Place))
        self.assertTrue(isinstance(self.place.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.place.created_at, dt))
        self.assertTrue(isinstance(self.place.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)

    def test_right_value(self):
        self.assertEqual(self.place.my_number, 89)
        self.assertEqual(self.place.name, "My First Model")
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)
        self.assertGreater(self.place.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        place_json = self.place.to_dict()
        self.assertIsNotNone(place_json.get("id"))
        self.assertIsNotNone(place_json.get("name"))
        self.assertIsNotNone(place_json.get("my_number"))
        self.assertIsNotNone(place_json.get("__class__"))
        self.assertIsNotNone(place_json.get("updated_at"))
        self.assertIsNotNone(place_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        place_json = self.place.to_dict()
        class_from_json = Place(**place_json)
        self.assertTrue(isinstance(class_from_json, Place))
        self.assertEqual(place_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(place_json.get('name'), name)
        self.assertEqual(place_json.get('my_number'), my_number)
        self.assertEqual(place_json.get('created_at'), formatted_created_at)
        self.assertEqual(place_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
