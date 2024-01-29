import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """First program"""
        input0 = """func main() begin
                    end
                    """
        expect0 = "successful"
        self.assertTrue(TestParser.test(input0,expect0,200))
        """Assignments"""
        input1 = """func main() begin
                    number x <- 1
                    end"""
        expect1 = "successful"
        self.assertTrue(TestParser.test(input1,expect1,201))
        input2 = """func main() begin
                    bool x <- true
                    end"""
        expect2 = "successful"
        self.assertTrue(TestParser.test(input2,expect2,202))
        input3 = """func main() begin
                    string x <- "asdsad"
                    end"""
        expect3 = "successful"
        self.assertTrue(TestParser.test(input3,expect3,203))
        input4 = """func main() begin
                    var x <- variable
                    end"""
        expect4 = "successful"
        self.assertTrue(TestParser.test(input4,expect4,204))
        input5 = """func main() begin
                    dynamic x <- false
                    end"""
        expect5 = "successful"
        self.assertTrue(TestParser.test(input5,expect5,205))
        input6 = """func main() begin
                    number x[1,1,1] <- [[[[[[[[[]]]]]]]]]
                    end"""
        expect6 = "successful"
        self.assertTrue(TestParser.test(input6,expect6,206))
        input7 = """func main() begin
                    dynamic x[1,1,1] <- [[[[[[[[[]]]]]]]]]
                    end"""
        expect7 = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input7,expect7,207))
        input8 = """func main() begin
                    number x1 <- 1\nnumber x2 <- 2\nnumber x3 <- 3\nstring asdjn
                    bool x4 <- test()
                    end"""
        expect8 = "successful"
        self.assertTrue(TestParser.test(input8,expect8,208))
        input9 = """func main() begin
                    number x1 <- arr[1,2]
                    end"""
        expect9 = "successful"
        self.assertTrue(TestParser.test(input9,expect9,209))