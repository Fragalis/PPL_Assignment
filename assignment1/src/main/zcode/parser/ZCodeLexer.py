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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0169\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3-\3-\3-\3-\7-\u0115\n-\f-\16-\u0118")
        buf.write("\13-\3.\6.\u011b\n.\r.\16.\u011c\3.\3.\7.\u0121\n.\f.")
        buf.write("\16.\u0124\13.\5.\u0126\n.\3.\3.\5.\u012a\n.\3.\6.\u012d")
        buf.write("\n.\r.\16.\u012e\5.\u0131\n.\3/\3/\5/\u0135\n/\3\60\3")
        buf.write("\60\3\60\3\60\7\60\u013b\n\60\f\60\16\60\u013e\13\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\7\61\u0145\n\61\f\61\16\61\u0148")
        buf.write("\13\61\3\62\6\62\u014b\n\62\r\62\16\62\u014c\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\7\64\u0158\n\64\f")
        buf.write("\64\16\64\u015b\13\64\3\64\3\64\3\65\3\65\3\65\3\65\7")
        buf.write("\65\u0163\n\65\f\65\16\65\u0166\13\65\3\65\3\65\3\u013c")
        buf.write("\2\66\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27")
        buf.write("\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27")
        buf.write("/\30\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%")
        buf.write("K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65\3\2\r\3")
        buf.write("\2\62;\4\2\f\f\17\17\4\2GGgg\4\2--//\t\2))^^ddhhppttv")
        buf.write("v\6\2\f\f\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13")
        buf.write("\16\17\"\"\6\2\n\f\16\17$$^^\3\2^^\2\u0177\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2")
        buf.write("\2\2\5m\3\2\2\2\7r\3\2\2\2\tx\3\2\2\2\13\177\3\2\2\2\r")
        buf.write("\u0084\3\2\2\2\17\u008b\3\2\2\2\21\u0092\3\2\2\2\23\u0096")
        buf.write("\3\2\2\2\25\u009e\3\2\2\2\27\u00a3\3\2\2\2\31\u00a7\3")
        buf.write("\2\2\2\33\u00ad\3\2\2\2\35\u00b0\3\2\2\2\37\u00b6\3\2")
        buf.write("\2\2!\u00bf\3\2\2\2#\u00c2\3\2\2\2%\u00c7\3\2\2\2\'\u00cc")
        buf.write("\3\2\2\2)\u00d2\3\2\2\2+\u00d6\3\2\2\2-\u00da\3\2\2\2")
        buf.write("/\u00de\3\2\2\2\61\u00e1\3\2\2\2\63\u00e3\3\2\2\2\65\u00e5")
        buf.write("\3\2\2\2\67\u00e7\3\2\2\29\u00e9\3\2\2\2;\u00eb\3\2\2")
        buf.write("\2=\u00ed\3\2\2\2?\u00f0\3\2\2\2A\u00f3\3\2\2\2C\u00f6")
        buf.write("\3\2\2\2E\u00f9\3\2\2\2G\u00fd\3\2\2\2I\u0100\3\2\2\2")
        buf.write("K\u0102\3\2\2\2M\u0104\3\2\2\2O\u0106\3\2\2\2Q\u0108\3")
        buf.write("\2\2\2S\u010a\3\2\2\2U\u010c\3\2\2\2W\u010e\3\2\2\2Y\u0110")
        buf.write("\3\2\2\2[\u011a\3\2\2\2]\u0134\3\2\2\2_\u0136\3\2\2\2")
        buf.write("a\u0142\3\2\2\2c\u014a\3\2\2\2e\u0150\3\2\2\2g\u0153\3")
        buf.write("\2\2\2i\u015e\3\2\2\2kl\t\2\2\2l\4\3\2\2\2mn\7v\2\2no")
        buf.write("\7t\2\2op\7w\2\2pq\7g\2\2q\6\3\2\2\2rs\7h\2\2st\7c\2\2")
        buf.write("tu\7n\2\2uv\7u\2\2vw\7g\2\2w\b\3\2\2\2xy\7p\2\2yz\7w\2")
        buf.write("\2z{\7o\2\2{|\7d\2\2|}\7g\2\2}~\7t\2\2~\n\3\2\2\2\177")
        buf.write("\u0080\7d\2\2\u0080\u0081\7q\2\2\u0081\u0082\7q\2\2\u0082")
        buf.write("\u0083\7n\2\2\u0083\f\3\2\2\2\u0084\u0085\7u\2\2\u0085")
        buf.write("\u0086\7v\2\2\u0086\u0087\7t\2\2\u0087\u0088\7k\2\2\u0088")
        buf.write("\u0089\7p\2\2\u0089\u008a\7i\2\2\u008a\16\3\2\2\2\u008b")
        buf.write("\u008c\7t\2\2\u008c\u008d\7g\2\2\u008d\u008e\7v\2\2\u008e")
        buf.write("\u008f\7w\2\2\u008f\u0090\7t\2\2\u0090\u0091\7p\2\2\u0091")
        buf.write("\20\3\2\2\2\u0092\u0093\7x\2\2\u0093\u0094\7c\2\2\u0094")
        buf.write("\u0095\7t\2\2\u0095\22\3\2\2\2\u0096\u0097\7f\2\2\u0097")
        buf.write("\u0098\7{\2\2\u0098\u0099\7p\2\2\u0099\u009a\7c\2\2\u009a")
        buf.write("\u009b\7o\2\2\u009b\u009c\7k\2\2\u009c\u009d\7e\2\2\u009d")
        buf.write("\24\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7w\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\u00a2\7e\2\2\u00a2\26\3\2\2\2\u00a3")
        buf.write("\u00a4\7h\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7t\2\2\u00a6")
        buf.write("\30\3\2\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7v\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7n\2\2\u00ac")
        buf.write("\32\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af\7{\2\2\u00af")
        buf.write("\34\3\2\2\2\u00b0\u00b1\7d\2\2\u00b1\u00b2\7t\2\2\u00b2")
        buf.write("\u00b3\7g\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7m\2\2\u00b5")
        buf.write("\36\3\2\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8\7q\2\2\u00b8")
        buf.write("\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7k\2\2\u00bb")
        buf.write("\u00bc\7p\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write(" \3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7h\2\2\u00c1")
        buf.write("\"\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7n\2\2\u00c4")
        buf.write("\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6$\3\2\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7k\2\2\u00ca")
        buf.write("\u00cb\7h\2\2\u00cb&\3\2\2\2\u00cc\u00cd\7d\2\2\u00cd")
        buf.write("\u00ce\7g\2\2\u00ce\u00cf\7i\2\2\u00cf\u00d0\7k\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1(\3\2\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\u00d4\7p\2\2\u00d4\u00d5\7f\2\2\u00d5*\3\2\2\2\u00d6")
        buf.write("\u00d7\7p\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write(",\3\2\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\u00dd\7f\2\2\u00dd.\3\2\2\2\u00de\u00df\7q\2\2\u00df")
        buf.write("\u00e0\7t\2\2\u00e0\60\3\2\2\2\u00e1\u00e2\7\f\2\2\u00e2")
        buf.write("\62\3\2\2\2\u00e3\u00e4\7*\2\2\u00e4\64\3\2\2\2\u00e5")
        buf.write("\u00e6\7+\2\2\u00e6\66\3\2\2\2\u00e7\u00e8\7]\2\2\u00e8")
        buf.write("8\3\2\2\2\u00e9\u00ea\7_\2\2\u00ea:\3\2\2\2\u00eb\u00ec")
        buf.write("\7.\2\2\u00ec<\3\2\2\2\u00ed\u00ee\7>\2\2\u00ee\u00ef")
        buf.write("\7/\2\2\u00ef>\3\2\2\2\u00f0\u00f1\7#\2\2\u00f1\u00f2")
        buf.write("\7?\2\2\u00f2@\3\2\2\2\u00f3\u00f4\7@\2\2\u00f4\u00f5")
        buf.write("\7?\2\2\u00f5B\3\2\2\2\u00f6\u00f7\7>\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8D\3\2\2\2\u00f9\u00fa\7\60\2\2\u00fa\u00fb")
        buf.write("\7\60\2\2\u00fb\u00fc\7\60\2\2\u00fcF\3\2\2\2\u00fd\u00fe")
        buf.write("\7?\2\2\u00fe\u00ff\7?\2\2\u00ffH\3\2\2\2\u0100\u0101")
        buf.write("\7-\2\2\u0101J\3\2\2\2\u0102\u0103\7/\2\2\u0103L\3\2\2")
        buf.write("\2\u0104\u0105\7,\2\2\u0105N\3\2\2\2\u0106\u0107\7\61")
        buf.write("\2\2\u0107P\3\2\2\2\u0108\u0109\7\'\2\2\u0109R\3\2\2\2")
        buf.write("\u010a\u010b\7@\2\2\u010bT\3\2\2\2\u010c\u010d\7>\2\2")
        buf.write("\u010dV\3\2\2\2\u010e\u010f\7?\2\2\u010fX\3\2\2\2\u0110")
        buf.write("\u0111\7%\2\2\u0111\u0112\7%\2\2\u0112\u0116\3\2\2\2\u0113")
        buf.write("\u0115\n\3\2\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117Z\3\2\2")
        buf.write("\2\u0118\u0116\3\2\2\2\u0119\u011b\5\3\2\2\u011a\u0119")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011a\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u0125\3\2\2\2\u011e\u0122\7\60\2")
        buf.write("\2\u011f\u0121\5\3\2\2\u0120\u011f\3\2\2\2\u0121\u0124")
        buf.write("\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u011e\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126\u0130\3\2\2\2\u0127\u0129\t")
        buf.write("\4\2\2\u0128\u012a\t\5\2\2\u0129\u0128\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u012d\5\3\2\2\u012c")
        buf.write("\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u0127\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\\\3\2\2\2\u0132\u0135")
        buf.write("\5\5\3\2\u0133\u0135\5\7\4\2\u0134\u0132\3\2\2\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135^\3\2\2\2\u0136\u013c\7$\2\2\u0137")
        buf.write("\u0138\7^\2\2\u0138\u013b\t\6\2\2\u0139\u013b\n\7\2\2")
        buf.write("\u013a\u0137\3\2\2\2\u013a\u0139\3\2\2\2\u013b\u013e\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\7$\2\2\u0140")
        buf.write("\u0141\b\60\2\2\u0141`\3\2\2\2\u0142\u0146\t\b\2\2\u0143")
        buf.write("\u0145\t\t\2\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2")
        buf.write("\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147b\3\2\2")
        buf.write("\2\u0148\u0146\3\2\2\2\u0149\u014b\t\n\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\b\62\3")
        buf.write("\2\u014fd\3\2\2\2\u0150\u0151\13\2\2\2\u0151\u0152\b\63")
        buf.write("\4\2\u0152f\3\2\2\2\u0153\u0159\7$\2\2\u0154\u0155\7^")
        buf.write("\2\2\u0155\u0158\t\6\2\2\u0156\u0158\n\13\2\2\u0157\u0154")
        buf.write("\3\2\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015c\u015d\b\64\5\2\u015dh\3\2\2")
        buf.write("\2\u015e\u0164\7$\2\2\u015f\u0160\7^\2\2\u0160\u0163\n")
        buf.write("\6\2\2\u0161\u0163\n\f\2\2\u0162\u015f\3\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0167\u0168\b\65\6\2\u0168j\3\2\2\2\23\2\u0116\u011c")
        buf.write("\u0122\u0125\u0129\u012e\u0130\u0134\u013a\u013c\u0146")
        buf.write("\u014c\u0157\u0159\u0162\u0164\7\3\60\2\b\2\2\3\63\3\3")
        buf.write("\64\4\3\65\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    NEWLINE = 23
    LP = 24
    RP = 25
    LB = 26
    RB = 27
    COMMA = 28
    ASSIGN = 29
    NEQ = 30
    GTEQ = 31
    LTEQ = 32
    CONCAT = 33
    STRING_EQ = 34
    PLUS = 35
    MINUS = 36
    MUL = 37
    DIV = 38
    MOD = 39
    GT = 40
    LT = 41
    NUMBER_EQ = 42
    COMMENT = 43
    NUMBER_L = 44
    BOOL_L = 45
    STRING_L = 46
    IDENTIFIERS = 47
    WHITESPACES = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'\n'", "'('", "')'", "'['", 
            "']'", "','", "'<-'", "'!='", "'>='", "'<='", "'...'", "'=='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "NEWLINE", 
            "LP", "RP", "LB", "RB", "COMMA", "ASSIGN", "NEQ", "GTEQ", "LTEQ", 
            "CONCAT", "STRING_EQ", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "GT", "LT", "NUMBER_EQ", "COMMENT", "NUMBER_L", "BOOL_L", "STRING_L", 
            "IDENTIFIERS", "WHITESPACES", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "DIGIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NOT", "AND", "OR", "NEWLINE", "LP", "RP", "LB", "RB", 
                  "COMMA", "ASSIGN", "NEQ", "GTEQ", "LTEQ", "CONCAT", "STRING_EQ", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", "NUMBER_EQ", 
                  "COMMENT", "NUMBER_L", "BOOL_L", "STRING_L", "IDENTIFIERS", 
                  "WHITESPACES", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[46] = self.STRING_L_action 
            actions[49] = self.ERROR_CHAR_action 
            actions[50] = self.UNCLOSE_STRING_action 
            actions[51] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_L_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		self.text = self.text[1:]
            		raise ErrorToken(self.text)
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		self.text = self.text[1:]
            		raise ErrorToken(self.text)
            	
     


