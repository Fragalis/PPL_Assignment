import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Expressions"""
        input = """not a ... -b + (c and d)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))