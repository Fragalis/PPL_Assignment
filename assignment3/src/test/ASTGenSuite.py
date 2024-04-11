import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """dynamic a <- [1]
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", ArrayLiteral([NumberLiteral(1.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 300))
