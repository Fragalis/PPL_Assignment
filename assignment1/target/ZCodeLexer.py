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
        buf.write("\u0197\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\5\3\u0087\n\3\3\3\5\3\u008a\n\3\3\4\3\4\5\4\u008e")
        buf.write("\n\4\3\5\3\5\3\5\3\5\7\5\u0094\n\5\f\5\16\5\u0097\13\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\60\7\60\u0142\n\60\f\60\16\60\u0145")
        buf.write("\13\60\3\61\3\61\3\61\3\61\7\61\u014b\n\61\f\61\16\61")
        buf.write("\u014e\13\61\3\61\3\61\3\62\6\62\u0153\n\62\r\62\16\62")
        buf.write("\u0154\3\62\3\62\3\63\3\63\3\64\3\64\3\65\6\65\u015e\n")
        buf.write("\65\r\65\16\65\u015f\3\66\3\66\7\66\u0164\n\66\f\66\16")
        buf.write("\66\u0167\13\66\3\67\3\67\5\67\u016b\n\67\3\67\6\67\u016e")
        buf.write("\n\67\r\67\16\67\u016f\38\38\39\39\39\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\7=\u0183\n=\f=\16=\u0186\13=\3=\3")
        buf.write("=\3>\3>\3>\3>\7>\u018e\n>\f>\16>\u0191\13>\3>\3>\3?\3")
        buf.write("?\3?\2\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m")
        buf.write("\2o\2q\2s\2u\2w\2y\64{\65}\66\3\2\f\4\2\f\f\17\17\5\2")
        buf.write("\n\13\16\17\"\"\5\2C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2")
        buf.write("$$\5\2\f\f\17\17$$\t\2))^^ddhhppttvv\n\2$$))^^ddhhppt")
        buf.write("tvv\2\u01a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0084\3")
        buf.write("\2\2\2\7\u008d\3\2\2\2\t\u008f\3\2\2\2\13\u009b\3\2\2")
        buf.write("\2\r\u00a0\3\2\2\2\17\u00a6\3\2\2\2\21\u00ad\3\2\2\2\23")
        buf.write("\u00b2\3\2\2\2\25\u00b9\3\2\2\2\27\u00c0\3\2\2\2\31\u00c4")
        buf.write("\3\2\2\2\33\u00cc\3\2\2\2\35\u00d1\3\2\2\2\37\u00d5\3")
        buf.write("\2\2\2!\u00db\3\2\2\2#\u00de\3\2\2\2%\u00e4\3\2\2\2\'")
        buf.write("\u00ed\3\2\2\2)\u00f0\3\2\2\2+\u00f5\3\2\2\2-\u00fa\3")
        buf.write("\2\2\2/\u0100\3\2\2\2\61\u0104\3\2\2\2\63\u0108\3\2\2")
        buf.write("\2\65\u010c\3\2\2\2\67\u010f\3\2\2\29\u0111\3\2\2\2;\u0113")
        buf.write("\3\2\2\2=\u0115\3\2\2\2?\u0117\3\2\2\2A\u0119\3\2\2\2")
        buf.write("C\u011b\3\2\2\2E\u011e\3\2\2\2G\u0121\3\2\2\2I\u0124\3")
        buf.write("\2\2\2K\u0127\3\2\2\2M\u012b\3\2\2\2O\u012e\3\2\2\2Q\u0130")
        buf.write("\3\2\2\2S\u0132\3\2\2\2U\u0134\3\2\2\2W\u0136\3\2\2\2")
        buf.write("Y\u0138\3\2\2\2[\u013a\3\2\2\2]\u013c\3\2\2\2_\u013e\3")
        buf.write("\2\2\2a\u0146\3\2\2\2c\u0152\3\2\2\2e\u0158\3\2\2\2g\u015a")
        buf.write("\3\2\2\2i\u015d\3\2\2\2k\u0161\3\2\2\2m\u0168\3\2\2\2")
        buf.write("o\u0171\3\2\2\2q\u0173\3\2\2\2s\u0176\3\2\2\2u\u0178\3")
        buf.write("\2\2\2w\u017b\3\2\2\2y\u017e\3\2\2\2{\u0189\3\2\2\2}\u0194")
        buf.write("\3\2\2\2\177\u0080\7o\2\2\u0080\u0081\7c\2\2\u0081\u0082")
        buf.write("\7k\2\2\u0082\u0083\7p\2\2\u0083\4\3\2\2\2\u0084\u0086")
        buf.write("\5i\65\2\u0085\u0087\5k\66\2\u0086\u0085\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u008a\5m\67\2")
        buf.write("\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\6\3\2\2")
        buf.write("\2\u008b\u008e\5\13\6\2\u008c\u008e\5\r\7\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\b\3\2\2\2\u008f\u0095")
        buf.write("\5o8\2\u0090\u0094\5u;\2\u0091\u0094\5s:\2\u0092\u0094")
        buf.write("\5q9\2\u0093\u0090\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092")
        buf.write("\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0098\u0099\5o8\2\u0099\u009a\b\5\2\2\u009a\n\3\2\2\2")
        buf.write("\u009b\u009c\7v\2\2\u009c\u009d\7t\2\2\u009d\u009e\7w")
        buf.write("\2\2\u009e\u009f\7g\2\2\u009f\f\3\2\2\2\u00a0\u00a1\7")
        buf.write("h\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\16\3\2\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7o\2\2\u00a9\u00aa")
        buf.write("\7d\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7t\2\2\u00ac\20")
        buf.write("\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7n\2\2\u00b1\22\3\2\2\2\u00b2\u00b3")
        buf.write("\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7i\2\2\u00b8\24")
        buf.write("\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\26\3\2\2\2\u00c0\u00c1\7x\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7t\2\2\u00c3\30\3\2\2\2\u00c4\u00c5")
        buf.write("\7f\2\2\u00c5\u00c6\7{\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8")
        buf.write("\7c\2\2\u00c8\u00c9\7o\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7e\2\2\u00cb\32\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce")
        buf.write("\7w\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7e\2\2\u00d0\34")
        buf.write("\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da \3\2\2\2\u00db\u00dc\7d\2\2\u00dc\u00dd")
        buf.write("\7{\2\2\u00dd\"\3\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3")
        buf.write("\7m\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6")
        buf.write("\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec&\3\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7h\2\2\u00ef(\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4\7g\2\2\u00f4*\3")
        buf.write("\2\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7h\2\2\u00f9,\3\2\2\2\u00fa\u00fb")
        buf.write("\7d\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7i\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7p\2\2\u00ff.\3\2\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101\u0102\7p\2\2\u0102\u0103\7f\2\2\u0103\60")
        buf.write("\3\2\2\2\u0104\u0105\7p\2\2\u0105\u0106\7q\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\62\3\2\2\2\u0108\u0109\7c\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7f\2\2\u010b\64\3\2\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7t\2\2\u010e\66\3\2\2\2\u010f\u0110")
        buf.write("\7*\2\2\u01108\3\2\2\2\u0111\u0112\7+\2\2\u0112:\3\2\2")
        buf.write("\2\u0113\u0114\7]\2\2\u0114<\3\2\2\2\u0115\u0116\7_\2")
        buf.write("\2\u0116>\3\2\2\2\u0117\u0118\7.\2\2\u0118@\3\2\2\2\u0119")
        buf.write("\u011a\7\f\2\2\u011aB\3\2\2\2\u011b\u011c\7>\2\2\u011c")
        buf.write("\u011d\7/\2\2\u011dD\3\2\2\2\u011e\u011f\7#\2\2\u011f")
        buf.write("\u0120\7?\2\2\u0120F\3\2\2\2\u0121\u0122\7@\2\2\u0122")
        buf.write("\u0123\7?\2\2\u0123H\3\2\2\2\u0124\u0125\7>\2\2\u0125")
        buf.write("\u0126\7?\2\2\u0126J\3\2\2\2\u0127\u0128\7\60\2\2\u0128")
        buf.write("\u0129\7\60\2\2\u0129\u012a\7\60\2\2\u012aL\3\2\2\2\u012b")
        buf.write("\u012c\7?\2\2\u012c\u012d\7?\2\2\u012dN\3\2\2\2\u012e")
        buf.write("\u012f\7-\2\2\u012fP\3\2\2\2\u0130\u0131\7/\2\2\u0131")
        buf.write("R\3\2\2\2\u0132\u0133\7,\2\2\u0133T\3\2\2\2\u0134\u0135")
        buf.write("\7\61\2\2\u0135V\3\2\2\2\u0136\u0137\7\'\2\2\u0137X\3")
        buf.write("\2\2\2\u0138\u0139\7@\2\2\u0139Z\3\2\2\2\u013a\u013b\7")
        buf.write(">\2\2\u013b\\\3\2\2\2\u013c\u013d\7?\2\2\u013d^\3\2\2")
        buf.write("\2\u013e\u0143\5e\63\2\u013f\u0142\5e\63\2\u0140\u0142")
        buf.write("\5g\64\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144`\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\7%\2\2")
        buf.write("\u0147\u0148\7%\2\2\u0148\u014c\3\2\2\2\u0149\u014b\n")
        buf.write("\2\2\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014f\u0150\b\61\3\2\u0150b\3\2\2\2\u0151")
        buf.write("\u0153\t\3\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0157\b\62\3\2\u0157d\3\2\2\2\u0158\u0159")
        buf.write("\t\4\2\2\u0159f\3\2\2\2\u015a\u015b\t\5\2\2\u015bh\3\2")
        buf.write("\2\2\u015c\u015e\5g\64\2\u015d\u015c\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("j\3\2\2\2\u0161\u0165\7\60\2\2\u0162\u0164\5g\64\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166l\3\2\2\2\u0167\u0165\3\2\2")
        buf.write("\2\u0168\u016a\t\6\2\2\u0169\u016b\t\7\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3\2\2\2\u016c")
        buf.write("\u016e\5g\64\2\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170n\3\2\2")
        buf.write("\2\u0171\u0172\7$\2\2\u0172p\3\2\2\2\u0173\u0174\7)\2")
        buf.write("\2\u0174\u0175\t\b\2\2\u0175r\3\2\2\2\u0176\u0177\n\t")
        buf.write("\2\2\u0177t\3\2\2\2\u0178\u0179\7^\2\2\u0179\u017a\t\n")
        buf.write("\2\2\u017av\3\2\2\2\u017b\u017c\7^\2\2\u017c\u017d\n\13")
        buf.write("\2\2\u017dx\3\2\2\2\u017e\u0184\5o8\2\u017f\u0183\5q9")
        buf.write("\2\u0180\u0183\5u;\2\u0181\u0183\5s:\2\u0182\u017f\3\2")
        buf.write("\2\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0186")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\b=\4\2")
        buf.write("\u0188z\3\2\2\2\u0189\u018f\5o8\2\u018a\u018e\5q9\2\u018b")
        buf.write("\u018e\5w<\2\u018c\u018e\5s:\2\u018d\u018a\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3")
        buf.write("\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\b>\5\2\u0193|\3")
        buf.write("\2\2\2\u0194\u0195\13\2\2\2\u0195\u0196\b?\6\2\u0196~")
        buf.write("\3\2\2\2\24\2\u0086\u0089\u008d\u0093\u0095\u0141\u0143")
        buf.write("\u014c\u0154\u015f\u0165\u016a\u016f\u0182\u0184\u018d")
        buf.write("\u018f\7\3\5\2\b\2\2\3=\3\3>\4\3?\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NUMBER_L = 2
    BOOL_L = 3
    STRING_L = 4
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
    AND = 25
    OR = 26
    LPAREN = 27
    RPAREN = 28
    LBRACKET = 29
    RBRACKET = 30
    COMMA = 31
    NEWLINE = 32
    ASSIGN = 33
    NEQ = 34
    GTEQ = 35
    LTEQ = 36
    CONCAT = 37
    STRING_EQ = 38
    PLUS = 39
    MINUS = 40
    MUL = 41
    DIV = 42
    MOD = 43
    GT = 44
    LT = 45
    NUMBER_EQ = 46
    IDENTIFIER = 47
    COMMENT = 48
    WHITESPACE = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'and'", "'or'", "'('", "')'", 
            "'['", "']'", "','", "'\n'", "'<-'", "'!='", "'>='", "'<='", 
            "'...'", "'=='", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_L", "BOOL_L", "STRING_L", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
            "COMMA", "NEWLINE", "ASSIGN", "NEQ", "GTEQ", "LTEQ", "CONCAT", 
            "STRING_EQ", "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", 
            "NUMBER_EQ", "IDENTIFIER", "COMMENT", "WHITESPACE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "NUMBER_L", "BOOL_L", "STRING_L", "TRUE", "FALSE", 
                  "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "LPAREN", 
                  "RPAREN", "LBRACKET", "RBRACKET", "COMMA", "NEWLINE", 
                  "ASSIGN", "NEQ", "GTEQ", "LTEQ", "CONCAT", "STRING_EQ", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", "NUMBER_EQ", 
                  "IDENTIFIER", "COMMENT", "WHITESPACE", "NONDIGIT", "DIGIT", 
                  "INT", "DEC", "EXP", "QUOTE", "QUOTE_IN_STR", "ILLEGAL_NL_STR", 
                  "ESCAPE_SEQ", "ILLEGAL_ESCAPE_SEQ", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[3] = self.STRING_L_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_L_action(self, localctx:RuleContext , actionIndex:int):
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
     


