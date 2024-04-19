import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """        
        dynamic a
        a <- [[1, 2], [3, true]]
        func main() return
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
