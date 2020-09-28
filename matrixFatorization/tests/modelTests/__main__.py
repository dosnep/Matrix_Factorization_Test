import unittest

from matrixFatorization.tests.modelTests.ModelTest import ModelTest

def modelTestBuilder():
    # TestChains to Return
    testChainsBuilder = unittest.TestSuite()
    # Declare all unit test
    testsChainsObject = [ModelTest("test_description")]

    for obj in testsChainsObject:
        testChainsBuilder.addTest(obj)

    return testChainsBuilder

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(modelTestBuilder())