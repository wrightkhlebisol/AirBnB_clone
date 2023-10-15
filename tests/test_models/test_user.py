#!/usr/bin/python3
""" Test the user model """
import datetime
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.name = "My First Model"
        self.user.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.user.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.user.created_at, dt))
        self.assertTrue(isinstance(self.user.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_right_value(self):
        self.assertEqual(self.user.my_number, 89)
        self.assertEqual(self.user.name, "My First Model")
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)
        self.assertGreater(self.user.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        user_json = self.user.to_dict()
        self.assertIsNotNone(user_json.get("id"))
        self.assertIsNotNone(user_json.get("name"))
        self.assertIsNotNone(user_json.get("my_number"))
        self.assertIsNotNone(user_json.get("__class__"))
        self.assertIsNotNone(user_json.get("updated_at"))
        self.assertIsNotNone(user_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        user_json = self.user.to_dict()
        class_from_json = User(**user_json)
        self.assertTrue(isinstance(class_from_json, User))
        self.assertEqual(user_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(user_json.get('name'), name)
        self.assertEqual(user_json.get('my_number'), my_number)
        self.assertEqual(user_json.get('created_at'), formatted_created_at)
        self.assertEqual(user_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
