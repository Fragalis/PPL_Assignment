import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_keyword_operator(self):
        """basics"""
        self.assertTrue(TestLexer.test("true false number bool string return var dynamic func for until by break continue if else elif begin end not and or + - * / % = <- != < <= > >= ... == ( [ , ] )",
                                       "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,(,[,,,],),<EOF>"
                                      ,100))
        self.assertTrue(TestLexer.test("!===","!=,==,<EOF>",101))
    
    def test_identifier(self):
        """identifiers"""
        self.assertTrue(TestLexer.test("i J _ ab aB a0 a_ B1 Bx BQ B_ _x _Y _8 _______ printer vAr _xy123"
                                      ,"i,J,_,ab,aB,a0,a_,B1,Bx,BQ,B_,_x,_Y,_8,_______,printer,vAr,_xy123,<EOF>"
                                      ,102))
        self.assertTrue(TestLexer.test("_!invalid","_,Error Token !",103))
        self.assertTrue(TestLexer.test("1nvalid","1,nvalid,<EOF>",104))
        self.assertTrue(TestLexer.test("?nvalid","Error Token ?",105))
        
    def test_number_literal(self):
        """numbers"""
        self.assertTrue(TestLexer.test("0 10. 192376182 57.21 27.8e1 21E+4 5e-2 0.00E+00"
                                      ,"0,10.,192376182,57.21,27.8e1,21E+4,5e-2,0.00E+00,<EOF>"
                                      ,106))
        self.assertTrue(TestLexer.test("Invalid number 1.2.3","Invalid,number,1.2,Error Token .",107))
        self.assertTrue(TestLexer.test("Valid number question mark 0e","Valid,number,question,mark,0,e,<EOF>",108))
        
    def test_string_literal(self):
        """strings"""
        self.assertTrue(TestLexer.test(""" "" """
                                      ,""",<EOF>"""
                                      ,109))
        self.assertTrue(TestLexer.test(""" "This's a valid string" """
                                      ,"""This's a valid string,<EOF>"""
                                      ,110))
        self.assertTrue(TestLexer.test(""" "" "" """
                                      ,""",,<EOF>"""
                                      ,111))
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John?'"" """
                                      ,"""He asked me: '"Where is John?'",<EOF>"""
                                      ,112))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """b" """
                                      ,"""Escape seq: \\b,<EOF>"""
                                      ,113))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """'" " """
                                      ,"""Escape seq: \\'" ,<EOF>"""
                                      ,114))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """t" """
                                      ,"""Escape seq: \\t,<EOF>"""
                                      ,115))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """\\" """
                                      ,"""Escape seq: \\\\,<EOF>"""
                                      ,116))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """f" """
                                      ,"""Escape seq: \\f,<EOF>"""
                                      ,117))
        self.assertTrue(TestLexer.test(""" "Escape seq: \\""" + """r" """
                                      ,"""Escape seq: \\r,<EOF>"""
                                      ,118))
        self.assertTrue(TestLexer.test(""" "string 1" "string 2" """
                                      ,"""string 1,string 2,<EOF>"""
                                      ,119))
        self.assertTrue(TestLexer.test(""" "string "inside string"" """
                                      ,"""string ,inside,string,,<EOF>"""
                                      ,120))
        
    def test_unclosed_string(self):
        """unclosed string"""
        self.assertTrue(TestLexer.test(""" "test """
                                      ,"""Unclosed String: test """
                                      ,121))
        self.assertTrue(TestLexer.test(""" "quotation: \'" """
                                      ,"""Unclosed String: quotation: \'" """
                                      ,122))
        self.assertTrue(TestLexer.test(""" "string "in string" """
                                      ,"""string ,in,string,Unclosed String:  """
                                      ,123))
        self.assertTrue(TestLexer.test(""" "multi '"string in "string " """
                                      ,"""multi '"string in ,string,Unclosed String:  """
                                      ,124))
        self.assertTrue(TestLexer.test(""" "linebreak \n in string" """
                                      ,"""Unclosed String: linebreak """
                                      ,125))
        
    def test_illegal_escape(self):
        """illegal escape"""
        self.assertTrue(TestLexer.test(""" "Escape seq \\""" + """a funny" """
                                      ,"""Illegal Escape In String: Escape seq \\""" + """a"""
                                      ,126))  
        self.assertTrue(TestLexer.test(""" "Escape seq \\""" + """c funny" """
                                      ,"""Illegal Escape In String: Escape seq \\""" + """c"""
                                      ,127)) 
        self.assertTrue(TestLexer.test(""" "Escape seq \\""" + """" funny" """
                                      ,"""Illegal Escape In String: Escape seq \\""" + '"'
                                      ,128))
        self.assertTrue(TestLexer.test(""" "Escape seq \\b with \\""" + """v funny" """
                                      ,"""Illegal Escape In String: Escape seq \\b with \\""" + """v"""
                                      ,129))
        
    def test_separator(self):
        """separators"""
        self.assertTrue(TestLexer.test("[,](\n)","[,,,],(,\n,),<EOF>",130))
        self.assertTrue(TestLexer.test("([}}])","(,[,Error Token }",131))    
        self.assertTrue(TestLexer.test("([{}}])","(,[,Error Token {",132))
        self.assertTrue(TestLexer.test("""var x\n\nvar y"""
                                      ,"""var,x,\n,\n,var,y,<EOF>"""
                                      ,133))
        self.assertTrue(TestLexer.test("""arr[1,2 + foo(6)]"""
                                      ,"""arr,[,1,,,2,+,foo,(,6,),],<EOF>"""
                                      ,134))
        
    def test_comments(self):   
        """comments test"""
        self.assertTrue(TestLexer.test("## A valid comment","<EOF>",135))
        self.assertTrue(TestLexer.test("##stillav\nalidcomment","\n,alidcomment,<EOF>",136))
        self.assertTrue(TestLexer.test("b\n## After slash n","b,\n,<EOF>",137))  
        self.assertTrue(TestLexer.test("b\n## Between slash n\na","b,\n,\n,a,<EOF>",138))
        self.assertTrue(TestLexer.test("## Before slash n\na","\n,a,<EOF>",139))
        self.assertTrue(TestLexer.test("a ## Valid","a,<EOF>",140))
        input = """array <- 1 
                ## Comment
                """
        expect = """array,<-,1,\n,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,141))
        input = """
                ## Comment
                array <- 1
                """
        expect = """\n,\n,array,<-,1,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,142))
        self.assertTrue(TestLexer.test("a######### Valid","a,<EOF>",143))
        self.assertTrue(TestLexer.test("a# Invalid","a,Error Token #",144))
        self.assertTrue(TestLexer.test("a// What if C Comment","a,/,/,What,if,C,Comment,<EOF>",145))
        self.assertTrue(TestLexer.test("a <!-- What if HTML Comment -->","a,<,Error Token !",146))
        input = """## Body
                begin for i in value <- exponent end
                ## After body
                """
        expect = """\n,begin,for,i,in,value,<-,exponent,end,\n,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,147))
        input = """## \n Body
                begin \r for \f i in value <- exponent end
                ## After body
                """
        expect = """\n,Body,\n,begin,for,i,in,value,<-,exponent,end,\n,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,148))
        input = """## []as[d]as[d "string" Body
                begin \r for \f i in value <- exponent end
                ## After body
                """
        expect = """\n,begin,for,i,in,value,<-,exponent,end,\n,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,149))
        
    def test_combination(self):
        """combination"""
        self.assertTrue(TestLexer.test("a######### Valid","a,<EOF>",150))
        self.assertTrue(TestLexer.test("func main dynamic type","func,main,dynamic,type,<EOF>",151))
        input = """var x <- 1 and y
                begin tester end \n
                end
                """
        expect = """var,x,<-,1,and,y,\n,begin,tester,end,\n,\n,end,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,152))
        input = """bool y is not var <- "!@#%&^%@(*!%)^#*!@&(*#^@%$0)"
                if lexer the quick brown fox <-===!= else
                """
        expect = """bool,y,is,not,var,<-,!@#%&^%@(*!%)^#*!@&(*#^@%$0),\n,if,lexer,the,quick,brown,fox,<-,==,=,!=,else,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,153))
        input = """bool y is not var <- "!@#%&^%@(*!%)^#*!@&(*#^@%$0)
                if lexer the quick brown fox <-==!= else
                """
        expect = """bool,y,is,not,var,<-,Unclosed String: !@#%&^%@(*!%)^#*!@&(*#^@%$0)"""
        self.assertTrue(TestLexer.test(input,expect,154))
        input = """<==>==<===>==><><>========..."""
        expect = """<=,=,>=,=,<=,==,>=,=,>,<,>,<,>=,==,==,==,=,...,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,155))
        input = """(+-[\n-<andornot!=%/%>%>=<--\n--->)"""
        expect = """(,+,-,[,\n,-,<,andornot,!=,%,/,%,>,%,>=,<-,-,\n,-,-,-,>,),<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,156))
        input = """var and <-- andnot and not
                dynamic bool boolean -><- boolean1917_ _912"""
        expect = """var,and,<-,-,andnot,and,not,\n,dynamic,bool,boolean,-,>,<-,boolean1917_,_912,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,157))
        input = """var and <-- andnot and not
                dynamic bool boolean -><- boolean1917_ _912"""
        expect = """var,and,<-,-,andnot,and,not,\n,dynamic,bool,boolean,-,>,<-,boolean1917_,_912,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,157))
        input = """for y by until if you === ok then (v)^"""
        expect = """for,y,by,until,if,you,==,=,ok,then,(,v,),Error Token ^"""
        self.assertTrue(TestLexer.test(input,expect,158))
        input = """class Classer @overdrive"""
        expect = """class,Classer,Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,159))
        input = """if !(a and b) elif eliF File"""
        expect = """if,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,160))
        input = """func add(a, b) begin
                return a + b
                end"""
        expect = """func,add,(,a,,,b,),begin,\n,return,a,+,b,\n,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,161))
        input = """func decl() begin end
                var x <- 10
                var y <- 3.14
                var z <- true
                var str <- "!Hello, world!"
                """
        expect = """func,decl,(,),begin,end,\n,var,x,<-,10,\n,var,y,<-,3.14,\n,var,z,<-,true,\n,var,str,<-,!Hello, world!,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,162))
        input = """arr[1,2,3,4,5] <-->>=< """
        expect = """arr,[,1,,,2,,,3,,,4,,,5,],<-,-,>,>=,<,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,163))
        input = """x = 1e"""
        expect = """x,=,1,e,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,164))
        input = """_cC192 = _pri!vateVariable"""
        expect = """_cC192,=,_pri,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,165))
        input = """string str$ <- "The quick fox\\b escape \\t'" " q """
        expect = """string,str,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,166))
        input = """dynam1c <- 0ver"""
        expect = """dynam1c,<-,0,ver,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,167))
        input = """## Comment \n abdullah#IRQ3-1JOR"""
        expect = """\n,abdullah,Error Token #"""
        self.assertTrue(TestLexer.test(input,expect,168))
        input = """string stR <- """""""#IRQ3-1JOR""""""" """
        expect = """string,stR,<-,#IRQ3-1JOR,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,169))

    def test_final(self):
        """everything else here"""
        input = """func main()
                begin
                string c <- "Illegal Escape \\a"
                end"""
        expect = "func,main,(,),\n,begin,\n,string,c,<-,Illegal Escape In String: Illegal Escape \\" + "a"
        self.assertTrue(TestLexer.test(input,expect,170))
        input = """func main()
                begin
                string c <- "Unclosed String\n"
                end"""
        expect = "func,main,(,),\n,begin,\n,string,c,<-,Unclosed String: Unclosed String"
        self.assertTrue(TestLexer.test(input,expect,171))
        input = """func main() begin
                    number x[1,2,3] <- [[[1,2,q,7],[2,26,6],[2]],[[5367]],[[123]]]
                    end"""
        expect = """func,main,(,),begin,
