#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()

        self.assertEqual(amenity.name, "")

        amenity.name = "Swimming Pool"

        self.assertEqual(amenity.name, "Swimming Pool")

    def test_inheritance(self):
        amenity = Amenity()

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_string_representation(self):
        amenity = Amenity()
        amenity.name = "Gym"

        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)


if __name__ == '__main__':
    unittest.main()
