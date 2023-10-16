#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_default_attributes(self):
        review = Review()

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        review = Review()

        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
