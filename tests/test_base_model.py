#!/usr/bin/python3
import datetime
import uuid
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
        self.assertTrue(isinstance(self.my_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(self.my_model.updated_at, datetime.datetime))
        
    def test_value_is_set(self):
        self.assertIsNotNone(self.my_model.id)
        self.assertIsNotNone(self.my_model.created_at)
        self.assertIsNotNone(self.my_model.updated_at)

    def test_right_value(self):
        self.assertAlmostEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model.name, "My First Model")

