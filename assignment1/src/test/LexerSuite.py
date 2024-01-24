import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_primitive(self):
        """basics"""
        self.assertTrue(TestLexer.test("true false number bool string return var dynamic func for until by break continue if else elif begin end not and or + - * / % = <- != < <= > >= ... == ( [ , ] )",
                                       "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,(,[,,,],),<EOF>"
                                      ,100))
    
        """numbers"""
        self.assertTrue(TestLexer.test("0 10. 192376182 57.21 27.8e1 21E+4 5e-2 0.00E+00"
                                      ,"0,10.,192376182,57.21,27.8e1,21E+4,5e-2,0.00E+00,<EOF>"
                                      ,101))
        
        """strings"""
        self.assertTrue(TestLexer.test("\"This's a valid string\""
                                      ,"This's a valid string,<EOF>"
                                      ,102))
        # self.assertTrue(TestLexer.test("\'Simon says: '\"This is valid\""
        #                               ,"Simon says: '\"This is valid,<EOF>"
        #                               ,103))
        self.assertTrue(TestLexer.test("\"Another  \b \f \' valid \t stri\\ng yeah\""
                                      ,"Another  \b \f \' valid \t stri\\ng yeah,<EOF>"
                                      ,104))
        
        """newliners"""
        self.assertTrue(TestLexer.test("\n"
                                      ,"\n,<EOF>"
                                      ,105))
        self.assertTrue(TestLexer.test("a\n\n\n\n"
                                      ,"a,\n,\n,\n,\n,<EOF>"
                                      ,106))
        
    def test_comments(self):   
        """comments test"""
        self.assertTrue(TestLexer.test("## A valid comment","## A valid comment,<EOF>",110))
        self.assertTrue(TestLexer.test("  ##stillavalidcomment","##stillavalidcomment,<EOF>",111))
        self.assertTrue(TestLexer.test("b\n## After slash n","b,\n,## After slash n,<EOF>",112))  
        self.assertTrue(TestLexer.test("b\n## Between slash n\na","b,\n,## Between slash n,\n,a,<EOF>",113))
        self.assertTrue(TestLexer.test("## Before slash n\na","## Before slash n,\n,a,<EOF>",114))
        self.assertTrue(TestLexer.test("a ## Valid until parse","a,## Valid until parse,<EOF>",115))
    def test_error(self):
        """ERROR_TOKEN"""
        self.assertTrue(TestLexer.test("a# Invalid","a,Error Token #",120))   
        
        """UNCLOSED_STRING"""
        
        """ILLEGAL_ESCAPE"""    
    