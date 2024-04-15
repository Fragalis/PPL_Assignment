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

    def test04(self):
        input = """func main() begin
        number a <- readNumber()
        bool b <- readBool()
        string c <- readString()
        var d <- a
        writeNumber(a)
        writeBool(b)
        writeString(c)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test05(self):
        input = """func main() begin
        number a <- readNumber()
        bool b <- readBool()
        string c <- readString()
        var d <- a
        dynamic e
        e <- b
        writeNumber(a)
        writeBool(b)
        writeString(c)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test06(self):
        input = """func main() begin
        number a[1] <- [1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test07(self):
        input = """func main() begin
        number a[1,1] <- [[1]]
        bool b[1,1] <- [[true]]
        string c[1,1] <- [["hello world"]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        
    def test08(self):
        input = """func main() begin
        number a[2,2] <- [[2,2],[2,2]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test09(self):
        input = """func main() begin
        bool a[1,1] <- [[true]]
        string b[1,1] <- [["hello world"]]
        string c[1,1] <- b
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test10(self):
        input = """func main() begin
        bool a[1,1] <- [[true]]
        string b[1,1] <- [["hello world"]]
        var c <- a
        dynamic d
        d <- a[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test11(self):
        input = """func main() begin
        number a <- 1
        bool a <- true
        end
        """
        expect = "Redeclared Variable: a)"
        self.assertTrue(TestChecker.test(input, expect, 411))
        