import unittest

from matrixFatorization.tests.modelTests.__main__ import modelTestBuilder

runner = unittest.TextTestRunner()
moduleTest = [modelTestBuilder()]

for obj in moduleTest:
    runner.run(obj)
