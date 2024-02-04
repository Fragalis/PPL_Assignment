# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\5\3{\n\3\3\3\5\3~\n\3\3\4\6\4\u0081")
        buf.write("\n\4\r\4\16\4\u0082\3\5\3\5\7\5\u0087\n\5\f\5\16\5\u008a")
        buf.write("\13\5\3\6\3\6\5\6\u008e\n\6\3\6\6\6\u0091\n\6\r\6\16\6")
        buf.write("\u0092\3\7\3\7\5\7\u0097\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\b\u00a1\n\b\f\b\16\b\u00a4\13\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\5\t\u00ab\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)")
        buf.write("\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u0154\n\64\f\64\16\64\u0157\13\64\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u015d\n\65\f\65\16\65\u0160\13\65\3\66")
        buf.write("\6\66\u0163\n\66\r\66\16\66\u0164\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0171\n\67\f\67\16")
        buf.write("\67\u0174\13\67\3\67\3\67\38\38\38\38\38\78\u017d\n8\f")
        buf.write("8\168\u0180\138\38\38\38\38\39\39\39\2\2:\3\3\5\4\7\2")
        buf.write("\t\2\13\2\r\5\17\6\21\2\23\7\25\b\27\t\31\n\33\13\35\f")
        buf.write("\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27\65")
        buf.write("\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(")
        buf.write("W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66\3\2\16\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\3\2))\3\2$$\n\2")
        buf.write("$$))^^ddhhppttvv\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\n\f\17\17\"\"\t\2))^^ddhhppttvv\2\u0198\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\3s\3\2\2\2\5x\3\2\2\2\7\u0080\3\2\2\2\t\u0084")
        buf.write("\3\2\2\2\13\u008b\3\2\2\2\r\u0096\3\2\2\2\17\u0098\3\2")
        buf.write("\2\2\21\u00a8\3\2\2\2\23\u00ac\3\2\2\2\25\u00b1\3\2\2")
        buf.write("\2\27\u00b7\3\2\2\2\31\u00be\3\2\2\2\33\u00c3\3\2\2\2")
        buf.write("\35\u00ca\3\2\2\2\37\u00d1\3\2\2\2!\u00d5\3\2\2\2#\u00dd")
        buf.write("\3\2\2\2%\u00e2\3\2\2\2\'\u00e6\3\2\2\2)\u00ec\3\2\2\2")
        buf.write("+\u00ef\3\2\2\2-\u00f5\3\2\2\2/\u00fe\3\2\2\2\61\u0101")
        buf.write("\3\2\2\2\63\u0106\3\2\2\2\65\u010b\3\2\2\2\67\u0111\3")
        buf.write("\2\2\29\u0115\3\2\2\2;\u0119\3\2\2\2=\u011c\3\2\2\2?\u0120")
        buf.write("\3\2\2\2A\u0122\3\2\2\2C\u0124\3\2\2\2E\u0126\3\2\2\2")
        buf.write("G\u0128\3\2\2\2I\u012a\3\2\2\2K\u012c\3\2\2\2M\u012f\3")
        buf.write("\2\2\2O\u0132\3\2\2\2Q\u0135\3\2\2\2S\u0138\3\2\2\2U\u013a")
        buf.write("\3\2\2\2W\u013c\3\2\2\2Y\u0140\3\2\2\2[\u0143\3\2\2\2")
        buf.write("]\u0145\3\2\2\2_\u0147\3\2\2\2a\u0149\3\2\2\2c\u014b\3")
        buf.write("\2\2\2e\u014d\3\2\2\2g\u014f\3\2\2\2i\u015a\3\2\2\2k\u0162")
        buf.write("\3\2\2\2m\u0168\3\2\2\2o\u0177\3\2\2\2q\u0185\3\2\2\2")
        buf.write("st\7o\2\2tu\7c\2\2uv\7k\2\2vw\7p\2\2w\4\3\2\2\2xz\5\7")
        buf.write("\4\2y{\5\t\5\2zy\3\2\2\2z{\3\2\2\2{}\3\2\2\2|~\5\13\6")
        buf.write("\2}|\3\2\2\2}~\3\2\2\2~\6\3\2\2\2\177\u0081\t\2\2\2\u0080")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\b\3\2\2\2\u0084\u0088\7\60\2\2\u0085")
        buf.write("\u0087\t\2\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\n\3\2\2")
        buf.write("\2\u008a\u0088\3\2\2\2\u008b\u008d\t\3\2\2\u008c\u008e")
        buf.write("\t\4\2\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u0091\t\2\2\2\u0090\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\f\3\2\2\2\u0094\u0097\5\23\n\2\u0095\u0097")
        buf.write("\5\25\13\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\16\3\2\2\2\u0098\u00a2\7$\2\2\u0099\u00a1\5\21\t\2\u009a")
        buf.write("\u00a1\n\5\2\2\u009b\u009c\7)\2\2\u009c\u00a1\7$\2\2\u009d")
        buf.write("\u009e\7^\2\2\u009e\u009f\t\6\2\2\u009f\u00a1\t\7\2\2")
        buf.write("\u00a0\u0099\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0\u009b\3")
        buf.write("\2\2\2\u00a0\u009d\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a5\u00a6\7$\2\2\u00a6\u00a7\b\b\2\2")
        buf.write("\u00a7\20\3\2\2\2\u00a8\u00aa\7^\2\2\u00a9\u00ab\t\b\2")
        buf.write("\2\u00aa\u00a9\3\2\2\2\u00ab\22\3\2\2\2\u00ac\u00ad\7")
        buf.write("v\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7w\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\26\3\2\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7w\2\2\u00b9\u00ba\7o\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7t\2\2\u00bd\30\3\2\2\2\u00be\u00bf")
        buf.write("\7d\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7n\2\2\u00c2\32\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\34\3\2\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7w\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7p\2\2\u00d0\36")
        buf.write("\3\2\2\2\u00d1\u00d2\7x\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7")
        buf.write("\7{\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da")
        buf.write("\7o\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7e\2\2\u00dc\"")
        buf.write("\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7e\2\2\u00e1$\3\2\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5&\3")
        buf.write("\2\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7n\2\2\u00eb(\3")
        buf.write("\2\2\2\u00ec\u00ed\7d\2\2\u00ed\u00ee\7{\2\2\u00ee*\3")
        buf.write("\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7m\2\2\u00f4,\3")
        buf.write("\2\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7g\2\2\u00fd.\3")
        buf.write("\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7h\2\2\u0100\60")
        buf.write("\3\2\2\2\u0101\u0102\7g\2\2\u0102\u0103\7n\2\2\u0103\u0104")
        buf.write("\7u\2\2\u0104\u0105\7g\2\2\u0105\62\3\2\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7h\2\2\u010a\64\3\2\2\2\u010b\u010c\7d\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u010e\7i\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\66\3\2\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7p\2\2\u0113\u0114\7f\2\2\u01148\3\2\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7q\2\2\u0117\u0118\7v\2\2\u0118:\3")
        buf.write("\2\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b<\3")
        buf.write("\2\2\2\u011c\u011d\7c\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7f\2\2\u011f>\3\2\2\2\u0120\u0121\7*\2\2\u0121@\3\2\2")
        buf.write("\2\u0122\u0123\7+\2\2\u0123B\3\2\2\2\u0124\u0125\7]\2")
        buf.write("\2\u0125D\3\2\2\2\u0126\u0127\7_\2\2\u0127F\3\2\2\2\u0128")
        buf.write("\u0129\7.\2\2\u0129H\3\2\2\2\u012a\u012b\7\f\2\2\u012b")
        buf.write("J\3\2\2\2\u012c\u012d\7>\2\2\u012d\u012e\7/\2\2\u012e")
        buf.write("L\3\2\2\2\u012f\u0130\7#\2\2\u0130\u0131\7?\2\2\u0131")
        buf.write("N\3\2\2\2\u0132\u0133\7@\2\2\u0133\u0134\7?\2\2\u0134")
        buf.write("P\3\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137")
        buf.write("R\3\2\2\2\u0138\u0139\7@\2\2\u0139T\3\2\2\2\u013a\u013b")
        buf.write("\7>\2\2\u013bV\3\2\2\2\u013c\u013d\7\60\2\2\u013d\u013e")
        buf.write("\7\60\2\2\u013e\u013f\7\60\2\2\u013fX\3\2\2\2\u0140\u0141")
        buf.write("\7?\2\2\u0141\u0142\7?\2\2\u0142Z\3\2\2\2\u0143\u0144")
        buf.write("\7?\2\2\u0144\\\3\2\2\2\u0145\u0146\7-\2\2\u0146^\3\2")
        buf.write("\2\2\u0147\u0148\7/\2\2\u0148`\3\2\2\2\u0149\u014a\7,")
        buf.write("\2\2\u014ab\3\2\2\2\u014b\u014c\7\61\2\2\u014cd\3\2\2")
        buf.write("\2\u014d\u014e\7\'\2\2\u014ef\3\2\2\2\u014f\u0150\7%\2")
        buf.write("\2\u0150\u0151\7%\2\2\u0151\u0155\3\2\2\2\u0152\u0154")
        buf.write("\n\t\2\2\u0153\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2")
        buf.write("\u0157\u0155\3\2\2\2\u0158\u0159\b\64\3\2\u0159h\3\2\2")
        buf.write("\2\u015a\u015e\t\n\2\2\u015b\u015d\t\13\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015fj\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0163\t\f\2\2\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166\u0167\b\66\3\2\u0167l\3\2\2\2\u0168\u0172")
        buf.write("\7$\2\2\u0169\u0171\5\21\t\2\u016a\u0171\n\5\2\2\u016b")
        buf.write("\u016c\7)\2\2\u016c\u0171\7$\2\2\u016d\u016e\7^\2\2\u016e")
        buf.write("\u016f\t\6\2\2\u016f\u0171\t\7\2\2\u0170\u0169\3\2\2\2")
        buf.write("\u0170\u016a\3\2\2\2\u0170\u016b\3\2\2\2\u0170\u016d\3")
        buf.write("\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0176\b\67\4\2\u0176n\3\2\2\2\u0177\u017e\7$\2\2\u0178")
        buf.write("\u017d\5\21\t\2\u0179\u017d\n\5\2\2\u017a\u017b\7)\2\2")
        buf.write("\u017b\u017d\7$\2\2\u017c\u0178\3\2\2\2\u017c\u0179\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0182\7^\2\2\u0182\u0183\n\r\2\2")
        buf.write("\u0183\u0184\b8\5\2\u0184p\3\2\2\2\u0185\u0186\13\2\2")
        buf.write("\2\u0186\u0187\b9\6\2\u0187r\3\2\2\2\24\2z}\u0082\u0088")
        buf.write("\u008d\u0092\u0096\u00a0\u00a2\u00aa\u0155\u015e\u0164")
        buf.write("\u0170\u0172\u017c\u017e\7\3\b\2\b\2\2\3\67\3\38\4\39")
        buf.write("\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBERLIT = 2
    BOOLLIT = 3
    STRINGLIT = 4
    TRUE = 5
    FALSE = 6
    NUMBER = 7
    BOOL = 8
    STRING = 9
    RETURN = 10
    VAR = 11
    DYNAMIC = 12
    FUNC = 13
    FOR = 14
    UNTIL = 15
    BY = 16
    BREAK = 17
    CONTINUE = 18
    IF = 19
    ELSE = 20
    ELIF = 21
    BEGIN = 22
    END = 23
    NOT = 24
    OR = 25
    AND = 26
    LEFT_PAR = 27
    RIGHT_PAR = 28
    LEFT_BRACKET = 29
    RIGHT_BRACKET = 30
    COMMA = 31
    NEWLN = 32
    ASSIGN = 33
    NOTEQ = 34
    GRATER_EQ = 35
    LESS_EQ = 36
    GRATER = 37
    LESS = 38
    STR_CONCAT = 39
    STR_EQ = 40
    EQ = 41
    NUM_ADD = 42
    NUM_SUB = 43
    NUM_MUL = 44
    NUM_DIV = 45
    NUM_REMAINDER = 46
    COMMENT = 47
    IDENTIFIER = 48
    WS = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'or'", "'and'", "'('", "')'", 
            "'['", "']'", "','", "'\n'", "'<-'", "'!='", "'>='", "'<='", 
            "'>'", "'<'", "'...'", "'=='", "'='", "'+'", "'-'", "'*'", "'/'", 
            "'%'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBERLIT", "BOOLLIT", "STRINGLIT", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "OR", "AND", "LEFT_PAR", "RIGHT_PAR", "LEFT_BRACKET", 
            "RIGHT_BRACKET", "COMMA", "NEWLN", "ASSIGN", "NOTEQ", "GRATER_EQ", 
            "LESS_EQ", "GRATER", "LESS", "STR_CONCAT", "STR_EQ", "EQ", "NUM_ADD", 
            "NUM_SUB", "NUM_MUL", "NUM_DIV", "NUM_REMAINDER", "COMMENT", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "NUMBERLIT", "INTPART", "DECPART", "EXTPART", 
                  "BOOLLIT", "STRINGLIT", "ESCAPE_SEQUENCE", "TRUE", "FALSE", 
                  "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "OR", "AND", "LEFT_PAR", 
                  "RIGHT_PAR", "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", 
                  "NEWLN", "ASSIGN", "NOTEQ", "GRATER_EQ", "LESS_EQ", "GRATER", 
                  "LESS", "STR_CONCAT", "STR_EQ", "EQ", "NUM_ADD", "NUM_SUB", 
                  "NUM_MUL", "NUM_DIV", "NUM_REMAINDER", "COMMENT", "IDENTIFIER", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRINGLIT_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		self.text = self.text[1:]
            		raise UncloseString(self.text)
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		self.text = self.text[1:] 
            		raise IllegalEscape(self.text)
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


