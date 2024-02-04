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
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\5\2\u0082\n\2\3")
        buf.write("\2\5\2\u0085\n\2\3\3\3\3\5\3\u0089\n\3\3\4\3\4\7\4\u008d")
        buf.write("\n\4\f\4\16\4\u0090\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\7/\u013b\n/\f/\16/")
        buf.write("\u013e\13/\3\60\3\60\3\60\3\60\7\60\u0144\n\60\f\60\16")
        buf.write("\60\u0147\13\60\3\60\3\60\3\61\6\61\u014c\n\61\r\61\16")
        buf.write("\61\u014d\3\61\3\61\3\62\3\62\3\63\3\63\3\64\6\64\u0157")
        buf.write("\n\64\r\64\16\64\u0158\3\65\3\65\7\65\u015d\n\65\f\65")
        buf.write("\16\65\u0160\13\65\3\66\3\66\5\66\u0164\n\66\3\66\6\66")
        buf.write("\u0167\n\66\r\66\16\66\u0168\3\67\3\67\38\38\38\38\38")
        buf.write("\58\u0172\n8\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\5<\u017f")
        buf.write("\n<\3=\3=\7=\u0183\n=\f=\16=\u0186\13=\3=\3=\3=\3>\3>")
        buf.write("\7>\u018d\n>\f>\16>\u0190\13>\3>\3>\3?\3?\3?\2\2@\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w")
        buf.write("\2y\63{\64}\65\3\2\f\4\2\f\f\17\17\5\2\n\13\16\17\"\"")
        buf.write("\5\2C\\aac|\3\2\62;\4\2GGgg\4\2--//\3\2$$\3\2))\6\2\f")
        buf.write("\f\16\17$$^^\t\2))^^ddhhppttvv\2\u019b\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2")
        buf.write("\2\2\5\u0088\3\2\2\2\7\u008a\3\2\2\2\t\u0094\3\2\2\2\13")
        buf.write("\u0099\3\2\2\2\r\u009f\3\2\2\2\17\u00a6\3\2\2\2\21\u00ab")
        buf.write("\3\2\2\2\23\u00b2\3\2\2\2\25\u00b9\3\2\2\2\27\u00bd\3")
        buf.write("\2\2\2\31\u00c5\3\2\2\2\33\u00ca\3\2\2\2\35\u00ce\3\2")
        buf.write("\2\2\37\u00d4\3\2\2\2!\u00d7\3\2\2\2#\u00dd\3\2\2\2%\u00e6")
        buf.write("\3\2\2\2\'\u00e9\3\2\2\2)\u00ee\3\2\2\2+\u00f3\3\2\2\2")
        buf.write("-\u00f9\3\2\2\2/\u00fd\3\2\2\2\61\u0101\3\2\2\2\63\u0105")
        buf.write("\3\2\2\2\65\u0108\3\2\2\2\67\u010a\3\2\2\29\u010c\3\2")
        buf.write("\2\2;\u010e\3\2\2\2=\u0110\3\2\2\2?\u0112\3\2\2\2A\u0114")
        buf.write("\3\2\2\2C\u0117\3\2\2\2E\u011a\3\2\2\2G\u011d\3\2\2\2")
        buf.write("I\u0120\3\2\2\2K\u0124\3\2\2\2M\u0127\3\2\2\2O\u0129\3")
        buf.write("\2\2\2Q\u012b\3\2\2\2S\u012d\3\2\2\2U\u012f\3\2\2\2W\u0131")
        buf.write("\3\2\2\2Y\u0133\3\2\2\2[\u0135\3\2\2\2]\u0137\3\2\2\2")
        buf.write("_\u013f\3\2\2\2a\u014b\3\2\2\2c\u0151\3\2\2\2e\u0153\3")
        buf.write("\2\2\2g\u0156\3\2\2\2i\u015a\3\2\2\2k\u0161\3\2\2\2m\u016a")
        buf.write("\3\2\2\2o\u0171\3\2\2\2q\u0173\3\2\2\2s\u0175\3\2\2\2")
        buf.write("u\u0178\3\2\2\2w\u017e\3\2\2\2y\u0180\3\2\2\2{\u018a\3")
        buf.write("\2\2\2}\u0193\3\2\2\2\177\u0081\5g\64\2\u0080\u0082\5")
        buf.write("i\65\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\u0085\5k\66\2\u0084\u0083\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\4\3\2\2\2\u0086\u0089\5\t\5\2\u0087")
        buf.write("\u0089\5\13\6\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2")
        buf.write("\2\u0089\6\3\2\2\2\u008a\u008e\5m\67\2\u008b\u008d\5w")
        buf.write("<\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0092\5m\67\2\u0092\u0093\b\4\2\2")
        buf.write("\u0093\b\3\2\2\2\u0094\u0095\7v\2\2\u0095\u0096\7t\2\2")
        buf.write("\u0096\u0097\7w\2\2\u0097\u0098\7g\2\2\u0098\n\3\2\2\2")
        buf.write("\u0099\u009a\7h\2\2\u009a\u009b\7c\2\2\u009b\u009c\7n")
        buf.write("\2\2\u009c\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\f\3\2")
        buf.write("\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7o\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\16\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7n\2\2\u00aa\20")
        buf.write("\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7i\2\2\u00b1\22\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7p\2\2\u00b8\24\3\2\2\2\u00b9\u00ba")
        buf.write("\7x\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7t\2\2\u00bc\26")
        buf.write("\3\2\2\2\u00bd\u00be\7f\2\2\u00be\u00bf\7{\2\2\u00bf\u00c0")
        buf.write("\7p\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7e\2\2\u00c4\30\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\32\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\34\3\2\2\2\u00ce\u00cf")
        buf.write("\7w\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7n\2\2\u00d3\36\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7{\2\2\u00d6 \3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7m\2\2\u00dc\"\3\2\2\2\u00dd\u00de")
        buf.write("\7e\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7w\2\2\u00e4\u00e5\7g\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7h\2\2\u00e8&\3\2\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7h\2\2\u00f2*\3")
        buf.write("\2\2\2\u00f3\u00f4\7d\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7i\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8,\3")
        buf.write("\2\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7f\2\2\u00fc.\3\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7v\2\2\u0100\60\3\2\2\2\u0101\u0102")
        buf.write("\7c\2\2\u0102\u0103\7p\2\2\u0103\u0104\7f\2\2\u0104\62")
        buf.write("\3\2\2\2\u0105\u0106\7q\2\2\u0106\u0107\7t\2\2\u0107\64")
        buf.write("\3\2\2\2\u0108\u0109\7*\2\2\u0109\66\3\2\2\2\u010a\u010b")
        buf.write("\7+\2\2\u010b8\3\2\2\2\u010c\u010d\7]\2\2\u010d:\3\2\2")
        buf.write("\2\u010e\u010f\7_\2\2\u010f<\3\2\2\2\u0110\u0111\7.\2")
        buf.write("\2\u0111>\3\2\2\2\u0112\u0113\7\f\2\2\u0113@\3\2\2\2\u0114")
        buf.write("\u0115\7>\2\2\u0115\u0116\7/\2\2\u0116B\3\2\2\2\u0117")
        buf.write("\u0118\7#\2\2\u0118\u0119\7?\2\2\u0119D\3\2\2\2\u011a")
        buf.write("\u011b\7@\2\2\u011b\u011c\7?\2\2\u011cF\3\2\2\2\u011d")
        buf.write("\u011e\7>\2\2\u011e\u011f\7?\2\2\u011fH\3\2\2\2\u0120")
        buf.write("\u0121\7\60\2\2\u0121\u0122\7\60\2\2\u0122\u0123\7\60")
        buf.write("\2\2\u0123J\3\2\2\2\u0124\u0125\7?\2\2\u0125\u0126\7?")
        buf.write("\2\2\u0126L\3\2\2\2\u0127\u0128\7-\2\2\u0128N\3\2\2\2")
        buf.write("\u0129\u012a\7/\2\2\u012aP\3\2\2\2\u012b\u012c\7,\2\2")
        buf.write("\u012cR\3\2\2\2\u012d\u012e\7\61\2\2\u012eT\3\2\2\2\u012f")
        buf.write("\u0130\7\'\2\2\u0130V\3\2\2\2\u0131\u0132\7@\2\2\u0132")
        buf.write("X\3\2\2\2\u0133\u0134\7>\2\2\u0134Z\3\2\2\2\u0135\u0136")
        buf.write("\7?\2\2\u0136\\\3\2\2\2\u0137\u013c\5c\62\2\u0138\u013b")
        buf.write("\5c\62\2\u0139\u013b\5e\63\2\u013a\u0138\3\2\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d^\3\2\2\2\u013e\u013c\3\2\2")
        buf.write("\2\u013f\u0140\7%\2\2\u0140\u0141\7%\2\2\u0141\u0145\3")
        buf.write("\2\2\2\u0142\u0144\n\2\2\2\u0143\u0142\3\2\2\2\u0144\u0147")
        buf.write("\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\b\60\3")
        buf.write("\2\u0149`\3\2\2\2\u014a\u014c\t\3\2\2\u014b\u014a\3\2")
        buf.write("\2\2\u014c\u014d\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\b\61\3\2\u0150")
        buf.write("b\3\2\2\2\u0151\u0152\t\4\2\2\u0152d\3\2\2\2\u0153\u0154")
        buf.write("\t\5\2\2\u0154f\3\2\2\2\u0155\u0157\5e\63\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159h\3\2\2\2\u015a\u015e\7\60\2\2\u015b")
        buf.write("\u015d\5e\63\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015fj\3\2\2")
        buf.write("\2\u0160\u015e\3\2\2\2\u0161\u0163\t\6\2\2\u0162\u0164")
        buf.write("\t\7\2\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0166\3\2\2\2\u0165\u0167\5e\63\2\u0166\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169l\3\2\2\2\u016a\u016b\7$\2\2\u016bn\3\2\2")
        buf.write("\2\u016c\u016d\7)\2\2\u016d\u0172\t\b\2\2\u016e\u016f")
        buf.write("\7^\2\2\u016f\u0170\t\t\2\2\u0170\u0172\t\b\2\2\u0171")
        buf.write("\u016c\3\2\2\2\u0171\u016e\3\2\2\2\u0172p\3\2\2\2\u0173")
        buf.write("\u0174\n\n\2\2\u0174r\3\2\2\2\u0175\u0176\7^\2\2\u0176")
        buf.write("\u0177\t\13\2\2\u0177t\3\2\2\2\u0178\u0179\7^\2\2\u0179")
        buf.write("\u017a\n\13\2\2\u017av\3\2\2\2\u017b\u017f\5o8\2\u017c")
        buf.write("\u017f\5s:\2\u017d\u017f\5q9\2\u017e\u017b\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017fx\3\2\2\2\u0180")
        buf.write("\u0184\5m\67\2\u0181\u0183\5w<\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\5")
        buf.write("u;\2\u0188\u0189\b=\4\2\u0189z\3\2\2\2\u018a\u018e\5m")
        buf.write("\67\2\u018b\u018d\5w<\2\u018c\u018b\3\2\2\2\u018d\u0190")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\b>\5\2")
        buf.write("\u0192|\3\2\2\2\u0193\u0194\13\2\2\2\u0194\u0195\b?\6")
        buf.write("\2\u0195~\3\2\2\2\23\2\u0081\u0084\u0088\u008e\u013a\u013c")
        buf.write("\u0145\u014d\u0158\u015e\u0163\u0168\u0171\u017e\u0184")
        buf.write("\u018e\7\3\4\2\b\2\2\3=\3\3>\4\3?\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER_L = 1
    BOOL_L = 2
    STRING_L = 3
    TRUE = 4
    FALSE = 5
    NUMBER = 6
    BOOL = 7
    STRING = 8
    RETURN = 9
    VAR = 10
    DYNAMIC = 11
    FUNC = 12
    FOR = 13
    UNTIL = 14
    BY = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    BEGIN = 21
    END = 22
    NOT = 23
    AND = 24
    OR = 25
    LPAREN = 26
    RPAREN = 27
    LBRACKET = 28
    RBRACKET = 29
    COMMA = 30
    NEWLINE = 31
    ASSIGN = 32
    NEQ = 33
    GTEQ = 34
    LTEQ = 35
    CONCAT = 36
    STRING_EQ = 37
    PLUS = 38
    MINUS = 39
    MUL = 40
    DIV = 41
    MOD = 42
    GT = 43
    LT = 44
    NUMBER_EQ = 45
    IDENTIFIER = 46
    COMMENT = 47
    WHITESPACE = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'('", "')'", "'['", "']'", 
            "','", "'\n'", "'<-'", "'!='", "'>='", "'<='", "'...'", "'=='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_L", "BOOL_L", "STRING_L", "TRUE", "FALSE", "NUMBER", 
            "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
            "COMMA", "NEWLINE", "ASSIGN", "NEQ", "GTEQ", "LTEQ", "CONCAT", 
            "STRING_EQ", "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", 
            "NUMBER_EQ", "IDENTIFIER", "COMMENT", "WHITESPACE", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "NUMBER_L", "BOOL_L", "STRING_L", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                  "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "LPAREN", 
                  "RPAREN", "LBRACKET", "RBRACKET", "COMMA", "NEWLINE", 
                  "ASSIGN", "NEQ", "GTEQ", "LTEQ", "CONCAT", "STRING_EQ", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "GT", "LT", "NUMBER_EQ", 
                  "IDENTIFIER", "COMMENT", "WHITESPACE", "NONDIGIT", "DIGIT", 
                  "INT", "DEC", "EXP", "QUOTE", "QUOTE_IN_STR", "CHARACTER", 
                  "ESCAPE_SEQ", "ILLEGAL_ESCAPE_SEQ", "STRING_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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
            actions[2] = self.STRING_L_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
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
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		self.text = self.text[1:]
            		raise IllegalEscape(self.text)
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		self.text = self.text[1:]
            		raise UncloseString(self.text)
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


