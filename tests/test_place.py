#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_default_attributes(self):
        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        place = Place()

        self.assertTrue(issubclass(Place, BaseModel))

    def test_string_representation(self):
        place = Place()
        place.city_id = "city-123"
        place.name = "Cozy Cabin"

        expected_str = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected_str)


if __name__ == '__main__':
    unittest.main()
