import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test00(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test01(self):
        input = """func main() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test02(self):
        input = """func main() begin
        number a <- readNumber()
        bool b <- readBool()
        string c <- readString()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test03(self):
        input = """func main() begin
        number a <- readNumber()
        bool b <- readBool()
        string c <- readString()
        writeNumber(a)
        writeBool(b)
        writeString(c)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))
