#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_default_attributes(self):
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()

        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
