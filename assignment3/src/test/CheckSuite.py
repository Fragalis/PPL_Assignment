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
        dynamic a
        dynamic x <- a == (a+2)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), BinaryOp(+, Id(a), NumLit(2.0)))))"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_simple_vardecl_6(self):
        input = """func main() begin
        dynamic b
        var a <- b + 1
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
        expect = ""
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
        
    def test_complex_funcdecl_0(self):
        input = """
        var k <- 1
        func f1() return k
        func main() begin
            writeNumber(f1())
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_complex_funcdecl_1(self):
        input = """
        func a() return 1
        number a <- 1
        func main() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_complex_funcdecl_2(self):
        input = """
        func a() return 1
        func main() begin
        var b <- a()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_complex_funcdecl_3(self):
        input = """
        func a(number a, number b[1]) begin
            return a = b[1]
        end
        func main() begin
        var b <- a(1, [1])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_complex_funcdecl_4(self):
        input = """
        func a() begin
            return
        end
        func main() begin
        var b <- 1
        a()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_complex_funcdecl_5(self):
        input = """
        func a() begin
            return
        end
        func main() begin
        var b <- 1
        a()
        writeNumber(a())
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_complex_funcdecl_6(self):
        input = """
        func a() begin
            return
        end
        func main()
        func main() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_complex_funcdecl_7(self):
        input = """
        func foo(number a)
        func foo(string a, bool b) return a
        func main()
        begin 
        end
        """
        expect = "Redeclared Function: foo)"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_complex_funcdecl_8(self):
        input = """
        number x
        func foo()
        begin
        if (x = 1)
            return true
        else
            return 1
        end
        func main()
        begin
        number num <- foo()
        end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_complex_funcdecl_9(self):
        input = """
        func foo()
        func main() begin
           number a <- foo()
        end
        func foo() return "str"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(str))"
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_if_0(self):
        input = """
        func main() begin
        dynamic i
        if (i) writeBool(true)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_if_1(self):
        input = """
        func main() begin
        dynamic i1
        dynamic i2
        if (i1) begin
            i2 <- readNumber()
        end
        elif (i2) begin
            i1 <- true
        end
        end
        """
        expect = "Type Mismatch In Statement: If(Id(i1), Block([AssignStmt(Id(i2), CallExpr(Id(readNumber), []))])), [(Id(i2), Block([AssignStmt(Id(i1), BooleanLit(True))]))], None"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_if_2(self):
        input = """
        func main() begin
        dynamic i1
        dynamic i2
        dynamic i3 <- i1 and i2
        if (i1) begin
            i2 <- readBool()
        end
        elif (i2) begin
            i3 <- true
        end
        else
            writeString("hello world")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_if_3(self):
        input = """
        func main() begin
        dynamic i1
        dynamic i2
        dynamic i3 <- i1 ... "string"
        if (false) 
            i2 <- i3 == i1
        if (i2)
            i3 <- i1
        else
            i2 <- (i3 == i1) or i2
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_if_4(self):
        input = """
        func main() begin
        dynamic i1
        dynamic i2
        if (i1 = i2) begin
        end
        elif (i1) begin
        end
        end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=, Id(i1), Id(i2))), Block([])), [(Id(i1), Block([]))], None"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_for_0(self):
        input = """
        func main() begin
        dynamic i
        for i until true by 1 begin
        end
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_for_1(self):
        input = """
        func main() begin
        dynamic i <- true
        for i until true by 1 begin
        end
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i), BooleanLit(True), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_for_2(self):
        input = """
        func main() begin
        dynamic i <- 1
        for i until 10 by 1 begin
        end
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i), NumLit(10.0), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_for_3(self):
        input = """
        func main() begin
        dynamic i <- 1
        var j <- i = i
        for i until true by j begin
        end
        end
        """
        expect = "Type Mismatch In Statement: For(Id(i), BooleanLit(True), Id(j), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_for_4(self):
        input = """
        func main() begin
        dynamic i <- 1
        var j <- i = i
        for i until true by 1 begin
            number i <- j + 1
            j <- i
        end
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(j), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_scope_0(self):
        input = """
        var a <- 1
        func main() begin
            var a <- true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test_scope_1(self):
        input = """
        var a <- 1
        func f(string a)
        func main() begin
            var a <- true
            if (f("true"))
                number a <- 1
        end
        func f(string a) return true
        """
        expect = "Redeclared Variable: a)"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test_scope_2(self):
        input = """
        var a <- 1
        func f(string a)
        func main() begin
            var a <- true
            if (f("true")) begin
                number a <- 1
            end
        end
        func f(string a) return true
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))
        
    def test_scope_3(self):
        input = """
        var a <- 1
        func f(string a)
        func main() begin
            var a <- true
            if (f("true")) begin
                number a <- 1
                for a until true by 1 begin
                    var a <- "hello"
                end
            end
        end
        func f(string a) return true
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test_scope_4(self):
        input = """
        var a <- 1
        func f(string a) begin
            bool a <- true
        end
        func main() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
            
    def test_scope_5(self):
        input = """
        var a <- 1
        func f(string a)
        func main() begin
        end
        func f(string b) begin
            bool b <- true
            return a
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test_scope_6(self):
        input = """
        var a <- 1
        func f(string a)
        func main() begin
            var b <- true
            if (f("true")) begin
                number c <- 1
                for c until true by 1
                    var c <- f("hi")
            end
        end
        func f(string a) return true
        """
        expect = "Redeclared Variable: c)"
        self.assertTrue(TestChecker.test(input, expect, 456))
            
    def test_scope_7(self):
        input = """
        dynamic x
        func f(string a)
        func main() begin
            if (true) begin
                dynamic x
                x <- "hello"
                f(x)
            end
            x <- 1
            f(x)
        end
        func f(string b) begin
            var b <- true
            if (false) begin
                number c <- 1
                for c until true by 1 writeNumber(c)
            end
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test_scope_8(self):
        input = """
        dynamic x
        func f(string a)
        func main() begin
            if (true) begin
                dynamic x
                x <- "hello"
                f(x)
            end
            elif (false) begin
                f(x)
            end
            x <- 1
            f(x)
        end
        func f(string b) begin
            var b <- true
            if (false) begin
                number c <- 1
                for c until true by 1 writeNumber(c)
            end
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_scope_9(self):
        input = """
        dynamic x
        func f(string a, number b)
        func main() begin
            x <- 1
            if (true) begin
                dynamic x
                x <- "hello"
                f(x, x)
            end
        end
        func f(string b, number c) begin
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [Id(x), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test_infer_0(self):
        input = """
        func main() begin
            dynamic x
            if (x = 1)
                x <- 2
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_infer_1(self):
        input = """
        dynamic a
        string x <- [a]
        func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_infer_2(self):
        input = """
        dynamic a
        string x[1] <- [a]
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_infer_3(self):
        input = """
        dynamic a
        dynamic x <- a == (a+2)
        func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), BinaryOp(+, Id(a), NumLit(2.0)))))"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_infer_4(self):
        input = """
        func main()
        begin
        dynamic a
        var x <- a[0]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_infer_5(self):
        input = """
        func main()
        begin
        dynamic x
        dynamic y
        number a[2] <- [x,y]
        writeNumber(x)
        writeNumber(y)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_infer_6(self):
        input = """
        func main()
        func foo()
        begin
        number a <- main()
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test_infer_7(self):
        input = """
        func main()
        begin 
            dynamic a
            dynamic b
            dynamic c
            number x[3,3] <- [a,b,c]
            a <- [1,2,3]
            b <- [4,5,6]
            c <- [7,8,9]
            writeNumber(a[0] + b[0] + c[0])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test_infer_8(self):
        input = """
        func foo() begin
            dynamic d
            return d
        end
        func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_infer_9(self):
        input = """
        dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_infer_10(self):
        input = """
        func main()
        begin
            var a <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_infer_11(self):
        input = """
        dynamic x
        number a[2,2] <- [x,[x,x]]
        func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_infer_12(self):
        input = """
        dynamic a
        func main() begin
        a <- [[1, 2], [3, true]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(3.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_infer_13(self):
        input = """
        func foo(number a, number b)
        func main()
        begin
            return 1 + foo(1, "str")
        end
        func foo(number a, number b)
        begin
            return 0
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(str)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_infer_14(self):
        input = """
        func foo(number a, number b)
        func main()
        begin
            dynamic a <- 1 + foo(1, 2)
        end
        func foo(number a, number b)
        begin
            return 0
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test_infer_15(self):
        input = """
        func foo(number a) begin
            if (a > 0) return "aa"
            elif (a > 2) return true
            return
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_infer_16(self):
        input = """
        func f() return 1
        func main() begin
        var x <- f
        end
        """
        expect = "Undeclared Identifier: f)"
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test_infer_17(self):
        input = """
        func main() begin
        dynamic a
        number b <- a[0]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test_infer_18(self):
        input = """
        func main() begin
        dynamic a
        var b <- a[0]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test_infer_19(self):
        input = """
        func hello(number a)
        begin
        end
        
        func main()
        begin
            dynamic a 
            dynamic b <- [[1,2,3], a]
            number c <- a[0]
            number d <- a
        end
        
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(d), NumberType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
    def test_infer_20(self):
        input = """
        func main() begin
        dynamic a
        var b <- a[0] and true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))       
        
    def test_infer_21(self):
        input = """
        dynamic d
        func foo()
        func main() begin
            dynamic a
            a[1] <- d[0] and true
        end
        func foo() begin
            return d[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
        
    def test_infer_22(self):
        input = """
        dynamic d
        func foo()
        func main() begin
            dynamic a <- [true]
            a[1] <- d[0]
        end
        func foo() begin
            return d[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))    
        
    def test_infer_23(self):
        input = """
        func foo()
        func main() begin
            dynamic a <- foo()
        end
        func foo() begin
            return
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test_infer_24(self):
        input = """
        func main() begin
            number a[4,4]
            dynamic b
            a[4] <- [b]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
        
    def test_infer_25(self):
        input = """
        func foo() begin
            return [[1]]
        end
        func main() begin
            dynamic x
            dynamic y <- x[1]
            x <- foo()[1]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, ArrayCell(Id(x), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 485))
        
    def test_infer_26(self):
        input = """
        func foo() begin
            return [[1]]
        end
        func main() begin
            dynamic x
            x <- foo()[1]
            dynamic y <- x[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test_infer_27(self):
        input = """
        func hello(number a)
        begin
        end
        func main()
        begin
            dynamic b
            hello(b)
            number c <- b + 1
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))
        
    def test_infer_28(self):
        input = """
        func foo(number x) return 1
        func main()
        begin
            dynamic a
            dynamic x
            dynamic y <- a + foo(x)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test_infer_29(self):
        input = """
        func f() begin
        number c[3,2] <- [[6,7],[4,5],[4,5]]
        return c[2]
        end
        func main() begin
        dynamic a <- f()[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_program_0(self):
        input = """
        func fib() begin
            number c[10]
            c[0] <- 1
            c[1] <- 1
            var i <- 2
            for i until i >= 10 by 1 begin
                c[i] <- c[i - 1] + c[i - 2]
            end
            return c
        end
        func main() begin
            dynamic idx <- readNumber()
            writeNumber(fib()[idx])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_program_1(self):
        input = """
        func someRandomNumber()
        func gen(number arr[10,10], number idx) begin
            var i <- 0
            for i until i >= 10 by 1 begin
                var j <- 0
                for j until j >= 10 by 1 begin
                    arr[i,j] <- someRandomNumber()
                end
            end
            return arr[idx]
        end
        func main() begin
            dynamic list
            var i <- 0
            for i until i >= 10 by 1 begin
                writeNumber(gen(list, i)[i])
            end
        end
        func someRandomNumber() return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_program_2(self):
        input = """
        dynamic list
        func extract(number m[10,10], number i)
        func main() begin
            dynamic m
            dynamic x
            dynamic idx
            dynamic i
            for i until x and (i = 10) by idx begin
                extract(m, i - idx)
                writeNumber(list[idx])
            end
        end
        func extract(number mat[10,10], number idx) begin
            list <- mat[idx]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))