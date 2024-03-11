import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_variable_declaration_000(self):
        input = """
        """
        expect = str(Program([]))
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
        
    def test_function_declaration_001(self):
        input = """func main()
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_function_declaration_002(self):
        input = """func main(number a)
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(Id("a"),NumberType(),None,None)
        ],
        None)]))
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_function_declaration_003(self):
        input = """func main() return
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Return())]))
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_function_declaration_004(self):
        input = """func main() return 1
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_function_declaration_005(self):
        input = """func main(number a) return 1
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(Id("a"),NumberType(),None,None)
        ],
        Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_function_declaration_006(self):
        input = """func main(number a, bool b) return 1
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(Id("a"),NumberType(),None,None),
            VarDecl(Id("b"),BoolType(),None,None)
        ],
        Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_function_declaration_007(self):
        input = """func main(number a[1], bool b) return 1
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(
                Id("a"), 
                ArrayType(
                    [1.0],
                    NumberType()
                    ),
                None,
                None
                ),
            VarDecl(Id("b"),BoolType(),None,None)
        ],
        Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test_function_declaration_008(self):
        input = """func main(number a[1], bool b) begin
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(
                Id("a"), 
                ArrayType(
                    [1.0],
                    NumberType()
                    ),
                None,
                None
                ),
            VarDecl(Id("b"),BoolType(),None,None)
        ],
        Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 318))
    
    def test_function_declaration_009(self):
        input = """func main(number a[1], bool b) begin
        var c <- "Hello World"
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(
                Id("a"), 
                ArrayType(
                    [1.0],
                    NumberType()
                    ),
                None,
                None
                ),
            VarDecl(Id("b"),BoolType(),None,None)
        ],
        Block(
            [
                VarDecl(Id("c"), None, "var", StringLiteral("Hello World"))
            ]))]))
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test_function_declaration_010(self):
        input = """func main(number a[1], bool b) begin
        var c <- "Hello World"
        return c
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [
            VarDecl(
                Id("a"), 
                ArrayType(
                    [1.0],
                    NumberType()
                    ),
                None,
                None
                ),
            VarDecl(Id("b"),BoolType(),None,None)
        ],
        Block(
            [
                VarDecl(Id("c"), None, "var", StringLiteral("Hello World")),
                Return(Id("c"))
            ]))]))
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_expression_001(self):
        input = """number a <- a ... b
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        BinaryOp("...", Id("a"), Id("b"))
        )]))
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_expression_002(self):
        input = """number a <- a ... b == c
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        BinaryOp(
            "...",
            Id("a"),
            BinaryOp(
                "==",
                Id("b"), 
                Id("c")
                )
            )
        )]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_expression_003(self):
        input = """number a <- a and b != c or d
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        BinaryOp(
            "!=",
            BinaryOp(
                "and",
                Id("a"), 
                Id("b")
                ),
            BinaryOp(
                "or",
                Id("c"), 
                Id("d")
                )
            )
        )]))
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_expression_004(self):
        input = """number a <- a * b + not c
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        BinaryOp(
            "+",
            BinaryOp(
                "*",
                Id("a"), 
                Id("b")
                ),
            UnaryOp(
                "not",
                Id("c") 
                )
            )
        )]))
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_expression_005(self):
        input = """number a <- not - a
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        UnaryOp(
            "not",
            UnaryOp(
                "-",
                Id("a") 
                )
            )
        )]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_expression_006(self):
        input = """number a <- a * (b + c) * d
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        BinaryOp(
            "*",
            BinaryOp(
                "*",
                Id("a"), 
                BinaryOp(
                    "+",
                    Id("b"), 
                    Id("c")
                    )
                ),
            Id("d")
            )
        )]))
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_expression_007(self):
        input = """number a <- a[1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        ArrayCell(
            Id("a"),
            [NumberLiteral(1.0)]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_expression_008(self):
        input = """number a <- a[b[c+d]]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        ArrayCell(
            Id("a"),
            [
                ArrayCell(
                    Id("b"),
                    [BinaryOp("+",Id("c"),Id("d"))]
                )
            ]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_expression_009(self):
        input = """number a <- a()[1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        ArrayCell(
            CallExpr(
                Id("a"),
                []
            ),
            [NumberLiteral(1.0)]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_expression_010(self):
        input = """number a <- a(arg1,arg2)[1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        ArrayCell(
            CallExpr(
                Id("a"),
                [
                    Id("arg1"),
                    Id("arg2")
                ]
            ),
            [NumberLiteral(1.0)]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test_expression_011(self):
        input = """number a <- a(arg1[1], arg2 + arg3)[1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        ArrayCell(
            CallExpr(
                Id("a"),
                [
                    ArrayCell(
                        Id("arg1"),
                        [NumberLiteral(1.0)]
                    ),
                    BinaryOp("+", Id("arg2"), Id("arg3"))
                ]
            ),
            [NumberLiteral(1.0)]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_expression_012(self):
        input = """number a <- caller(x)
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        NumberType(),
        None,
        CallExpr(
            Id("caller"),
            [Id("x")]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_expression_013(self):
        input = """var a <- caller(x[1,1])[1,1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        None,
        "var",
        ArrayCell(
            CallExpr(
                Id("caller"),
                [
                    ArrayCell(
                        Id("x"),
                        [
                            NumberLiteral(1.0),
                            NumberLiteral(1.0)
                        ]
                    ),
                ]
            ),
            [
                NumberLiteral(1.0),
                NumberLiteral(1.0)
            ]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_expression_014(self):
        input = """var a <- a[1] * b(c,"strlit")[1] + d
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        None,
        "var",
        BinaryOp(
            "+",
            BinaryOp(
                "*",
                ArrayCell(
                    Id("a"),
                    [
                        NumberLiteral(1.0)
                    ]
                ),
                ArrayCell(
                    CallExpr(
                        Id("b"),
                        [
                            Id("c"),
                            StringLiteral("strlit")
                        ]
                    ),
                    [
                        NumberLiteral(1.0)
                    ]
                )
                ),
            Id("d")
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_expression_015(self):
        input = """var a <- a[a[1],1]
        """
        expect = str(
Program([
    VarDecl(
        Id("a"), 
        None,
        "var",
        ArrayCell(
            Id("a"),
            [
                ArrayCell(
                    Id("a"),
                    [
                        NumberLiteral(1.0)
                    ]
                ),
                NumberLiteral(1.0)
            ]
        )
        )]))
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test_assignment_statement_001(self):
        input = """func main () begin
        a <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block(
            [
                Assign(Id("a"), NumberLiteral(1.0))
            ]
        )
    )]))
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_assignment_statement_002(self):
        input = """func main () begin
        a <- b
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block(
            [
                Assign(Id("a"), Id("b"))
            ]
        )
    )]))
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_assignment_statement_003(self):
        input = """func main() begin
        a <- a[1] * b(c,"strlit")[1] + d
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            Assign(
                Id("a"),            
                BinaryOp(
                    "+",
                    BinaryOp(
                        "*",
                        ArrayCell(
                            Id("a"),
                            [
                                NumberLiteral(1.0)
                            ]
                        ),
                        ArrayCell(
                            CallExpr(
                                Id("b"),
                                [
                                    Id("c"),
                                    StringLiteral("strlit")
                                ]
                            ),
                            [
                                NumberLiteral(1.0)
                            ]
                        )
                        ),
                    Id("d")
                    )
                )
            ])
        )
    ]))
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_assignment_statement_004(self):
        input = """func a() begin
        a[1] <- a[a[1],1]
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            Assign(
                ArrayCell(
                    Id("a"),
                    [
                        NumberLiteral(1.0)
                    ]
                ),            
                ArrayCell(
                    Id("a"),
                    [
                        ArrayCell(
                            Id("a"),
                            [NumberLiteral(1.0)]
                        ),
                        NumberLiteral(1.0)
                    ]
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test_assignment_statement_005(self):
        input = """func a() begin
        a[1] <- call()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            Assign(
                ArrayCell(
                    Id("a"),
                    [
                        NumberLiteral(1.0)
                    ]
                ),
                CallExpr(
                    Id("call"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_block_statement_001(self):
        input = """func a() begin
        begin
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            Block([
            ])
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_block_statement_002(self):
        input = """func a() begin
        number a <- 1
        begin
        number b <- 2
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            Block([
                VarDecl(Id("b"), NumberType(), None, NumberLiteral(2.0))
            ])
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_block_statement_003(self):
        input = """func a() begin
        number a <- 1
        begin
        a <- 2
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            Block([
                Assign(Id("a"), NumberLiteral(2.0))
            ])
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test_block_statement_004(self):
        input = """func a() begin
        number a <- 1
        begin
        a <- 2
        end
        a <- arr[1] + 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("a"),
        [],
        Block([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            Block([
                Assign(Id("a"), NumberLiteral(2.0))
            ]),
            Assign(
                Id("a"),
                BinaryOp(
                    "+",
                    ArrayCell(
                        Id("arr"),
                        [NumberLiteral(1.0)]
                    ),
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_block_statement_005(self):
        input = """func main() begin
        number a <- 1
        begin
        a <- a(1,1)[1]
        end
        begin
        a <- arr[1] + 1
        end
        a <- a
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)),
            Block([
                Assign(
                    Id("a"), 
                    ArrayCell(
                        CallExpr(
                            Id("a"),
                            [
                                NumberLiteral(1.0),
                                NumberLiteral(1.0)
                            ]
                        ),
                        [
                            NumberLiteral(1.0)
                        ]
                    )
                )
            ]),
            Block([
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        ArrayCell(
                            Id("arr"),
                            [NumberLiteral(1.0)]
                        ),
                        NumberLiteral(1.0)
                    )
                )  
            ]),
            Assign(Id("a"), Id("a"))
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_for_statement_001(self):
        input = """func main() begin
        for i until i by i number a
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                VarDecl(
                    Id("a"),
                    NumberType(),
                    None,
                    None
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_for_statement_002(self):
        input = """func main() begin
        for i until i by i number a <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                VarDecl(
                    Id("a"),
                    NumberType(),
                    None,
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_for_statement_003(self):
        input = """func main() begin
        for i until i by i a <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Assign(
                    Id("a"),
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_for_statement_004(self):
        input = """func main() begin
        for i until i by i break
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Break()
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_for_statement_005(self):
        input = """func main() begin
        for i until i by i continue
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Continue()
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_for_statement_006(self):
        input = """func main() begin
        for i until i by i return
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Return(None)
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_for_statement_007(self):
        input = """func main() begin
        for i until i by i return i
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Return(Id("i"))
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_for_statement_008(self):
        input = """func main() begin
        for i until i by i call()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                CallStmt(
                    Id("call"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_for_statement_009(self):
        input = """func main() begin
        for i until i by i call(i)
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                CallStmt(
                    Id("call"),
                    [
                        Id("i")
                    ]
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_for_statement_010(self):
        input = """func main() begin
        for i until i by i call(i,i(i)[i])
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                CallStmt(
                    Id("call"),
                    [
                        Id("i"),
                        ArrayCell(
                            CallExpr(
                                Id("i"),
                                [
                                    Id("i")
                                ]
                            ),
                            [
                                Id("i")
                            ]
                        )
                    ]
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_for_statement_011(self):
        input = """func main() begin
        for i until i by i begin
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_for_statement_012(self):
        input = """func main() begin
        for i until i by i begin
        number x
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    VarDecl(
                        Id("x"),
                        NumberType(),
                        None,
                        None
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_for_statement_013(self):
        input = """func main() begin
        for i until i by i begin
        number x <- 1
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    VarDecl(
                        Id("x"),
                        NumberType(),
                        None,
                        NumberLiteral(1.0)
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_for_statement_014(self):
        input = """func main() begin
        for i until i by i begin
        x <- 1
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    Assign(
                        Id("x"),
                        NumberLiteral(1.0)
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_for_statement_015(self):
        input = """func main() begin
        for i until i by i begin
        call(i)
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    CallStmt(
                        Id("call"),
                        [
                            Id("i")
                        ]
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test_for_statement_016(self):
        input = """func main() begin
        for i until i by i for j until j by j begin
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                For(
                    Id("j"),
                    Id("j"),
                    Id("j"),
                    Block([])
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test_for_statement_017(self):
        input = """func main() begin
        for i until i by i begin
        end
        for j until j by j begin
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([])
            ),
            For(
                Id("j"),
                Id("j"),
                Id("j"),
                Block([])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 362))
        
    def test_for_statement_018(self):
        input = """func main() begin
        for i until i by i begin
            return caller(1)
        end
        for j until j by j begin
            return caller(1)[1]
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    Return(
                        CallExpr(
                            Id("caller"),
                            [
                                NumberLiteral(1.0)
                            ]
                        )
                    )
                ])
            ),
            For(
                Id("j"),
                Id("j"),
                Id("j"),
                Block([
                    Return(
                        ArrayCell(
                            CallExpr(
                                Id("caller"),
                                [
                                    NumberLiteral(1.0)
                                ]
                            ),
                            [
                                NumberLiteral(1.0)
                            ]
                        )
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test_for_statement_019(self):
        input = """func main() begin
        for i until i by i begin
            dynamic arr <- 1
            for k until k by k begin
            return caller(1)
            end
        end
        for j until j by j begin
            return caller(1)[1]
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            For(
                Id("i"),
                Id("i"),
                Id("i"),
                Block([
                    VarDecl(
                        Id("arr"),
                        None,
                        "dynamic",
                        NumberLiteral(1.0)
                    ),
                    For(
                        Id("k"),
                        Id("k"),
                        Id("k"),
                        Block([
                            Return(
                                CallExpr(
                                    Id("caller"),
                                    [
                                        NumberLiteral(1.0)
                                    ]
                                )
                            )
                        ])
                    )
                ])
            ),
            For(
                Id("j"),
                Id("j"),
                Id("j"),
                Block([
                    Return(
                        ArrayCell(
                            CallExpr(
                                Id("caller"),
                                [
                                    NumberLiteral(1.0)
                                ]
                            ),
                            [
                                NumberLiteral(1.0)
                            ]
                        )
                    )
                ])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test_if_statement_001(self):
        input = """func main() begin
        if (i = 1) i <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                Assign(
                    Id("i"),
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test_simple_if_statement_001(self):
        input = """func main() begin
        if (i = 1) i <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                Assign(
                    Id("i"),
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_simple_if_statement_002(self):
        input = """func main() begin
        if (i = 1) number i <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                VarDecl(
                    Id("i"),
                    NumberType(),
                    None,
                    NumberLiteral(1.0)
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test_simple_if_statement_003(self):
        input = """func main() begin
        if (i = 1) return
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                Return()
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test_simple_if_statement_004(self):
        input = """func main() begin
        if (i = 1) return callee(1)
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                Return(
                    CallExpr(
                        Id("callee"),
                        [
                            NumberLiteral(1.0)
                        ]
                    )
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test_simple_if_statement_005(self):
        input = """func main() begin
        if (i = 1) begin
        end
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                Block([])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test_simple_if_statement_006(self):
        input = """func main() begin
        if (i = 1) for i until i by i i <- 1
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                For(
                    Id("i"),
                    Id("i"),
                    Id("i"),
                    Assign(
                        Id("i"),
                        NumberLiteral(1.0)
                    )
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test_simple_if_statement_007(self):
        input = """func main() begin
        if (i = 1) if_stmt()
        else else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                CallStmt(
                    Id("if_stmt"),
                    []
                ),
                [],
                CallStmt(
                    Id("else_stmt"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test_simple_if_statement_008(self):
        input = """func main() begin
        if (i = 1) if_stmt()
        elif (i = 2) elif_1_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                CallStmt(
                    Id("if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(2.0)
                        ),
                        CallStmt(
                            Id("elif_1_stmt"),
                            []
                        )
                    ))
                ],
                None
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_simple_if_statement_009(self):
        input = """func main() begin
        if (i = 1) if_stmt()
        elif (i = 2) elif_1_stmt()
        else else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                CallStmt(
                    Id("if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(2.0)
                        ),
                        CallStmt(
                            Id("elif_1_stmt"),
                            []
                        )
                    ))
                ],
                CallStmt(
                    Id("else_stmt"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test_simple_if_statement_010(self):
        input = """func main() begin
        if (i = 1) if_stmt()
        elif (i = 2) elif_1_stmt()
        elif (i = 3) elif_2_stmt()
        else else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(1.0)
                ),
                CallStmt(
                    Id("if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(2.0)
                        ),
                        CallStmt(
                            Id("elif_1_stmt"),
                            []
                        )
                    )),
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(3.0)
                        ),
                        CallStmt(
                            Id("elif_2_stmt"),
                            []
                        )
                    ))
                ],
                CallStmt(
                    Id("else_stmt"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test_complex_if_statement_001(self):
        input = """func main() begin
        if (i = 11) first_if_stmt()
        if (i = 21) second_if_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(11.0)
                ),
                CallStmt(
                    Id("first_if_stmt"),
                    []
                ),
                [],
                None
            ),
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(21.0)
                ),
                CallStmt(
                    Id("second_if_stmt"),
                    []
                ),
                [],
                None
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test_complex_if_statement_002(self):
        input = """func main() begin
        if (i = 11) first_if_stmt()
        if (i = 21) second_if_stmt()
        elif (i = 22) if2_elif_1_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(11.0)
                ),
                CallStmt(
                    Id("first_if_stmt"),
                    []
                ),
                [],
                None
            ),
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(21.0)
                ),
                CallStmt(
                    Id("second_if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(22.0)
                        ),
                        CallStmt(
                            Id("if2_elif_1_stmt"),
                            []
                        )
                    ))
                ],
                None
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_complex_if_statement_002(self):
        input = """func main() begin
        if (i = 11) first_if_stmt()
        elif (i = 12) if1_elif_1_stmt()
        if (i = 21) second_if_stmt()
        elif (i = 22) if2_elif_1_stmt()
        else if2_else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(11.0)
                ),
                CallStmt(
                    Id("first_if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(12.0)
                        ),
                        CallStmt(
                            Id("if1_elif_1_stmt"),
                            []
                        )
                    ))    
                ],
                None
            ),
            If(
                BinaryOp(
                    "=",
                    Id("i"),
                    NumberLiteral(21.0)
                ),
                CallStmt(
                    Id("second_if_stmt"),
                    []
                ),
                [
                    tuple((
                        BinaryOp(
                            "=",
                            Id("i"),
                            NumberLiteral(22.0)
                        ),
                        CallStmt(
                            Id("if2_elif_1_stmt"),
                            []
                        )
                    ))
                ],
                CallStmt(
                    Id("if2_else_stmt"),
                    []
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test_complex_if_statement_003(self):
        input = """func main() begin
        if (i = 11) begin
        first_if_stmt()
        if (i = 21) first_if_if_stmt()
        elif (i = 22) first_if_elif_1_stmt()
        end
        else if1_else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("main"),
        [],
        Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                Block([
                    CallStmt(Id("first_if_stmt"),[]),
                    If(
                        BinaryOp("=",Id("i"),NumberLiteral(21.0)),
                        CallStmt(Id("first_if_if_stmt"),[]),
                        [
                            tuple((
                                BinaryOp("=",Id("i"),NumberLiteral(22.0)),
                                CallStmt(Id("first_if_elif_1_stmt"),[])
                            ))
                        ],
                        None
                    )
                ]),
                [],
                CallStmt(Id("if1_else_stmt"),[])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_complex_if_statement_004(self):
        input = """func main() begin
        if (i = 11) if (i = 21) stmt()
        elif (i = 22) stmt()
        else if1_else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(21.0)),
                    CallStmt(Id("stmt"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),NumberLiteral(22.0)),
                            CallStmt(Id("stmt"),[])
                        ))
                    ],
                    CallStmt(Id("if1_else_stmt"),[])
                )
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test_complex_if_statement_005(self):
        input = """func main() begin
        if (i = 11) if (i = 21) stmt()
        else if_2_else_stmt()
        else if_1_else_stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(21.0)),
                    CallStmt(Id("stmt"),[]),
                    [],
                    CallStmt(Id("if_2_else_stmt"),[])
                ),
                [],
                CallStmt(Id("if_1_else_stmt"),[])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test_complex_if_statement_006(self):
        input = """func main() begin
        if (i = 1) if (i = 11) s11()
        elif (i = 12) if (i = 121) s121()
        elif (i = 122) s122()
        else s12x()
        else s1x()
        else sx()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(1.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                    CallStmt(Id("s11"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),NumberLiteral(12.0)),
                            If(
                                BinaryOp("=",Id("i"),NumberLiteral(121.0)),
                                CallStmt(Id("s121"),[]),
                                [
                                    tuple((
                                        BinaryOp("=",Id("i"),NumberLiteral(122.0)),
                                        CallStmt(Id("s122"),[])
                                    ))
                                ],
                                CallStmt(Id("s12x"),[]),
                            )
                        ))
                    ],
                    CallStmt(Id("s1x"),[])
                ),
                [],
                CallStmt(Id("sx"),[])
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_complex_if_statement_007(self):
        input = """func main() begin
        if (i = 1) 
            if (i = 11) s11()
            elif (i = 12) 
                if (i = 121) s121()
                elif (i = 122) s122()
                else s12x()
            else s1x()
        elif (i = 2)
            if (i = 21) s21()            
            else s2x()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(1.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                    CallStmt(Id("s11"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),NumberLiteral(12.0)),
                            If(
                                BinaryOp("=",Id("i"),NumberLiteral(121.0)),
                                CallStmt(Id("s121"),[]),
                                [
                                    tuple((
                                        BinaryOp("=",Id("i"),NumberLiteral(122.0)),
                                        CallStmt(Id("s122"),[])
                                    ))
                                ],
                                CallStmt(Id("s12x"),[]),
                            )
                        ))
                    ],
                    CallStmt(Id("s1x"),[])
                ),
                [
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(2.0)),
                        If(
                            BinaryOp("=",Id("i"),NumberLiteral(21.0)),
                            CallStmt(Id("s21"),[]),
                            [],
                            CallStmt(Id("s2x"),[])
                        )
                    ))
                ],
                None
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_complex_if_statement_008(self):
        input = """func main() begin
        if (i = 1) 
            if (i = 11) stmt()
            elif (i = 12) stmt()
            else stmt()
        elif (i = 2)
            if (i = 21) stmt()
            elif (i = 22) stmt()
            else stmt()
        else
            if (i = x1) stmt()
            elif (i = x2) stmt()
            else stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(1.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                    CallStmt(Id("stmt"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),NumberLiteral(12.0)),
                            CallStmt(Id("stmt"),[])
                        ))
                    ],
                    CallStmt(Id("stmt"),[])
                ),
                [
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(2.0)),
                        If(
                            BinaryOp("=",Id("i"),NumberLiteral(21.0)),
                            CallStmt(Id("stmt"),[]),
                            [
                                tuple((
                                    BinaryOp("=",Id("i"),NumberLiteral(22.0)),
                                    CallStmt(Id("stmt"),[])
                                ))
                            ],
                            CallStmt(Id("stmt"),[])
                        ),
                    ))
                ],
                If(
                    BinaryOp("=",Id("i"),Id("x1")),
                    CallStmt(Id("stmt"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),Id("x2")),
                            CallStmt(Id("stmt"),[])
                        ))
                    ],
                    CallStmt(Id("stmt"),[])
                ),
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test_complex_if_statement_009(self):
        input = """func main() begin
        if (i = 1) 
            if (i = 11) stmt()
            elif (i = 12) stmt()
            else stmt()
        elif (i = 2) stmt()
        elif (i = 3) stmt()
        elif (i = 4) stmt()
        else
            if (i = x1) stmt()
            elif (i = x2) stmt()
            else stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(1.0)),
                If(
                    BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                    CallStmt(Id("stmt"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),NumberLiteral(12.0)),
                            CallStmt(Id("stmt"),[])
                        ))
                    ],
                    CallStmt(Id("stmt"),[])
                ),
                [
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(2.0)),
                        CallStmt(Id("stmt"),[])
                    )),
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(3.0)),
                        CallStmt(Id("stmt"),[])
                    )),
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(4.0)),
                        CallStmt(Id("stmt"),[])
                    ))
                ],
                If(
                    BinaryOp("=",Id("i"),Id("x1")),
                    CallStmt(Id("stmt"),[]),
                    [
                        tuple((
                            BinaryOp("=",Id("i"),Id("x2")),
                            CallStmt(Id("stmt"),[])
                        ))
                    ],
                    CallStmt(Id("stmt"),[])
                ),
            )
        ])
    )
])  
)
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test_complex_if_statement_010(self):
        input = """func main() begin
        if (i = 1) 
        begin
            if (i = 11) stmt()
            elif (i = 12) stmt()
            elif (i = 13) stmt()
        end
        elif (i = 14) stmt()
        elif (i = 2) stmt()
        elif (i = 3) stmt()
        elif (i = 4) stmt()
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
            If(
                BinaryOp("=",Id("i"),NumberLiteral(1.0)),
                Block([
                    If(
                        BinaryOp("=",Id("i"),NumberLiteral(11.0)),
                        CallStmt(Id("stmt"),[]),
                        [
                            tuple((
                                BinaryOp("=",Id("i"),NumberLiteral(12.0)),
                                CallStmt(Id("stmt"),[])
                            )),
                            tuple((
                                BinaryOp("=",Id("i"),NumberLiteral(13.0)),
                                CallStmt(Id("stmt"),[])
                            ))
                        ],
                        None
                    )
                ]),
                [
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(14.0)),
                        CallStmt(Id("stmt"),[])
                    )),
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(2.0)),
                        CallStmt(Id("stmt"),[])
                    )),
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(3.0)),
                        CallStmt(Id("stmt"),[])
                    )),
                    tuple((
                        BinaryOp("=",Id("i"),NumberLiteral(4.0)),
                        CallStmt(Id("stmt"),[])
                    ))
                ],
                None
            )
        ])
    )
])
)
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_program_001(self):
        input = """func main() begin
        ## Read Number
        number x <- readNumber()
        ## Write Number
        writeNumber(x)
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(
            Id("x"),
            NumberType(),
            None,
            CallExpr(
                Id("readNumber"),
                []
            )
        ),
        CallStmt(
            Id("writeNumber"),
            [Id("x")]
        )
    ])
    )
])
        )
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_program_002(self):
        input = """func main() begin
        ## Read Number
        number x <- readNumber()
        number y <- readNumber()
        ## Write sum of x and y
        writeNumber(x + y)
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(
            Id("x"),
            NumberType(),
            None,
            CallExpr(
                Id("readNumber"),
                []
            )
        ),
        VarDecl(
            Id("y"),
            NumberType(),
            None,
            CallExpr(
                Id("readNumber"),
                []
            )
        ),
        CallStmt(
            Id("writeNumber"),
            [BinaryOp("+",Id("x"),Id("y"))]
        )
    ])
    )
])
        )
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_program_003(self):
        input = """func main() begin
        ## Read Number
        number x <- readNumber()
        var sum <- 0
        for i until i > x by 1 begin
            sum <- sum + i
        end
        writeNumber(sum)
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(
            Id("x"),
            NumberType(),
            None,
            CallExpr(
                Id("readNumber"),
                []
            )
        ),
        VarDecl(
            Id("sum"),
            None,
            "var",
            NumberLiteral(0.0)
        ),
        For(
            Id("i"),
            BinaryOp(">",Id("i"),Id("x")),
            NumberLiteral(1.0),
            Block([
                Assign(
                    Id("sum"),
                    BinaryOp("+",Id("sum"),Id("i"))
                )
            ])
        ),
        CallStmt(
            Id("writeNumber"),
            [Id("sum")]
        )
    ])
    )
])
        )
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_program_004(self):
        input = """func main() begin
        ## Read Number
        number x[5] <- [1,2,3,4,5]
        var sum <- 0
        for i until i > x by 1 begin
            sum <- sum + x[i]
        end
        writeNumber(sum)
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(
            Id("x"),
            ArrayType([5.0], NumberType()),
            None,
            ArrayLiteral([
                NumberLiteral(1.0),
                NumberLiteral(2.0),
                NumberLiteral(3.0),
                NumberLiteral(4.0),
                NumberLiteral(5.0)
            ])
        ),
        VarDecl(
            Id("sum"),
            None,
            "var",
            NumberLiteral(0.0)
        ),
        For(
            Id("i"),
            BinaryOp(">",Id("i"),Id("x")),
            NumberLiteral(1.0),
            Block([
                Assign(
                    Id("sum"),
                    BinaryOp("+",Id("sum"),ArrayCell(Id("x"),[Id("i")]))
                )
            ])
        ),
        CallStmt(
            Id("writeNumber"),
            [Id("sum")]
        )
    ])
    )
])
        )
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test_program_005(self):
        input = """func main() begin
        ## Read Number
        number x[10]
        for i until i > 10 by 1 begin
            x[i] <- readNumber()
        end
        for i until i > 10 by 1 begin
            if (x[i] % 3 = 0) writeString("Troll")
            if (x[i] % 5 = 0) writeString("Face")
        end
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(
            Id("x"),
            ArrayType([10.0], NumberType()),
            None,
            None
        ),
        For(
            Id("i"),
            BinaryOp(">",Id("i"),NumberLiteral(10.0)),
            NumberLiteral(1.0),
            Block([
                Assign(
                    ArrayCell(Id("x"),[Id("i")]),
                    CallExpr(Id("readNumber"),[])
                )
            ])
        ),
        For(
            Id("i"),
            BinaryOp(">",Id("i"),NumberLiteral(10.0)),
            NumberLiteral(1.0),
            Block([
                If(
                    BinaryOp(
                        "=",
                        BinaryOp("%",ArrayCell(Id("x"),[Id("i")]),NumberLiteral(3.0)),
                        NumberLiteral(0.0)
                    ),
                    CallStmt(Id("writeString"),[StringLiteral("Troll")])
                ),
                If(
                    BinaryOp(
                        "=",
                        BinaryOp("%",ArrayCell(Id("x"),[Id("i")]),NumberLiteral(5.0)),
                        NumberLiteral(0.0)
                    ),
                    CallStmt(Id("writeString"),[StringLiteral("Face")])
                )
            ])
        ),
    ])
    )
])
)
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test_program_006(self):
        input = """number num <- 0
        func inc() begin
        num <- num + 1
        return num
        end
        func main() begin
        for i until i = 10 by 1 inc()
        writeNumber(num)
        end
        """
        expect = str(
Program([
    VarDecl(Id("num"),NumberType(),None,NumberLiteral(0.0)),
    FuncDecl(Id("inc"),[],Block([
        Assign(Id("num"),BinaryOp("+",Id("num"),NumberLiteral(1.0))),
        Return(Id("num"))
    ])),
    FuncDecl(Id("main"),[],Block([
        For(
            Id("i"),
            BinaryOp("=",Id("i"),NumberLiteral(10.0)),
            NumberLiteral(1.0),
            CallStmt(Id("inc"),[])    
        ),
        CallStmt(Id("writeNumber"),[Id("num")])
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test_program_007(self):
        input = """number num <- 0
        func inc() begin
        num <- num + 1
        return num
        end
        func main() begin
        var sum <- 0
        for i until i = 10 by 1 sum <- sum + inc()*inc()
        writeNumber(sum)
        end
        """
        expect = str(
Program([
    VarDecl(Id("num"),NumberType(),None,NumberLiteral(0.0)),
    FuncDecl(Id("inc"),[],Block([
        Assign(Id("num"),BinaryOp("+",Id("num"),NumberLiteral(1.0))),
        Return(Id("num"))
    ])),
    FuncDecl(Id("main"),[],Block([
        VarDecl(Id("sum"),None,"var",NumberLiteral(0.0)),
        For(
            Id("i"),
            BinaryOp("=",Id("i"),NumberLiteral(10.0)),
            NumberLiteral(1.0),
            Assign(
                Id("sum"),
                BinaryOp(
                    "+",
                    Id("sum"),
                    BinaryOp("*",CallExpr(Id("inc"),[]),CallExpr(Id("inc"),[]))
                )
            )    
        ),
        CallStmt(Id("writeNumber"),[Id("sum")])
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test_program_008(self):
        input = """func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main() begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1,num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = str(
Program([
    FuncDecl(
        Id("areDivisors"),
        [
            VarDecl(Id("num1"),NumberType()),
            VarDecl(Id("num2"),NumberType())
        ],
        Return(
            BinaryOp("or",
                BinaryOp("=",
                    BinaryOp("%",Id("num1"),Id("num2")),
                    NumberLiteral(0.0)
                ),
                BinaryOp("=",
                    BinaryOp("%",Id("num2"),Id("num1")),
                    NumberLiteral(0.0)
                )
            )
        )
    ),
    FuncDecl(Id("main"),[],Block([
        VarDecl(Id("num1"),None,"var",CallExpr(Id("readNumber"),[])),
        VarDecl(Id("num2"),None,"var",CallExpr(Id("readNumber"),[])),
        If(
            CallExpr(Id("areDivisors"),[Id("num1"),Id("num2")]),
            CallStmt(Id("writeString"),[StringLiteral("Yes")]),
            [],
            CallStmt(Id("writeString"),[StringLiteral("No")])
        )
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_program_009(self):
        input = """func isPrime(number x)
        func main() begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        func isPrime(number x) begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x/2 by 1 begin
        if (x % i = 0) return false
        end
        return true
        end
        """
        expect = str(
Program([
    FuncDecl(Id("isPrime"),[VarDecl(Id("x"),NumberType())],None),
    FuncDecl(Id("main"),[],Block([
        VarDecl(Id("x"),NumberType(),None,CallExpr(Id("readNumber"),[])),
        If(
            CallExpr(Id("isPrime"),[Id("x")]),
            CallStmt(Id("writeString"),[StringLiteral("Yes")]),
            [],
            CallStmt(Id("writeString"),[StringLiteral("No")])
        )
    ])),
    FuncDecl(Id("isPrime"),[VarDecl(Id("x"),NumberType())],Block([
        If(
            BinaryOp("<=",Id("x"),NumberLiteral(1.0)),
            Return(BooleanLiteral(False))
        ),
        VarDecl(Id("i"),None,"var",NumberLiteral(2.0)),
        For(
            Id("i"),
            BinaryOp(
                ">",
                Id("i"),
                BinaryOp("/",Id("x"),NumberLiteral(2.0))
            ),
            NumberLiteral(1.0),
            Block([
                If(
                    BinaryOp(
                        "=",
                        BinaryOp("%",Id("x"),Id("i")),
                        NumberLiteral(0.0)),
                    Return(BooleanLiteral(False))
                )
            ]),
        ),
        Return(BooleanLiteral(True))
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test_program_010(self):
        input = """func fibonacci_gen() begin
        number fib[10]
        fib[0] <- 1
        fib[1] <- 1
        var i <- 2
        for i until i >= 10 by 1 fib[i] <- fib[i-1] + fib[i-2]
        return fib
        end
        func main()
        begin
        writeNumber(fibonacci_gen()[9])
        end
        """
        expect = str(
Program([
    FuncDecl(Id("fibonacci_gen"),[],Block([
        VarDecl(Id("fib"), ArrayType([10.0], NumberType()), None, None),
        Assign(ArrayCell(Id("fib"),[NumberLiteral(0.0)]), NumberLiteral(1.0)),
        Assign(ArrayCell(Id("fib"),[NumberLiteral(1.0)]), NumberLiteral(1.0)),
        VarDecl(Id("i"), None, "var", NumberLiteral(2.0)),
        For(
            Id("i"), 
            BinaryOp(">=", Id("i"), NumberLiteral(10.0)),
            NumberLiteral(1.0),
            Assign(
                ArrayCell(Id("fib"),[Id("i")]), 
                BinaryOp(
                    "+",
                    ArrayCell(Id("fib"),[BinaryOp("-", Id("i"), NumberLiteral(1.0))]),
                    ArrayCell(Id("fib"),[BinaryOp("-", Id("i"), NumberLiteral(2.0))])
                )
            )
        ),
        Return(Id("fib"))
    ])),
    FuncDecl(Id("main"),[],Block([
        CallStmt(Id("writeNumber"),[ArrayCell(CallExpr(Id("fibonacci_gen"),[]),[NumberLiteral(9.0)])])
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_program_011(self):
        input = """
        func main()
        begin
        writeNumber(readNumber())
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        CallStmt(Id("writeNumber"),[CallExpr(Id("readNumber"),[])])
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_program_012(self):
        input = """
        func _() begin
        dynamic __ <- __()[_]
        end
        """
        expect = str(
Program([
    FuncDecl(Id("_"),[],Block([
        VarDecl(Id("__"), None, "dynamic", ArrayCell(CallExpr(Id("__"), []), [Id("_")]))
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_program_013(self):
        input = """
        func a(number a) return b(a)
        func b(number b) return a(b)
        func c(number c) return c
        func main() begin
        var x <- a(_[1]) and b("c[-]")
        end
        """
        expect = str(
Program([
    FuncDecl(Id("a"), [VarDecl(Id("a"), NumberType())], Return(CallExpr(Id("b"),[Id("a")]))),
    FuncDecl(Id("b"), [VarDecl(Id("b"), NumberType())], Return(CallExpr(Id("a"),[Id("b")]))),
    FuncDecl(Id("c"), [VarDecl(Id("c"), NumberType())], Return(Id("c"))),
    FuncDecl(Id("main"),[],Block([
        VarDecl(Id("x"), None, "var", BinaryOp(
            "and",
            CallExpr(Id("a"), [ArrayCell(Id("_"),[NumberLiteral(1.0)])]),
            CallExpr(Id("b"), [StringLiteral("c[-]")])
            )
        )
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test_program_014(self):
        input = """func main() begin
        number a[10,10]
        var sum <- 0
        var i <- 0
        for i until i >= 10 by 1 begin
        var j <- 0
        for j until j >= 10 by 1 begin
        a[i,j] <- readNumber()
        sum <- sum + a[i,j]
        end
        end
        writeNumber(sum)
        end
        """
        expect = str(
Program([
    FuncDecl(Id("main"),[],Block([
        VarDecl(Id("a"), ArrayType([10.0, 10.0], NumberType())),
        VarDecl(Id("sum"), None, "var", NumberLiteral(0.0)),
        VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), Block([
            VarDecl(Id("j"), None, "var", NumberLiteral(0.0)),
            For(Id("j"), BinaryOp(">=", Id("j"), NumberLiteral(10.0)), NumberLiteral(1.0), Block([
                Assign(ArrayCell(Id("a"),[Id("i"), Id("j")]), CallExpr(Id("readNumber"), [])),
                Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("a"),[Id("i"), Id("j")])))
            ]))
        ])),
        CallStmt(Id("writeNumber"), [Id("sum")])
    ]))
])
)
        self.assertTrue(TestAST.test(input, expect, 399))
        
    