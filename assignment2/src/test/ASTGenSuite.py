import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_variable_declaration_000(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_variable_declaration_001(self):
        input = """bool a
        """
        expect = str(Program([VarDecl(Id("a"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_variable_declaration_002(self):
        input = """string a
        """
        expect = str(Program([VarDecl(Id("a"), StringType())]))
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_variable_declaration_003(self):
        input = """number a <- 1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_variable_declaration_004(self):
        input = """bool a <- true
        """
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_variable_declaration_005(self):
        input = """string a <- "Hello world"
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("Hello world"))]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_variable_declaration_006(self):
        input = """var a <- 1
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_variable_declaration_007(self):
        input = """dynamic a <- 1
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_variable_declaration_008(self):
        input = """var a <- 1
                dynamic b <- 1
                string a <- "Hello world"
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                              VarDecl(Id("b"), None, "dynamic", NumberLiteral(1.0)),
                              VarDecl(Id("a"), StringType(), None, StringLiteral("Hello world"))
                              ]))
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_variable_declaration_009(self):
        input = """number a[1] <- [1]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.0],NumberType()), None, ArrayLiteral([NumberLiteral(1.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test_variable_declaration_010(self):
        input = """number a[1] <- []
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.0],NumberType()), None, ArrayLiteral([]))]))
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_variable_declaration_010(self):
        input = """number a[2,2] <- [[11,12],[21,22]]
        """
        expect = str(Program([VarDecl(
                        Id("a"), 
                        ArrayType([2.0,2.0],
                        NumberType()),
                        None,
                        ArrayLiteral([
                            ArrayLiteral([
                                NumberLiteral(11.0),
                                NumberLiteral(12.0)]),
                            ArrayLiteral([
                                NumberLiteral(21.0),
                                NumberLiteral(22.0)])
                            ]))]))
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_variable_declaration_011(self):
        input = """func main() return 1
        """
        expect = str(Program([FuncDecl(
                        Id("main"), 
                        [],
                        Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 311))
        