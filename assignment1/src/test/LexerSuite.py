import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_primitive(self):
        """basics"""
        self.assertTrue(TestLexer.test("true false number bool string return var dynamic func for until by break continue if else elif begin end not and or + - * / % = <- != < <= > >= ... == ( [ , ] )",
                                       "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,(,[,,,],),<EOF>"
                                      ,100))
        self.assertTrue(TestLexer.test("!===","!=,==,<EOF>",101))
        """identifiers"""
        self.assertTrue(TestLexer.test("i J _ ab aB a0 a_ B1 Bx BQ B_ _x _Y _8 _______ printer vAr _xy123"
                                      ,"i,J,_,ab,aB,a0,a_,B1,Bx,BQ,B_,_x,_Y,_8,_______,printer,vAr,_xy123,<EOF>"
                                      ,102))
        self.assertTrue(TestLexer.test("_!invalid","_,Error Token !",103))
        self.assertTrue(TestLexer.test("1nvalid","1,nvalid,<EOF>",104))
        self.assertTrue(TestLexer.test("?nvalid","Error Token ?",105))
        
        """numbers"""
        self.assertTrue(TestLexer.test("0 10. 192376182 57.21 27.8e1 21E+4 5e-2 0.00E+00"
                                      ,"0,10.,192376182,57.21,27.8e1,21E+4,5e-2,0.00E+00,<EOF>"
                                      ,106))
        self.assertTrue(TestLexer.test("Invalid number 1.2.3","Invalid,number,1.2,Error Token .",107))
        self.assertTrue(TestLexer.test("Valid number question mark 0e","Valid,number,question,mark,0,e,<EOF>",108))
        
        """strings"""
        self.assertTrue(TestLexer.test(""" "" """
                                      ,""",<EOF>"""
                                      ,109))
        self.assertTrue(TestLexer.test(""" "This's a valid string" """
                                      ,"""This's a valid string,<EOF>"""
                                      ,110))
        self.assertTrue(TestLexer.test(""" "Simon says: '\"This is valid" """
                                      ,"""Simon says: '\"This is valid,<EOF>"""
                                      ,111))
        self.assertTrue(TestLexer.test(""" "Another  \b \f \' valid \t stri\\ng yeah" """
                                      ,"""Another  \b \f \' valid \t stri\\ng yeah,<EOF>"""
                                      ,112))
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John?'"" """
                                      ,"""He asked me: '"Where is John?'",<EOF>"""
                                      ,113))
        self.assertTrue(TestLexer.test(""" "\b\f\t\'\\" """
                                      ,"""\b\f\t\'\\,<EOF>"""
                                      ,114))
    
        """unclosed string"""
        self.assertTrue(TestLexer.test(""" "test """
                                      ,"""Unclosed String: test """
                                      ,115))
        self.assertTrue(TestLexer.test(""" "quotation: '" """
                                      ,"""Unclosed String: quotation: '" """
                                      ,116))
        self.assertTrue(TestLexer.test(""" "escape \b \f \' \t \\"""
                                      ,"""Unclosed String: escape \b \f \' \t \\"""
                                      ,117))    
        self.assertTrue(TestLexer.test(""" " """
                                      ,"""Unclosed String:  """
                                      ,118))    
        self.assertTrue(TestLexer.test(""" "\b\f\t\\\'" """
                                      ,"""Unclosed String: \b\f\t\\\'" """
                                      ,119)) 
        """illegal escape"""
        self.assertTrue(TestLexer.test(""" "\a" """
                                      ,""" """
                                      ,120)) 
    
        """separators"""
        self.assertTrue(TestLexer.test("[,](\n)","[,,,],(,\n,),<EOF>",130))
        self.assertTrue(TestLexer.test("a\n\n\n\n","a,\n,\n,\n,\n,<EOF>",131))    
        self.assertTrue(TestLexer.test("[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]","[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]],<EOF>",130))
        
    def test_comments(self):   
        """comments test"""
        self.assertTrue(TestLexer.test("## A valid comment","<EOF>",150))
        self.assertTrue(TestLexer.test("  ##stillavalidcomment","<EOF>",151))
        self.assertTrue(TestLexer.test("b\n## After slash n","b,\n,<EOF>",152))  
        self.assertTrue(TestLexer.test("b\n## Between slash n\na","b,\n,\n,a,<EOF>",153))
        self.assertTrue(TestLexer.test("## Before slash n\na","\n,a,<EOF>",154))
        self.assertTrue(TestLexer.test("a ## Valid","a,<EOF>",155))