,number,x,[,1,,,2,,,3,],<-,[,[,[,1,,,2,,,q,,,7,],,,[,2,,,26,,,6,],,,[,2,],],,,[,[,5367,],],,,[,[,123,],],],
,end,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,172))
        input = """func main() begin
                    x <- a = b != c
                    end"""
        expect = "func,main,(,),begin,\n,x,<-,a,=,b,!=,c,\n,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,173))
        input = """func main() begin
                    if expr stmt <- 1 
                    elif expr stmt <- 2
                    end"""
        expect = "func,main,(,),begin,\n,if,expr,stmt,<-,1,\n,elif,expr,stmt,<-,2,\n,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,174))
        input = """func fUnc(number nUmber)"""
        expect = "func,fUnc,(,number,nUmber,),<EOF>"
        self.assertTrue(TestLexer.test(input,expect,175))
        input = """func fUnc(number nUmber) begin truE <- true end"""
        expect = "func,fUnc,(,number,nUmber,),begin,truE,<-,true,end,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,176))
        input = """ \"str1\" \"\"iden11\"\" \"\"\"str111\"\"\" "" """
        expect = "str1,,iden11,,,str111,,,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,177))
        input = """ "## Comment '\" \\'" " """
        expect = """## Comment '" \\'" ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,178))
        input = """ " '" \'" '\" \\'" " """
        expect = """ '" \'" '\" \\'" ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,179))
        input = """ " \\b \\t \\r \\n \\f \\' " """
        expect = """ \\b \\t \\r \\n \\f \\' ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,180))
        input = """ " \[]" """
        expect = """Illegal Escape In String:  \["""
        self.assertTrue(TestLexer.test(input,expect,181))
        input = """ " \\[]" """
        expect = """Illegal Escape In String:  \["""
        self.assertTrue(TestLexer.test(input,expect,182))
        input = """ " '" \'" '\" \\'" '\\" q" """
        expect = """Illegal Escape In String:  '" '" '" \\'" '\\\""""
        self.assertTrue(TestLexer.test(input,expect,183))
        input = """ " '" \'" '\" \\'" \\'\\" " """
        expect = """Illegal Escape In String:  '" '" '" \\'" \\'\\\""""
        self.assertTrue(TestLexer.test(input,expect,184))
        input = """ "\"\"" """
        expect = """,,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,185))
        input = """ "'"" """
        expect = """'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,186))
        input = """ class1.attr """
        expect = """class1,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,187))
        input = """ class1->attr """
        expect = """class1,-,>,attr,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,188))
        input = """ \"\"\"python long string\"\"\" """
        expect = """,python long string,,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,189))
        input = """ for(int i; c loop stmt) """
        expect = """for,(,int,i,Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,190))
        input = """ if(expr) {c block stmt} """
        expect = """if,(,expr,),Error Token {"""
        self.assertTrue(TestLexer.test(input,expect,191))
        input = """ <attribute> """
        expect = """<,attribute,>,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,192))
        input = """ _[]][] """
        expect = """_,[,],],[,],<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,193))
        input = """func fun(number &ref) """
        expect = """func,fun,(,number,Error Token &"""
        self.assertTrue(TestLexer.test(input,expect,194))
        input = """not bool = !bool"""
        expect = """not,bool,=,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,195))
        input = """a&&b"""
        expect = """a,Error Token &"""
        self.assertTrue(TestLexer.test(input,expect,196))
        input = """a||b"""
        expect = """a,Error Token |"""
        self.assertTrue(TestLexer.test(input,expect,197))
        input = """a^b"""
        expect = """a,Error Token ^"""
        self.assertTrue(TestLexer.test(input,expect,198))
        input = """ \"\"\"\"\"\"\"\"\"\"\"\" \""" super long '" ""\" """
        expect = """,,,,,,, super long '" ,,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,199))
