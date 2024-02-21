import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """First program"""
        input = """func main() begin
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_declarations(self):
        input = """func main() begin
                    number x <- 1
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        input = """func main() begin
                    bool x <- true
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        input = """func main() begin
                    string x <- "asdasd"
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
        input = """func main() begin
                    var x <- variable[][][]
                    end
                    """
        expect = "Error on line 2 col 38: ]"
        self.assertTrue(TestParser.test(input,expect,204))
        input = """func main() begin
                    dynamic x <- false
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        input = """func main() begin
                    number x[1,1,1] <- [[[[[[[[[],[]]]]]]]]]
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        input = """func main() begin
                    dynamic x[1,1,1] <- [[[[[[[[[]]]]]]]]]
                    end
                    """
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input,expect,207))
        input = """func main() begin
                    number x1 <- 1\nnumber x2 <- 2\nnumber x3 <- 3\nstring asdjn
                    bool x4 <- test()
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        input = """func main() begin
                    number x[q,2,3] <- [[[1,2,56,7],[2,27,6],[2]],[[5367]],[[123]]]
                    end
                    """
        expect = "Error on line 2 col 29: q"
        self.assertTrue(TestParser.test(input,expect,209))
        input = """func main() begin
                    number x[1,2,3] <- [[[1,2,q,7],[2,26,6],[2]],[[5367]],[[123]]]
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test_expressions(self):
        input = """func main() begin
                    x <- string1 ... string2
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        input = """func main() begin
                    x <- string1 ... string2 ... string3
                    end
                    """
        expect = "Error on line 2 col 45: ..."
        self.assertTrue(TestParser.test(input,expect,212))
        input = """func main() begin
                    x <- string1 == string2
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        input = """func main() begin
                    x <- string1 == string2 == string3
                    end\n"""
        expect = "Error on line 2 col 44: =="
        self.assertTrue(TestParser.test(input,expect,214))
        input = """func main() begin
                    x <- string1 === string2
                    end\n"""
        expect = "Error on line 2 col 35: ="
        self.assertTrue(TestParser.test(input,expect,215))
        input = """func main() begin
                    x <- a = b
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        input = """func main() begin
                    x <- a = b != c
                    end\n"""
        expect = "Error on line 2 col 31: !="
        self.assertTrue(TestParser.test(input,expect,217))
        input = """func main() begin
                    x <- a and b or c
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        input = """func main() begin
                    x <- a + b - c
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        input = """func main() begin
                    x <- a * b / c % d
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        input = """func main() begin
                    x <- not a
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
        input = """func main() begin
                    x <- not not a
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        input = """func main() begin
                    x <- -a
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
        input = """func main() begin
                    x <- -------a
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        input = """func main() begin
                    x <- a[index]
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
        input = """func main() begin
                    x <- a()[index, foo()]
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
        input = """func main() begin
                    x <- a()[index, foo()[1]]
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
        input = """func main() begin
                    x <- a(1=2)
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
        input = """func main() begin
                    x <- a[1][1]
                    end\n"""
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input,expect,229))
        input = """func main() begin
                    x <- (a+b) < c + (d ... e) ... f
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
        
    def test_loop_statement(self):
        input = """func main() begin
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
        input = """func main() begin
                    break
                    continue
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        input = """func main() begin
                    continue
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        input = """func main() begin
                    begin
                    begin
                    end
                    end
                    """
        expect = "Error on line 6 col 20: <EOF>"
        self.assertTrue(TestParser.test(input,expect,234))
        input = """func main() begin
                    begin newline
                    end
                """
        expect = "Error on line 2 col 26: newline"
        self.assertTrue(TestParser.test(input,expect,235))
        input = """func main() begin
                    for i_start until i_end by i_by begin 
                    arr[1,foo(3)] <- brr[2,c+-1]
                    end
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        input = """func main() begin
                    for i_start until i_end by i_by begin 
                    arr[1,foo(3)] <- brr[2,c+1] end
                    end\n"""
        expect = "Error on line 3 col 48: end"
        self.assertTrue(TestParser.test(input,expect,237))
        input = """func main() begin
                    for i_start until i_end by i_by for i_start until i_end by i_by arr[1,foo(3)] <- brr[2,c+1]
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        input = """func main() begin
                    for i_start until i_end by i_by fun(i)
                    x <- f()[1] = 1
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        
    def test_function(self):
        input = """func function1(a, b)"""
        expect = "Error on line 1 col 15: a"
        self.assertTrue(TestParser.test(input,expect,240))
        input = """func function1(number a, b)"""
        expect = "Error on line 1 col 25: b"
        self.assertTrue(TestParser.test(input,expect,241))
        input = """func function1(number a, b)"""
        expect = "Error on line 1 col 25: b"
        self.assertTrue(TestParser.test(input,expect,242))
        input = """func function1(number a, var b)
                    func main() begin
                    end\n"""
        expect = "Error on line 1 col 25: var"
        self.assertTrue(TestParser.test(input,expect,243))
        input = """func function1(number a, dynamic b)"""
        expect = "Error on line 1 col 25: dynamic"
        self.assertTrue(TestParser.test(input,expect,244))
        input = """func function1(bool b) return b
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
        input = """func function1(bool b) begin
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        input = """func function1(bool b) begin
                    return b
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
        input = """func function1(bool b) begin
                    func invalid_func_decl()
                    end
                    func main() begin
                    end\n"""
        expect = "Error on line 2 col 20: func"
        self.assertTrue(TestParser.test(input,expect,248))
        input = """func function1(bool b) begin
                    var x <- arr[1,2 + (b and c)]
                    b <- false and true
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        input = """var x <- 1
                    func function1(bool b) return x
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))     
        input = """var x <- 1
                    func function1(bool b) func invalid()
                    func main() begin
                    end\n"""
        expect = "Error on line 2 col 43: func"
        self.assertTrue(TestParser.test(input,expect,251))      
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c) begin
                    for i until x by a continue
                    return s
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))     
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c) begin
                    for i until x by a continue
                    return s
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c) begin
                    for i until x by a i <- function1(c ... a)
                    return s
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c) begin
                    begin
                    begin
                    end
                    end
                    end
                    func main() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    func main() begin
                    end
                    func invalid_function()"""
        expect = "Error on line 6 col 43: <EOF>"
        self.assertTrue(TestParser.test(input,expect,256))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    func main() begin
                    end
                    func function3() return\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    func main() begin
                    end
                    func function3() begin
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    func main() begin
                    end
                    func function3() begin
                    return function1(1,2,3,4,5) + function2(1)
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    func main() begin
                    end
                    var x <- 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    var x <- 1
                    func main() begin
                    end
                    var x <- 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    var x <- 1
                    func main() begin
                    end
                    var x <- 1
                    func function3(bool b) begin
                    end
                    var x <- 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
        input = """var x <- 1
                    func function1(bool b)
                    func function2(number a, string c)
                    var x <- 1
                    func main() begin
                    end
                    var x <- 1
                    func function3(bool b) return 1
                    var x <- 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        input = """var x <- 1
                    func function1(bool b) return 1
                    func function2(number a, string c) begin
                    c <- 1
                    end
                    var x <- 1
                    func main() begin
                    end
                    var x <- 1
                    func function3(bool b) begin
                    end
                    var x <- 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_if_statement(self):
        input = """func main() begin
                    if expr stmt <- 1
                    end\n"""
        expect = "Error on line 2 col 23: expr"
        self.assertTrue(TestParser.test(input,expect,265))
        input = """func main() begin
                    if (expr) 
                    
                    stmt <- 1
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        input = """func main() begin
                    elif expr stmt <- 1
                    end\n"""
        expect = "Error on line 2 col 20: elif"
        self.assertTrue(TestParser.test(input,expect,267))
        input = """func main() begin
                    if (expr) stmt <- 1 elif expr stmt <- 2
                    end\n"""
        expect = "Error on line 2 col 40: elif"
        self.assertTrue(TestParser.test(input,expect,268))
        input = """func main() begin
                    if (expr) stmt <- 1 
                    elif expr stmt <- 2
                    end\n"""
        expect = "Error on line 3 col 25: expr"
        self.assertTrue(TestParser.test(input,expect,269))
        input = """func main() begin
                    else stmt <- 3
                    end\n"""
        expect = "Error on line 2 col 20: else"
        self.assertTrue(TestParser.test(input,expect,270))
        input = """func main() begin
                    elif expr stmt <- 2
                    else stmt <- 3
                    end\n"""
        expect = "Error on line 2 col 20: elif"
        self.assertTrue(TestParser.test(input,expect,271))
        input = """func main() begin
                    if (expr) stmt <- 1
                    elif (expr) stmt <- 2
                    else expr stmt <- 3
                    end\n"""
        expect = "Error on line 4 col 30: stmt"
        self.assertTrue(TestParser.test(input,expect,272))
        input = """func main() begin
                    if (expr) stmt <- 1
                    elif (expr) stmt <- 2
                    else stmt <- 3
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
        input = """func main() begin
                    if (expr) if (expr) if (expr) if (expr) stmt <- 1111
                    elif (expr) stmt <- 2
                    else stmt <- 3
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
        input = """func main() begin
                    if (expr1)
                        if (expr2) 
                            if (expr2) 
                                if (expr2) stmt <- 31
                                elif (expr2) stmt <- 32
                                else stmt <- 33
                            elif (expr2) stmt <- 32
                            else stmt <- 33
                        elif (expr2) stmt <- 12
                        else stmt <- 13
                    elif (expr1) 
                        if (expr2) stmt <- 21
                        elif (expr2) stmt <- 22
                        else stmt <- 23
                    else 
                        if (expr2) stmt <- 31
                        elif (expr2) stmt <- 32
                        else
                            if (expr2) stmt <- 31
                            elif (expr2) stmt <- 32
                            else 
                                if (expr2) stmt <- 31
                                elif (expr2) stmt <- 32
                                else stmt <- 33
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
        input = """func main() begin
                    if (expr1) stmt <- 1
                    elif (expr1) 
                        if (expr2) stmt <- 21
                        elif (expr2) 
                            if (expr2) stmt <- 21
                            elif (expr2) 
                                if (expr2) stmt <- 21
                                elif (expr2) 
                                    if (expr2) stmt <- 21
                                    elif (expr2) stmt <- 22
                                    else stmt <- 23
                                else stmt <- 23
                            else stmt <- 23
                        else stmt <- 23
                    else stmt <- 3
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
        input = """func main() begin
                    if (expr1) stmt <- 1
                    elif (expr1) stmt <- 2
                    elif (expr1) stmt <- 3
                    elif (expr1) stmt <- 4
                    elif (expr1) stmt <- 5
                    else stmt <- 6
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        input = """func main() begin
                    if (expr1) for i until i_until by i_by begin
                        if (expr11) stmt <- 1
                        elif (expr11) stmt <- 1
                        elif (e) 
                            if (q2) stmt <- 1
                            elif (expr11) stmt <- 1
                            elif (e) stmt <- 1
                            elif (qweqwe) stmt <- 1
                        elif (qweqwe) stmt <- 1
                    end
                    elif (expr1) stmt <- 2
                    else stmt <- 3
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
        input = """var x <- 1
                if (expr1) stmt <- 1
                func main() begin
                end\n"""
        expect = "Error on line 2 col 16: if"
        self.assertTrue(TestParser.test(input,expect,279))
        input = """var x <- 1
                func main() begin
                    if (e1) stmt <- 1
                    elif (e1) begin
                        for i until i by i if (e1) stmt <- 2
                    end
                    elif (e1) b<-1
                    else b <- 1
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
        input = """var x <- 1
                func main() begin
                    if (e1) stmt <- 1
                    else begin
                        for i until i by i if (e1) stmt <- 2
                    end
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
        input = """var x <- 1
                func main() begin
                    iF (e1) stmt <- 1
                    else begin
                        for i until i by i if (e1) stmt <- 2
                    end
                end\n"""
        expect = "Error on line 3 col 28: stmt"
        self.assertTrue(TestParser.test(input,expect,282))
        input = """var x <- 1
                func main() begin
                    if (e1) stmt <- 1
                    elIf (e2) begin
                        for i until i by i if (e1) stmt <- 2
                    end
                end\n"""
        expect = "Error on line 4 col 30: begin"
        self.assertTrue(TestParser.test(input,expect,283))
        input = """var x <- 1
                func main() begin
                    if (e1) stmt <- 1
                    elif (e2) begin
                        for i until i by i if (e1) stmt <- 2
                    end
                    elSe stmt <- 1
                end\n"""
        expect = "Error on line 7 col 25: stmt"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_program(self):
        input = """func main() begin
                    number fib[100]
                    fib[0] <- 1
                    fib[1] <- 1
                    var i <- 1
                    for i until i < 99 by 1 begin
                    fib[i+1] <- fib[i] + fib[i-1]
                    end
                    i <- 0
                    for i until i < 100 by 1 writeString(fib[i])
                    end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
        input = """func areDiv(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()
                    if(areDiv(num1, num2)) writeString("Yes")
                    else writeString("No")
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
        input = """func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if(isPrime(x)) writeString("Yes")
                    else writeString("No")
                end
            func isPrime(number x)
                begin
                    if(x <= 1) return false
                    var i <- 2
                    for i until i > x/2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                    return true
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
        input = """func main()
                begin
                number r
                number s
                r <- 2.0
                number a[5]
                number b[5]
                s <- r * r * 3.14
                a[0] <- s
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
        input = """func main()
                begin
                var i <- 0
                for i until i >= 10 by 1
                writeNumbe(i)
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
        input = """func main() begin \n var i <- 0 \n for i until i >= 10 by 1 writeNumbe(i) \n end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
        input = """func finder(number array[100], number left, number right, number k) begin
                    if(left <= right) begin
                        var mid <- right + (left - right) / 2
                        if(array[mid] = k) return mid
                        if(array[mid] > k) return finder(array, left, mid - 1, k)
                        if(array[mid] < k) return finder(array, mid, right, k)
                    end
                    return -1
                end
                func main()
                begin
                    var arr[5] <- [1,2,3,4,5]
                    var index <- finder(arr,0,4,2)
                    if(index = -1) writeString("No")
                    else writeNumber(index)
                end\n"""
        expect = "Error on line 12 col 27: ["
        self.assertTrue(TestParser.test(input,expect,291))
        input = """func main(number invalid)
                begin
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
        input = """func main() return 1
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
        input = """func main()
                begin
                ## var i <- 0
                for i until i >= 10 by 1
                writeNumbe(i)
                end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
        input = """func main()
                begin
                ## var i <- 0
                for i until i >= 10 by 1
                writeNumbe(number i)
                end"""
        expect = "Error on line 5 col 27: number"
        self.assertTrue(TestParser.test(input,expect,295))
        input = """func main()
                begin
                if (x) stmt <- 1
                elif x = a = a writeNumbe(i)
                end\n"""
        expect = "Error on line 4 col 21: x"
        self.assertTrue(TestParser.test(input,expect,296))
    
    def test_err_lexer(self):
        input = """func main()
                begin
                string !qqq
                end\n"""
        expect = "!"
        self.assertTrue(TestParser.test(input,expect,297))
        input = """func main()
                begin
                string c <- "Illegal Escape \\a"
                end\n"""
        expect = "Illegal Escape \\" + "a"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_lexer_error(self):
        input = """func main()
                begin
                string c <- "Unclosed String
                end\n"""
        expect = "Unclosed String"
        self.assertTrue(TestParser.test(input,expect,299))
    