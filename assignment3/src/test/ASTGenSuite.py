import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a[2,2] <- [x,[x,x]]
        """
        expect = str(
            Program([
                VarDecl(
                    Id("a"),
                    ArrayType(
                        [2.0,2.0],
                        NumberType()
                        ),
                    None,
                    ArrayLiteral([
                        Id("x"),
                        ArrayLiteral([
                            Id("x"),
                            Id("x")
                        ])
                    ])
                    )
                ])
            )
        self.assertTrue(TestAST.test(input, expect, 300))
