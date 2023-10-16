#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()
        self.storage.reload()

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(new_model, self.storage.all().values())

    def test_save(self):
        initial_count = len(self.storage.all())
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        self.assertEqual(len(reloaded_storage.all()), initial_count + 1)


if __name__ == '__main__':
    unittest.main()
