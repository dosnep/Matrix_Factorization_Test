import unittest

from matrixFatorization.model.Model import Model


class ModelTest(unittest.TestCase):
    def setUp(self):
        self.model = Model(name="test", version=1.0)

    def test_description(self):
        self.assertEqual(self.model.description(), "name : test, version : 1.0")
