#!/usr/bin/python3
""" Test the review model """
import datetime
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()
        self.review.name = "My First Model"
        self.review.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.review, Review))
        self.assertTrue(isinstance(self.review.id, str))
        dt = datetime.datetime
        self.assertTrue(isinstance(self.review.created_at, dt))
        self.assertTrue(isinstance(self.review.updated_at, dt))

    def test_value_is_set(self):
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)

    def test_right_value(self):
        self.assertEqual(self.review.my_number, 89)
        self.assertEqual(self.review.name, "My First Model")
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)
        self.assertGreater(self.review.updated_at, old_updated_at)

    def test_keys_exist_in_dict(self):
        review_json = self.review.to_dict()
        self.assertIsNotNone(review_json.get("id"))
        self.assertIsNotNone(review_json.get("name"))
        self.assertIsNotNone(review_json.get("my_number"))
        self.assertIsNotNone(review_json.get("__class__"))
        self.assertIsNotNone(review_json.get("updated_at"))
        self.assertIsNotNone(review_json.get("created_at"))

    def test_recreate_class_from_dict(self):
        review_json = self.review.to_dict()
        class_from_json = Review(**review_json)
        self.assertTrue(isinstance(class_from_json, Review))
        self.assertEqual(review_json.get('id'), class_from_json.id)
        name = class_from_json.name
        my_number = class_from_json.my_number
        formatted_created_at = class_from_json.created_at.isoformat()
        formatted_updated_at = class_from_json.updated_at.isoformat()

        self.assertEqual(review_json.get('name'), name)
        self.assertEqual(review_json.get('my_number'), my_number)
        self.assertEqual(review_json.get('created_at'), formatted_created_at)
        self.assertEqual(review_json.get('updated_at'), formatted_updated_at)

    def test_exception(self):
        pass
