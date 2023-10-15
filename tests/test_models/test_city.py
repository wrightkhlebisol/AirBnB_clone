#!/usr/bin/python3
""" Test the city model """
import datetime
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()
        self.city.name = "My First Model"
        self.city.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.city, City))
        self.assertTrue(isinstance(self.city.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.city.created_at, dt))
        self.assertTrue(isinstance(self.city.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)

    def test_right_value(self):
        self.assertEqual(self.city.my_number, 89)
        self.assertEqual(self.city.name, "My First Model")
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)
        self.assertGreater(self.city.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        city_json = self.city.to_dict()
        self.assertIsNotNone(city_json.get("id"))
        self.assertIsNotNone(city_json.get("name"))
        self.assertIsNotNone(city_json.get("my_number"))
        self.assertIsNotNone(city_json.get("__class__"))
        self.assertIsNotNone(city_json.get("updated_at"))
        self.assertIsNotNone(city_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        city_json = self.city.to_dict()
        class_from_json = City(**city_json)
        self.assertTrue(isinstance(class_from_json, City))
        self.assertEqual(city_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(city_json.get('name'), name)
        self.assertEqual(city_json.get('my_number'), my_number)
        self.assertEqual(city_json.get('created_at'), formatted_created_at)
        self.assertEqual(city_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
