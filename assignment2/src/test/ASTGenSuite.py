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
        
    def test_simple_if_statement_003(self):
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
        
    def test_simple_if_statement_004(self):
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
        
    def test_simple_if_statement_005(self):
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
        
    def test_simple_if_statement_006(self):
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
        
    def test_simple_if_statement_007(self):
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

    def test_simple_if_statement_008(self):
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
        
    def test_simple_if_statement_009(self):
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