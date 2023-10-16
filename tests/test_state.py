#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_default_attributes(self):
        state = State()

        self.assertEqual(state.name, "")

    def test_inheritance(self):
        state = State()

        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
