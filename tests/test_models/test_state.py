#!/usr/bin/python3
""" Test the state model """
import datetime
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()
        self.state.name = "My First Model"
        self.state.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.state, State))
        self.assertTrue(isinstance(self.state.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.state.created_at, dt))
        self.assertTrue(isinstance(self.state.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_right_value(self):
        self.assertEqual(self.state.my_number, 89)
        self.assertEqual(self.state.name, "My First Model")
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)
        self.assertGreater(self.state.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        state_json = self.state.to_dict()
        self.assertIsNotNone(state_json.get("id"))
        self.assertIsNotNone(state_json.get("name"))
        self.assertIsNotNone(state_json.get("my_number"))
        self.assertIsNotNone(state_json.get("__class__"))
        self.assertIsNotNone(state_json.get("updated_at"))
        self.assertIsNotNone(state_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        state_json = self.state.to_dict()
        class_from_json = State(**state_json)
        self.assertTrue(isinstance(class_from_json, State))
        self.assertEqual(state_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(state_json.get('name'), name)
        self.assertEqual(state_json.get('my_number'), my_number)
        self.assertEqual(state_json.get('created_at'), formatted_created_at)
        self.assertEqual(state_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
