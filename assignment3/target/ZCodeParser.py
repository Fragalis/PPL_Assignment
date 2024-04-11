# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01ee\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0087\n\3\3\4\3\4\3\4\5\4\u008c\n\4\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u0098\n\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u009f\n\t\3\n\3\n\5\n\u00a3\n\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u00ac\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00b3\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00bb\n\16\f\16\16\16\u00be\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00c6\n\17\f\17\16\17\u00c9\13\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\7\20\u00d1\n\20\f\20\16\20\u00d4")
        buf.write("\13\20\3\21\3\21\3\21\5\21\u00d9\n\21\3\22\3\22\3\22\5")
        buf.write("\22\u00de\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00ea\n\23\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00f3\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00fd\n\26\3\27\3\27\5\27\u0101\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0115\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0125\n\31\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u012b\n\32\3\33\3\33\5\33\u012f\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\5\35\u013a\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u0141\n\36\3\37\3\37\5\37\u0145")
        buf.write("\n\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\5#\u015a\n#\3$\3$\3$\5$\u015f\n$\3%\3")
        buf.write("%\3&\3&\5&\u0165\n&\3\'\3\'\3\'\3\'\3\'\5\'\u016c\n\'")
        buf.write("\3(\3(\5(\u0170\n(\3)\3)\5)\u0174\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u017c\n*\3+\3+\5+\u0180\n+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u018c\n,\3-\3-\5-\u0190\n-\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u01a4\n\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u01b0\n\63\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\38\38\38\58\u01cb\n8\39\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3;\3;\5;\u01d7\n;\3<\3<\3<\3<\3<\5<\u01de")
        buf.write("\n<\3=\3=\3=\3=\3=\3=\5=\u01e6\n=\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\2\5\32\34\36?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz\2\b\3\2\b\n\3\2\3\5\5\2#%\'\'-/\3\2\32\33\3\2()\3")
        buf.write("\2*,\2\u01e1\2|\3\2\2\2\4\u0086\3\2\2\2\6\u008b\3\2\2")
        buf.write("\2\b\u008d\3\2\2\2\n\u008f\3\2\2\2\f\u0091\3\2\2\2\16")
        buf.write("\u0097\3\2\2\2\20\u009e\3\2\2\2\22\u00a2\3\2\2\2\24\u00a4")
        buf.write("\3\2\2\2\26\u00ab\3\2\2\2\30\u00b2\3\2\2\2\32\u00b4\3")
        buf.write("\2\2\2\34\u00bf\3\2\2\2\36\u00ca\3\2\2\2 \u00d8\3\2\2")
        buf.write("\2\"\u00dd\3\2\2\2$\u00e9\3\2\2\2&\u00eb\3\2\2\2(\u00f2")
        buf.write("\3\2\2\2*\u00fc\3\2\2\2,\u0100\3\2\2\2.\u0114\3\2\2\2")
        buf.write("\60\u0124\3\2\2\2\62\u012a\3\2\2\2\64\u012e\3\2\2\2\66")
        buf.write("\u0130\3\2\2\28\u0139\3\2\2\2:\u0140\3\2\2\2<\u0144\3")
        buf.write("\2\2\2>\u0146\3\2\2\2@\u0149\3\2\2\2B\u014f\3\2\2\2D\u0159")
        buf.write("\3\2\2\2F\u015e\3\2\2\2H\u0160\3\2\2\2J\u0164\3\2\2\2")
        buf.write("L\u016b\3\2\2\2N\u016f\3\2\2\2P\u0173\3\2\2\2R\u017b\3")
        buf.write("\2\2\2T\u017f\3\2\2\2V\u018b\3\2\2\2X\u018f\3\2\2\2Z\u0191")
        buf.write("\3\2\2\2\\\u0196\3\2\2\2^\u019a\3\2\2\2`\u01a3\3\2\2\2")
        buf.write("b\u01a5\3\2\2\2d\u01af\3\2\2\2f\u01b1\3\2\2\2h\u01b5\3")
        buf.write("\2\2\2j\u01be\3\2\2\2l\u01c1\3\2\2\2n\u01ca\3\2\2\2p\u01cc")
        buf.write("\3\2\2\2r\u01cf\3\2\2\2t\u01d6\3\2\2\2v\u01dd\3\2\2\2")
        buf.write("x\u01e5\3\2\2\2z\u01e7\3\2\2\2|}\5D#\2}~\5\4\3\2~\177")
        buf.write("\5D#\2\177\u0080\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\5")
        buf.write("\6\4\2\u0082\u0083\5D#\2\u0083\u0084\5\4\3\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0087\3\2\2\2\u0086\u0081\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\5\3\2\2\2\u0088\u008c\5,\27\2\u0089")
        buf.write("\u008c\5\64\33\2\u008a\u008c\5B\"\2\u008b\u0088\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\7\3\2")
        buf.write("\2\2\u008d\u008e\t\2\2\2\u008e\t\3\2\2\2\u008f\u0090\t")
        buf.write("\3\2\2\u0090\13\3\2\2\2\u0091\u0092\7\36\2\2\u0092\u0093")
        buf.write("\5\16\b\2\u0093\u0094\7\37\2\2\u0094\r\3\2\2\2\u0095\u0098")
        buf.write("\5\20\t\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\17\3\2\2\2\u0099\u009a\5\22\n\2\u009a")
        buf.write("\u009b\7 \2\2\u009b\u009c\5\20\t\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009f\5\22\n\2\u009e\u0099\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\21\3\2\2\2\u00a0\u00a3\5\26\f\2\u00a1\u00a3")
        buf.write("\5\f\7\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\23\3\2\2\2\u00a4\u00a5\7\60\2\2\u00a5\25\3\2\2\2\u00a6")
        buf.write("\u00a7\5\30\r\2\u00a7\u00a8\7&\2\2\u00a8\u00a9\5\30\r")
        buf.write("\2\u00a9\u00ac\3\2\2\2\u00aa\u00ac\5\30\r\2\u00ab\u00a6")
        buf.write("\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\27\3\2\2\2\u00ad\u00ae")
        buf.write("\5\32\16\2\u00ae\u00af\t\4\2\2\u00af\u00b0\5\32\16\2\u00b0")
        buf.write("\u00b3\3\2\2\2\u00b1\u00b3\5\32\16\2\u00b2\u00ad\3\2\2")
        buf.write("\2\u00b2\u00b1\3\2\2\2\u00b3\31\3\2\2\2\u00b4\u00b5\b")
        buf.write("\16\1\2\u00b5\u00b6\5\34\17\2\u00b6\u00bc\3\2\2\2\u00b7")
        buf.write("\u00b8\f\4\2\2\u00b8\u00b9\t\5\2\2\u00b9\u00bb\5\34\17")
        buf.write("\2\u00ba\u00b7\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\33\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00bf\u00c0\b\17\1\2\u00c0\u00c1\5\36\20\2\u00c1")
        buf.write("\u00c7\3\2\2\2\u00c2\u00c3\f\4\2\2\u00c3\u00c4\t\6\2\2")
        buf.write("\u00c4\u00c6\5\36\20\2\u00c5\u00c2\3\2\2\2\u00c6\u00c9")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\35\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\b\20\1\2\u00cb")
        buf.write("\u00cc\5 \21\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce\f\4\2\2")
        buf.write("\u00ce\u00cf\t\7\2\2\u00cf\u00d1\5 \21\2\u00d0\u00cd\3")
        buf.write("\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\37\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6")
        buf.write("\7\31\2\2\u00d6\u00d9\5 \21\2\u00d7\u00d9\5\"\22\2\u00d8")
        buf.write("\u00d5\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9!\3\2\2\2\u00da")
        buf.write("\u00db\7)\2\2\u00db\u00de\5\"\22\2\u00dc\u00de\5*\26\2")
        buf.write("\u00dd\u00da\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de#\3\2\2")
        buf.write("\2\u00df\u00e0\5\24\13\2\u00e0\u00e1\7\36\2\2\u00e1\u00e2")
        buf.write("\5(\25\2\u00e2\u00e3\7\37\2\2\u00e3\u00ea\3\2\2\2\u00e4")
        buf.write("\u00e5\5&\24\2\u00e5\u00e6\7\36\2\2\u00e6\u00e7\5(\25")
        buf.write("\2\u00e7\u00e8\7\37\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00df")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00ea%\3\2\2\2\u00eb\u00ec")
        buf.write("\5r:\2\u00ec\'\3\2\2\2\u00ed\u00ee\5\26\f\2\u00ee\u00ef")
        buf.write("\7 \2\2\u00ef\u00f0\5(\25\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00f3\5\26\f\2\u00f2\u00ed\3\2\2\2\u00f2\u00f1\3\2\2")
        buf.write("\2\u00f3)\3\2\2\2\u00f4\u00fd\5\n\6\2\u00f5\u00fd\5\24")
        buf.write("\13\2\u00f6\u00fd\5$\23\2\u00f7\u00fd\5&\24\2\u00f8\u00f9")
        buf.write("\7\34\2\2\u00f9\u00fa\5\26\f\2\u00fa\u00fb\7\35\2\2\u00fb")
        buf.write("\u00fd\3\2\2\2\u00fc\u00f4\3\2\2\2\u00fc\u00f5\3\2\2\2")
        buf.write("\u00fc\u00f6\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc\u00f8\3")
        buf.write("\2\2\2\u00fd+\3\2\2\2\u00fe\u0101\5.\30\2\u00ff\u0101")
        buf.write("\5\60\31\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("-\3\2\2\2\u0102\u0103\5\b\5\2\u0103\u0104\5\24\13\2\u0104")
        buf.write("\u0115\3\2\2\2\u0105\u0106\5\b\5\2\u0106\u0107\5\24\13")
        buf.write("\2\u0107\u0108\7\"\2\2\u0108\u0109\5\26\f\2\u0109\u0115")
        buf.write("\3\2\2\2\u010a\u010b\7\f\2\2\u010b\u010c\5\24\13\2\u010c")
        buf.write("\u010d\7\"\2\2\u010d\u010e\5\26\f\2\u010e\u0115\3\2\2")
        buf.write("\2\u010f\u0110\7\r\2\2\u0110\u0111\5\24\13\2\u0111\u0112")
        buf.write("\7\"\2\2\u0112\u0113\5\26\f\2\u0113\u0115\3\2\2\2\u0114")
        buf.write("\u0102\3\2\2\2\u0114\u0105\3\2\2\2\u0114\u010a\3\2\2\2")
        buf.write("\u0114\u010f\3\2\2\2\u0115/\3\2\2\2\u0116\u0117\5\b\5")
        buf.write("\2\u0117\u0118\5\24\13\2\u0118\u0119\7\36\2\2\u0119\u011a")
        buf.write("\5\62\32\2\u011a\u011b\7\37\2\2\u011b\u0125\3\2\2\2\u011c")
        buf.write("\u011d\5\b\5\2\u011d\u011e\5\24\13\2\u011e\u011f\7\36")
        buf.write("\2\2\u011f\u0120\5\62\32\2\u0120\u0121\7\37\2\2\u0121")
        buf.write("\u0122\7\"\2\2\u0122\u0123\5\f\7\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u0116\3\2\2\2\u0124\u011c\3\2\2\2\u0125\61\3\2")
        buf.write("\2\2\u0126\u0127\7\3\2\2\u0127\u0128\7 \2\2\u0128\u012b")
        buf.write("\5\62\32\2\u0129\u012b\7\3\2\2\u012a\u0126\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\63\3\2\2\2\u012c\u012f\5\66\34\2")
        buf.write("\u012d\u012f\5B\"\2\u012e\u012c\3\2\2\2\u012e\u012d\3")
        buf.write("\2\2\2\u012f\65\3\2\2\2\u0130\u0131\7\16\2\2\u0131\u0132")
        buf.write("\5\24\13\2\u0132\u0133\7\34\2\2\u0133\u0134\58\35\2\u0134")
        buf.write("\u0135\7\35\2\2\u0135\u0136\5H%\2\u0136\67\3\2\2\2\u0137")
        buf.write("\u013a\5:\36\2\u0138\u013a\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u013a9\3\2\2\2\u013b\u013c\5<\37")
        buf.write("\2\u013c\u013d\7 \2\2\u013d\u013e\5:\36\2\u013e\u0141")
        buf.write("\3\2\2\2\u013f\u0141\5<\37\2\u0140\u013b\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141;\3\2\2\2\u0142\u0145\5> \2\u0143")
        buf.write("\u0145\5@!\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145")
        buf.write("=\3\2\2\2\u0146\u0147\5\b\5\2\u0147\u0148\5\24\13\2\u0148")
        buf.write("?\3\2\2\2\u0149\u014a\5\b\5\2\u014a\u014b\5\24\13\2\u014b")
        buf.write("\u014c\7\36\2\2\u014c\u014d\5\62\32\2\u014d\u014e\7\37")
        buf.write("\2\2\u014eA\3\2\2\2\u014f\u0150\7\16\2\2\u0150\u0151\5")
        buf.write("\24\13\2\u0151\u0152\7\34\2\2\u0152\u0153\58\35\2\u0153")
        buf.write("\u0154\7\35\2\2\u0154\u0155\5D#\2\u0155\u0156\5J&\2\u0156")
        buf.write("C\3\2\2\2\u0157\u015a\5F$\2\u0158\u015a\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015aE\3\2\2\2\u015b")
        buf.write("\u015c\7!\2\2\u015c\u015f\5F$\2\u015d\u015f\7!\2\2\u015e")
        buf.write("\u015b\3\2\2\2\u015e\u015d\3\2\2\2\u015fG\3\2\2\2\u0160")
        buf.write("\u0161\7!\2\2\u0161I\3\2\2\2\u0162\u0165\5n8\2\u0163\u0165")
        buf.write("\5z>\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165K")
        buf.write("\3\2\2\2\u0166\u0167\5N(\2\u0167\u0168\5D#\2\u0168\u0169")
        buf.write("\5L\'\2\u0169\u016c\3\2\2\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0166\3\2\2\2\u016b\u016a\3\2\2\2\u016cM\3\2\2\2\u016d")
        buf.write("\u0170\5\\/\2\u016e\u0170\5P)\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170O\3\2\2\2\u0171\u0174\5R*\2\u0172")
        buf.write("\u0174\5T+\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("Q\3\2\2\2\u0175\u017c\5,\27\2\u0176\u017c\5V,\2\u0177")
        buf.write("\u017c\5j\66\2\u0178\u017c\5l\67\2\u0179\u017c\5n8\2\u017a")
        buf.write("\u017c\5p9\2\u017b\u0175\3\2\2\2\u017b\u0176\3\2\2\2\u017b")
        buf.write("\u0177\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017cS\3\2\2\2\u017d\u0180\5h\65")
        buf.write("\2\u017e\u0180\5z>\2\u017f\u017d\3\2\2\2\u017f\u017e\3")
        buf.write("\2\2\2\u0180U\3\2\2\2\u0181\u0182\5X-\2\u0182\u0183\7")
        buf.write("\"\2\2\u0183\u0184\5\26\f\2\u0184\u0185\5H%\2\u0185\u018c")
        buf.write("\3\2\2\2\u0186\u0187\5X-\2\u0187\u0188\7\"\2\2\u0188\u0189")
        buf.write("\5\f\7\2\u0189\u018a\5H%\2\u018a\u018c\3\2\2\2\u018b\u0181")
        buf.write("\3\2\2\2\u018b\u0186\3\2\2\2\u018cW\3\2\2\2\u018d\u0190")
        buf.write("\5\24\13\2\u018e\u0190\5Z.\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190Y\3\2\2\2\u0191\u0192\5\24\13\2\u0192")
        buf.write("\u0193\7\36\2\2\u0193\u0194\5(\25\2\u0194\u0195\7\37\2")
        buf.write("\2\u0195[\3\2\2\2\u0196\u0197\5^\60\2\u0197\u0198\5`\61")
        buf.write("\2\u0198\u0199\5d\63\2\u0199]\3\2\2\2\u019a\u019b\7\24")
        buf.write("\2\2\u019b\u019c\5f\64\2\u019c\u019d\5D#\2\u019d\u019e")
        buf.write("\5N(\2\u019e_\3\2\2\2\u019f\u01a0\5b\62\2\u01a0\u01a1")
        buf.write("\5`\61\2\u01a1\u01a4\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u019f\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4a\3\2\2\2\u01a5")
        buf.write("\u01a6\7\26\2\2\u01a6\u01a7\5f\64\2\u01a7\u01a8\5D#\2")
        buf.write("\u01a8\u01a9\5N(\2\u01a9c\3\2\2\2\u01aa\u01ab\7\25\2\2")
        buf.write("\u01ab\u01ac\5D#\2\u01ac\u01ad\5N(\2\u01ad\u01b0\3\2\2")
        buf.write("\2\u01ae\u01b0\3\2\2\2\u01af\u01aa\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0e\3\2\2\2\u01b1\u01b2\7\34\2\2\u01b2\u01b3")
        buf.write("\5\26\f\2\u01b3\u01b4\7\35\2\2\u01b4g\3\2\2\2\u01b5\u01b6")
        buf.write("\7\17\2\2\u01b6\u01b7\5\24\13\2\u01b7\u01b8\7\20\2\2\u01b8")
        buf.write("\u01b9\5\26\f\2\u01b9\u01ba\7\21\2\2\u01ba\u01bb\5\26")
        buf.write("\f\2\u01bb\u01bc\5D#\2\u01bc\u01bd\5N(\2\u01bdi\3\2\2")
        buf.write("\2\u01be\u01bf\7\22\2\2\u01bf\u01c0\5H%\2\u01c0k\3\2\2")
        buf.write("\2\u01c1\u01c2\7\23\2\2\u01c2\u01c3\5H%\2\u01c3m\3\2\2")
        buf.write("\2\u01c4\u01c5\7\13\2\2\u01c5\u01c6\5\26\f\2\u01c6\u01c7")
        buf.write("\5H%\2\u01c7\u01cb\3\2\2\2\u01c8\u01c9\7\13\2\2\u01c9")
        buf.write("\u01cb\5H%\2\u01ca\u01c4\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("o\3\2\2\2\u01cc\u01cd\5r:\2\u01cd\u01ce\5H%\2\u01ceq\3")
        buf.write("\2\2\2\u01cf\u01d0\5\24\13\2\u01d0\u01d1\7\34\2\2\u01d1")
        buf.write("\u01d2\5t;\2\u01d2\u01d3\7\35\2\2\u01d3s\3\2\2\2\u01d4")
        buf.write("\u01d7\5v<\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7u\3\2\2\2\u01d8\u01d9\5x=\2\u01d9")
        buf.write("\u01da\7 \2\2\u01da\u01db\5v<\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01de\5x=\2\u01dd\u01d8\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("w\3\2\2\2\u01df\u01e6\5\26\f\2\u01e0\u01e1\5\24\13\2\u01e1")
        buf.write("\u01e2\7\36\2\2\u01e2\u01e3\5\62\32\2\u01e3\u01e4\7\37")
        buf.write("\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01df\3\2\2\2\u01e5\u01e0")
        buf.write("\3\2\2\2\u01e6y\3\2\2\2\u01e7\u01e8\7\27\2\2\u01e8\u01e9")
        buf.write("\5F$\2\u01e9\u01ea\5L\'\2\u01ea\u01eb\7\30\2\2\u01eb\u01ec")
        buf.write("\5F$\2\u01ec{\3\2\2\2)\u0086\u008b\u0097\u009e\u00a2\u00ab")
        buf.write("\u00b2\u00bc\u00c7\u00d2\u00d8\u00dd\u00e9\u00f2\u00fc")
        buf.write("\u0100\u0114\u0124\u012a\u012e\u0139\u0140\u0144\u0159")
        buf.write("\u015e\u0164\u016b\u016f\u0173\u017b\u017f\u018b\u018f")
        buf.write("\u01a3\u01af\u01ca\u01d6\u01dd\u01e5")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'('", "')'", "'['", "']'", "','", "'\n'", 
                     "'<-'", "'!='", "'>='", "'<='", "'...'", "'=='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "NUMBER_L", "BOOL_L", "STRING_L", "TRUE", 
                      "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                      "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "COMMA", "NEWLINE", "ASSIGN", "NEQ", "GTEQ", 
                      "LTEQ", "CONCAT", "STRING_EQ", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "GT", "LT", "NUMBER_EQ", "IDENTIFIER", 
                      "COMMENT", "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration_list = 1
    RULE_declaration = 2
    RULE_primitive_type = 3
    RULE_primitive_literals = 4
    RULE_array_value = 5
    RULE_array_literal_list = 6
    RULE_array_literal_prime = 7
    RULE_array_literal = 8
    RULE_identifier = 9
    RULE_expression = 10
    RULE_relational_expr = 11
    RULE_logical_expr1 = 12
    RULE_numeric_expr1 = 13
    RULE_numeric_expr2 = 14
    RULE_logical_expr2 = 15
    RULE_numeric_expr3 = 16
    RULE_element_expr = 17
    RULE_function_call_expr = 18
    RULE_index_op_expr = 19
    RULE_term = 20
    RULE_variable_declaration = 21
    RULE_primitive_type_declaration = 22
    RULE_array_type_declaration = 23
    RULE_number_literal_list = 24
    RULE_function_declaration = 25
    RULE_function_prototype_declaration = 26
    RULE_parameter_list = 27
    RULE_parameter_prime = 28
    RULE_parameter = 29
    RULE_primitive_parameter = 30
    RULE_array_parameter = 31
    RULE_function_full_declaration = 32
    RULE_nullable_newline_list = 33
    RULE_newline_list = 34
    RULE_newline = 35
    RULE_function_body = 36
    RULE_statement_list = 37
    RULE_statement = 38
    RULE_non_if_statement = 39
    RULE_simple_statement = 40
    RULE_compound_statement = 41
    RULE_assignment_statement = 42
    RULE_assignee = 43
    RULE_array_cell = 44
    RULE_if_statement = 45
    RULE_if_clause = 46
    RULE_elif_clause_list = 47
    RULE_elif_clause = 48
    RULE_else_clause = 49
    RULE_conditional_expr = 50
    RULE_for_statement = 51
    RULE_break_statement = 52
    RULE_continue_statement = 53
    RULE_return_statement = 54
    RULE_function_call_statement = 55
    RULE_function_call = 56
    RULE_argument_list = 57
    RULE_argument_prime = 58
    RULE_argument = 59
    RULE_block_statement = 60

    ruleNames =  [ "program", "declaration_list", "declaration", "primitive_type", 
                   "primitive_literals", "array_value", "array_literal_list", 
                   "array_literal_prime", "array_literal", "identifier", 
                   "expression", "relational_expr", "logical_expr1", "numeric_expr1", 
                   "numeric_expr2", "logical_expr2", "numeric_expr3", "element_expr", 
                   "function_call_expr", "index_op_expr", "term", "variable_declaration", 
                   "primitive_type_declaration", "array_type_declaration", 
                   "number_literal_list", "function_declaration", "function_prototype_declaration", 
                   "parameter_list", "parameter_prime", "parameter", "primitive_parameter", 
                   "array_parameter", "function_full_declaration", "nullable_newline_list", 
                   "newline_list", "newline", "function_body", "statement_list", 
                   "statement", "non_if_statement", "simple_statement", 
                   "compound_statement", "assignment_statement", "assignee", 
                   "array_cell", "if_statement", "if_clause", "elif_clause_list", 
                   "elif_clause", "else_clause", "conditional_expr", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "function_call_statement", "function_call", "argument_list", 
                   "argument_prime", "argument", "block_statement" ]

    EOF = Token.EOF
    NUMBER_L=1
    BOOL_L=2
    STRING_L=3
    TRUE=4
    FALSE=5
    NUMBER=6
    BOOL=7
    STRING=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    NOT=23
    AND=24
    OR=25
    LPAREN=26
    RPAREN=27
    LBRACKET=28
    RBRACKET=29
    COMMA=30
    NEWLINE=31
    ASSIGN=32
    NEQ=33
    GTEQ=34
    LTEQ=35
    CONCAT=36
    STRING_EQ=37
    PLUS=38
    MINUS=39
    MUL=40
    DIV=41
    MOD=42
    GT=43
    LT=44
    NUMBER_EQ=45
    IDENTIFIER=46
    COMMENT=47
    WHITESPACE=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Nullable_newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,i)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.nullable_newline_list()
            self.state = 123
            self.declaration_list()
            self.state = 124
            self.nullable_newline_list()
            self.state = 125
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.declaration()
                self.state = 128
                self.nullable_newline_list()
                self.state = 129
                self.declaration_list()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def function_full_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_full_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.function_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.function_full_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = ZCodeParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_L(self):
            return self.getToken(ZCodeParser.NUMBER_L, 0)

        def BOOL_L(self):
            return self.getToken(ZCodeParser.BOOL_L, 0)

        def STRING_L(self):
            return self.getToken(ZCodeParser.STRING_L, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literals" ):
                return visitor.visitPrimitive_literals(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literals(self):

        localctx = ZCodeParser.Primitive_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_L) | (1 << ZCodeParser.BOOL_L) | (1 << ZCodeParser.STRING_L))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def array_literal_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literal_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZCodeParser.LBRACKET)
            self.state = 144
            self.array_literal_list()
            self.state = 145
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literal_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_list" ):
                return visitor.visitArray_literal_list(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_list(self):

        localctx = ZCodeParser.Array_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_literal_list)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.array_literal_prime()
                pass
            elif token in [ZCodeParser.RBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_literal_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literal_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_prime" ):
                return visitor.visitArray_literal_prime(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_prime(self):

        localctx = ZCodeParser.Array_literal_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_literal_prime)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.array_literal()
                self.state = 152
                self.match(ZCodeParser.COMMA)
                self.state = 153
                self.array_literal_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_literal)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.expression()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.array_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = ZCodeParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_exprContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.relational_expr()
                self.state = 165
                self.match(ZCodeParser.CONCAT)
                self.state = 166
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_expr1Context,i)


        def NUMBER_EQ(self):
            return self.getToken(ZCodeParser.NUMBER_EQ, 0)

        def STRING_EQ(self):
            return self.getToken(ZCodeParser.STRING_EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTEQ(self):
            return self.getToken(ZCodeParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(ZCodeParser.GTEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = ZCodeParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.logical_expr1(0)
                self.state = 172
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NEQ) | (1 << ZCodeParser.GTEQ) | (1 << ZCodeParser.LTEQ) | (1 << ZCodeParser.STRING_EQ) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.NUMBER_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.logical_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.logical_expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr1Context,0)


        def logical_expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_expr1Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr1" ):
                return visitor.visitLogical_expr1(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_logical_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.numeric_expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr1)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.numeric_expr1(0) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Numeric_expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr2Context,0)


        def numeric_expr1(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr1Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numeric_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_expr1" ):
                return visitor.visitNumeric_expr1(self)
            else:
                return visitor.visitChildren(self)



    def numeric_expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Numeric_expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_numeric_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.numeric_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr1)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.numeric_expr2(0) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Numeric_expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_expr2Context,0)


        def numeric_expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr2Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_numeric_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_expr2" ):
                return visitor.visitNumeric_expr2(self)
            else:
                return visitor.visitChildren(self)



    def numeric_expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Numeric_expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_numeric_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.logical_expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr2)
                    self.state = 203
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 205
                    self.logical_expr2() 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def logical_expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_expr2Context,0)


        def numeric_expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr3Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr2" ):
                return visitor.visitLogical_expr2(self)
            else:
                return visitor.visitChildren(self)




    def logical_expr2(self):

        localctx = ZCodeParser.Logical_expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logical_expr2)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(ZCodeParser.NOT)
                self.state = 212
                self.logical_expr2()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.numeric_expr3()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def numeric_expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Numeric_expr3Context,0)


        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numeric_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_expr3" ):
                return visitor.visitNumeric_expr3(self)
            else:
                return visitor.visitChildren(self)




    def numeric_expr3(self):

        localctx = ZCodeParser.Numeric_expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_numeric_expr3)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(ZCodeParser.MINUS)
                self.state = 217
                self.numeric_expr3()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def index_op_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_op_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def function_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = ZCodeParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_element_expr)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.identifier()
                self.state = 222
                self.match(ZCodeParser.LBRACKET)
                self.state = 223
                self.index_op_expr()
                self.state = 224
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.function_call_expr()
                self.state = 227
                self.match(ZCodeParser.LBRACKET)
                self.state = 228
                self.index_op_expr()
                self.state = 229
                self.match(ZCodeParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_expr" ):
                return visitor.visitFunction_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def function_call_expr(self):

        localctx = ZCodeParser.Function_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_op_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_op_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_op_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_op_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op_expr" ):
                return visitor.visitIndex_op_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_op_expr(self):

        localctx = ZCodeParser.Index_op_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_op_expr)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.expression()
                self.state = 236
                self.match(ZCodeParser.COMMA)
                self.state = 237
                self.index_op_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literals(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_literalsContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


        def function_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_exprContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.primitive_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.element_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.function_call_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.match(ZCodeParser.LPAREN)
                self.state = 247
                self.expression()
                self.state = 248
                self.match(ZCodeParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_type_declarationContext,0)


        def array_type_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_type_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable_declaration)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.primitive_type_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.array_type_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_type_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type_declaration" ):
                return visitor.visitPrimitive_type_declaration(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type_declaration(self):

        localctx = ZCodeParser.Primitive_type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primitive_type_declaration)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.primitive_type()
                self.state = 257
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.primitive_type()
                self.state = 260
                self.identifier()
                self.state = 261
                self.match(ZCodeParser.ASSIGN)
                self.state = 262
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(ZCodeParser.VAR)
                self.state = 265
                self.identifier()
                self.state = 266
                self.match(ZCodeParser.ASSIGN)
                self.state = 267
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.match(ZCodeParser.DYNAMIC)
                self.state = 270
                self.identifier()
                self.state = 271
                self.match(ZCodeParser.ASSIGN)
                self.state = 272
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def number_literal_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literal_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_declaration" ):
                return visitor.visitArray_type_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_type_declaration(self):

        localctx = ZCodeParser.Array_type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_type_declaration)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.primitive_type()
                self.state = 277
                self.identifier()
                self.state = 278
                self.match(ZCodeParser.LBRACKET)
                self.state = 279
                self.number_literal_list()
                self.state = 280
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.primitive_type()
                self.state = 283
                self.identifier()
                self.state = 284
                self.match(ZCodeParser.LBRACKET)
                self.state = 285
                self.number_literal_list()
                self.state = 286
                self.match(ZCodeParser.RBRACKET)
                self.state = 287
                self.match(ZCodeParser.ASSIGN)
                self.state = 288
                self.array_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literal_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_L(self):
            return self.getToken(ZCodeParser.NUMBER_L, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def number_literal_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literal_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_literal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal_list" ):
                return visitor.visitNumber_literal_list(self)
            else:
                return visitor.visitChildren(self)




    def number_literal_list(self):

        localctx = ZCodeParser.Number_literal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number_literal_list)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ZCodeParser.NUMBER_L)
                self.state = 293
                self.match(ZCodeParser.COMMA)
                self.state = 294
                self.number_literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.NUMBER_L)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_prototype_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_prototype_declarationContext,0)


        def function_full_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_full_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_function_declaration)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.function_prototype_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.function_full_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_prototype_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_prototype_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_prototype_declaration" ):
                return visitor.visitFunction_prototype_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_prototype_declaration(self):

        localctx = ZCodeParser.Function_prototype_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_function_prototype_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.FUNC)
            self.state = 303
            self.identifier()
            self.state = 304
            self.match(ZCodeParser.LPAREN)
            self.state = 305
            self.parameter_list()
            self.state = 306
            self.match(ZCodeParser.RPAREN)
            self.state = 307
            self.newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_parameter_list)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.parameter_prime()
                pass
            elif token in [ZCodeParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_prime" ):
                return visitor.visitParameter_prime(self)
            else:
                return visitor.visitChildren(self)




    def parameter_prime(self):

        localctx = ZCodeParser.Parameter_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_parameter_prime)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.parameter()
                self.state = 314
                self.match(ZCodeParser.COMMA)
                self.state = 315
                self.parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_parameterContext,0)


        def array_parameter(self):
            return self.getTypedRuleContext(ZCodeParser.Array_parameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parameter)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.primitive_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.array_parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_parameter" ):
                return visitor.visitPrimitive_parameter(self)
            else:
                return visitor.visitChildren(self)




    def primitive_parameter(self):

        localctx = ZCodeParser.Primitive_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primitive_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.primitive_type()
            self.state = 325
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def number_literal_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literal_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_parameter" ):
                return visitor.visitArray_parameter(self)
            else:
                return visitor.visitChildren(self)




    def array_parameter(self):

        localctx = ZCodeParser.Array_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.primitive_type()
            self.state = 328
            self.identifier()
            self.state = 329
            self.match(ZCodeParser.LBRACKET)
            self.state = 330
            self.number_literal_list()
            self.state = 331
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_full_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_full_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_full_declaration" ):
                return visitor.visitFunction_full_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_full_declaration(self):

        localctx = ZCodeParser.Function_full_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function_full_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.FUNC)
            self.state = 334
            self.identifier()
            self.state = 335
            self.match(ZCodeParser.LPAREN)
            self.state = 336
            self.parameter_list()
            self.state = 337
            self.match(ZCodeParser.RPAREN)
            self.state = 338
            self.nullable_newline_list()
            self.state = 339
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newline_list" ):
                return visitor.visitNullable_newline_list(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newline_list(self):

        localctx = ZCodeParser.Nullable_newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_nullable_newline_list)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_newline_list)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(ZCodeParser.NEWLINE)
                self.state = 346
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = ZCodeParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_function_body)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.return_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_statement_list)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.statement()
                self.state = 357
                self.nullable_newline_list()
                self.state = 358
                self.statement_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def non_if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Non_if_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.if_statement()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.non_if_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_statementContext,0)


        def compound_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_non_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_if_statement" ):
                return visitor.visitNon_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def non_if_statement(self):

        localctx = ZCodeParser.Non_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_non_if_statement)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.simple_statement()
                pass
            elif token in [ZCodeParser.FOR, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.compound_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_simple_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statement" ):
                return visitor.visitSimple_statement(self)
            else:
                return visitor.visitChildren(self)




    def simple_statement(self):

        localctx = ZCodeParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_simple_statement)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 375
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 376
                self.function_call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_compound_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = ZCodeParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_compound_statement)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.for_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignee(self):
            return self.getTypedRuleContext(ZCodeParser.AssigneeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assignment_statement)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.assignee()
                self.state = 384
                self.match(ZCodeParser.ASSIGN)
                self.state = 385
                self.expression()
                self.state = 386
                self.newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.assignee()
                self.state = 389
                self.match(ZCodeParser.ASSIGN)
                self.state = 390
                self.array_value()
                self.state = 391
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigneeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def array_cell(self):
            return self.getTypedRuleContext(ZCodeParser.Array_cellContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignee" ):
                return visitor.visitAssignee(self)
            else:
                return visitor.visitChildren(self)




    def assignee(self):

        localctx = ZCodeParser.AssigneeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assignee)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.array_cell()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_cellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def index_op_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_op_exprContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_cell" ):
                return visitor.visitArray_cell(self)
            else:
                return visitor.visitChildren(self)




    def array_cell(self):

        localctx = ZCodeParser.Array_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.identifier()
            self.state = 400
            self.match(ZCodeParser.LBRACKET)
            self.state = 401
            self.index_op_expr()
            self.state = 402
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_clause(self):
            return self.getTypedRuleContext(ZCodeParser.If_clauseContext,0)


        def elif_clause_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clause_listContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.if_clause()
            self.state = 405
            self.elif_clause_list()
            self.state = 406
            self.else_clause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def conditional_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Conditional_exprContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_clause" ):
                return visitor.visitIf_clause(self)
            else:
                return visitor.visitChildren(self)




    def if_clause(self):

        localctx = ZCodeParser.If_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(ZCodeParser.IF)
            self.state = 409
            self.conditional_expr()
            self.state = 410
            self.nullable_newline_list()
            self.state = 411
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_clause_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clauseContext,0)


        def elif_clause_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clause_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clause_list" ):
                return visitor.visitElif_clause_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_clause_list(self):

        localctx = ZCodeParser.Elif_clause_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_elif_clause_list)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.elif_clause()
                self.state = 414
                self.elif_clause_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def conditional_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Conditional_exprContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clause" ):
                return visitor.visitElif_clause(self)
            else:
                return visitor.visitChildren(self)




    def elif_clause(self):

        localctx = ZCodeParser.Elif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_elif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(ZCodeParser.ELIF)
            self.state = 420
            self.conditional_expr()
            self.state = 421
            self.nullable_newline_list()
            self.state = 422
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = ZCodeParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_else_clause)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(ZCodeParser.ELSE)
                self.state = 425
                self.nullable_newline_list()
                self.state = 426
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_conditional_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expr" ):
                return visitor.visitConditional_expr(self)
            else:
                return visitor.visitChildren(self)




    def conditional_expr(self):

        localctx = ZCodeParser.Conditional_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_conditional_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(ZCodeParser.LPAREN)
            self.state = 432
            self.expression()
            self.state = 433
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(ZCodeParser.FOR)
            self.state = 436
            self.identifier()
            self.state = 437
            self.match(ZCodeParser.UNTIL)
            self.state = 438
            self.expression()
            self.state = 439
            self.match(ZCodeParser.BY)
            self.state = 440
            self.expression()
            self.state = 441
            self.nullable_newline_list()
            self.state = 442
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(ZCodeParser.BREAK)
            self.state = 445
            self.newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(ZCodeParser.CONTINUE)
            self.state = 448
            self.newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_return_statement)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(ZCodeParser.RETURN)
                self.state = 451
                self.expression()
                self.state = 452
                self.newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.match(ZCodeParser.RETURN)
                self.state = 455
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.function_call()
            self.state = 459
            self.newline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def argument_list(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_listContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.identifier()
            self.state = 462
            self.match(ZCodeParser.LPAREN)
            self.state = 463
            self.argument_list()
            self.state = 464
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = ZCodeParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_argument_list)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.argument_prime()
                pass
            elif token in [ZCodeParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argument_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_prime" ):
                return visitor.visitArgument_prime(self)
            else:
                return visitor.visitChildren(self)




    def argument_prime(self):

        localctx = ZCodeParser.Argument_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_argument_prime)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.argument()
                self.state = 471
                self.match(ZCodeParser.COMMA)
                self.state = 472
                self.argument_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ZCodeParser.IdentifierContext,0)


        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def number_literal_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literal_listContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_argument)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.identifier()
                self.state = 479
                self.match(ZCodeParser.LBRACKET)
                self.state = 480
                self.number_literal_list()
                self.state = 481
                self.match(ZCodeParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(ZCodeParser.BEGIN)
            self.state = 486
            self.newline_list()
            self.state = 487
            self.statement_list()
            self.state = 488
            self.match(ZCodeParser.END)
            self.state = 489
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.logical_expr1_sempred
        self._predicates[13] = self.numeric_expr1_sempred
        self._predicates[14] = self.numeric_expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr1_sempred(self, localctx:Logical_expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def numeric_expr1_sempred(self, localctx:Numeric_expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def numeric_expr2_sempred(self, localctx:Numeric_expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




