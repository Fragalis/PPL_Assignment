import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_simple_expr_0(self):
        input = """func main() begin
        number a <- 1 + 1
        bool b <- true and true
        string c <- "hello" ... "world"
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_simple_expr_1(self):
        input = """func main() begin
        bool b <- true and true
        number a <- 1 + b
        string c <- "hello" ... "world"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_simple_expr_2(self):
        input = """func main() begin
        number a <- 1 + 1
        bool b <- true and a
        string c <- "hello" ... "world"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, BooleanLit(True), Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_simple_expr_3(self):
        input = """func main() begin
        number a <- 1 + 1
        bool b <- true and false
        string c <- "hello" ... b
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(hello), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_simple_expr_4(self):
        input = """func main() begin
        dynamic a
        a <- 1
        bool b <- true and a
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, BooleanLit(True), Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_simple_vardecl_0(self):
        input = """func main() begin
        number a <- 1
        number b <- a
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_simple_vardecl_1(self):
        input = """func main() begin
        var a <- 1
        number b <- a
        dynamic c <- b + a
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_simple_vardecl_2(self):
        input = """func main() begin
        var a <- readBool()
        number b[1,1] <- [[2]]
        dynamic arr
        arr <- b[1] + [readNumber()]
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, ArrayCell(Id(b), [NumLit(1.0)]), ArrayLit(CallExpr(Id(readNumber), []))))"
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_simple_vardecl_3(self):
        input = """func main() begin
        dynamic x
        dynamic y
        y <- [[1,2,3],[4,5,6]]
        x <- y[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_simple_vardecl_4(self):
        input = """func main() begin
        dynamic x
        x <- x + 1
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_simple_vardecl_5(self):
        input = """func main() begin
        dynamic x
        x <- x and true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_simple_vardecl_6(self):
        input = """func main() begin
        dynamic x
        x <- x ... "hello"
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_simple_vardecl_7(self):
        input = """func main() begin
        dynamic x <- readNumber()
        dynamic y <- [x]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_simple_vardecl_8(self):
        input = """func main() begin
        var x <- [readNumber()]
        dynamic y <- [x]
        number z[1,1] <- y
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_simple_vardecl_9(self):
        input = """func main() begin
        dynamic x <- [[1,2], [5, "a"]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(5.0), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_simple_vardecl_10(self):
        input = """func main() begin
        dynamic x <- 1 + x
        end
        """
        expect = "Undeclared Identifier: x)"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_simple_vardecl_11(self):
        input = """dynamic x
        func main() begin
        dynamic y <- x + 1
        x <- y = 12
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(=, Id(y), NumLit(12.0))))"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_simple_vardecl_12(self):
        input = """dynamic x
        func main() begin
        dynamic y <- x
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_simple_vardecl_13(self):
        input = """
        func main() begin
        dynamic y
        y <- (y = 1) and (y or "world")
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, Id(y), StringLit(world)))"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_simple_vardecl_14(self):
        input = """
        func main() begin
        dynamic y
        dynamic y <- 1
        end
        """
        expect = "Redeclared Variable: y)"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_simple_funcdecl_0(self):
        input = """
        func f()
        func main() begin
        end
        func f() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_simple_funcdecl_1(self):
        input = """
        func f(number a, number b[1,1,1])
        func main() begin
        end
        func f(number a, number b[1,1,1]) begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_simple_funcdecl_2(self):
        input = """
        func f(number a, number a)
        func main() begin
        end
        func f(number a, number b[1]) begin
        end
        """
        expect = "Redeclared Parameter: a)"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_simple_funcdecl_3(self):
        input = """
        func f(number a, number b[1,1])
        func f(number a, number b[1,1])
        func main() begin
        end
        func f(number a, number b[1,1]) begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_simple_funcdecl_4(self):
        input = """
        func foo()
        begin
            number a <- 3
        end
        func main() begin
        end
        func foo()
        """
        expect = "Redeclared Function: foo)"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_simple_funcdecl_5(self):
        input = """
        func func1()
        func main()
        begin
        number a <- func1()
        end
        func func2()
        func func1()
        begin
        var b <- func2()
        return b
        end
        func func2() return 1
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, CallExpr(Id(func2), []))"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_simple_funcdecl_6(self):
        input = """
        func readNumber()
        func main()
        begin
        end
        """
        expect = "Redeclared Function: readNumber)"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_simple_funcdecl_7(self):
        input = """
        func f1(number a, number b[1,1])
        func f2(number a, number b[1,1])
        func main() begin
        end
        func f2(number a, number b[1,1]) begin
        end
        """
        expect = "No Function Definition: f1"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test_simple_funcdecl_8(self):
        input = """
        func f1(number a, number b[1,1])
        func f2(number a, number b[1,1])
        func main() begin
        end
        func f2(number a, number b[1,1]) begin
        end
        func f2(number a, number b[1,1]) begin
        end
        func f1(number a, number b[1,1]) begin
        end
        """
        expect = "Redeclared Function: f2)"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_simple_funcdecl_9(self):
        input = """
        func f1(number a, number b[1,1])
        func f2(number a, number b[1,1])
        func main()
        func f2(number a, number b[1,1]) begin
        end
        func f1(number a, number b[1,1]) begin
        end
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 429))