#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_default_attributes(self):
        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        city = City()

        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_inheritance(self):
        city = City()

        self.assertTrue(issubclass(City, BaseModel))

    def test_string_representation(self):
        city = City()
        city.state_id = "NY"
        city.name = "New York City"

        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()
