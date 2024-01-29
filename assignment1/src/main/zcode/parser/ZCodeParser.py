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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\3\2\3\2\3\3\3\3\5\3\u0080\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0087\n\4\3\5\3\5\5\5\u008b\n\5\3")
        buf.write("\6\3\6\5\6\u008f\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u0096\n\7")
        buf.write("\3\b\3\b\5\b\u009a\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00ae\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\5\16\u00b5\n\16\3\17\3\17")
        buf.write("\5\17\u00b9\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00c2\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00c9\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00d1\n\23\f\23\16")
        buf.write("\23\u00d4\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00dc")
        buf.write("\n\24\f\24\16\24\u00df\13\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u00e7\n\25\f\25\16\25\u00ea\13\25\3\26\3\26")
        buf.write("\3\26\5\26\u00ef\n\26\3\27\3\27\3\27\5\27\u00f4\n\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u0100\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u010a\n\32\3\33\3\33\5\33\u010e\n\33\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0114\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u0120\n\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u0129\n\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0133\n\35\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0139\n\36\3\37\3\37\5\37\u013d\n\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\5!\u0147\n!\3\"\3\"\3\"\3\"\3\"\5\"\u014e")
        buf.write("\n\"\3#\3#\5#\u0152\n#\3$\3$\3$\3$\3$\5$\u0159\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0167\n%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3(\5(\u0173\n(\3)\3)\5)\u0177\n)\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\5*\u0180\n*\3+\3+\3+\3+\3+\5+\u0187")
        buf.write("\n+\3,\3,\5,\u018b\n,\3-\3-\3-\3-\5-\u0191\n-\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u0199\n.\3/\3/\3/\5/\u019e\n/\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\5\61\u01a6\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\7\62\u01b1\n\62\f\62\16\62")
        buf.write("\u01b4\13\62\3\62\3\62\3\62\3\62\5\62\u01ba\n\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\5\66\u01cb\n\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\39\39\59\u01d7\n9\3:\3:\3:\3:\3:\5:\u01de\n:\3")
        buf.write(";\3;\5;\u01e2\n;\3<\3<\3<\3<\3<\3<\3<\2\5$&(=\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\t\3\2\t\13\3\2\4\6")
        buf.write("\5\2$&((.\60\3\2\33\34\3\2)*\3\2+-\3\3\"\"\2\u01e6\2x")
        buf.write("\3\2\2\2\4\177\3\2\2\2\6\u0086\3\2\2\2\b\u008a\3\2\2\2")
        buf.write("\n\u008e\3\2\2\2\f\u0095\3\2\2\2\16\u0099\3\2\2\2\20\u009b")
        buf.write("\3\2\2\2\22\u00a3\3\2\2\2\24\u00a5\3\2\2\2\26\u00a7\3")
        buf.write("\2\2\2\30\u00ad\3\2\2\2\32\u00b4\3\2\2\2\34\u00b8\3\2")
        buf.write("\2\2\36\u00ba\3\2\2\2 \u00c1\3\2\2\2\"\u00c8\3\2\2\2$")
        buf.write("\u00ca\3\2\2\2&\u00d5\3\2\2\2(\u00e0\3\2\2\2*\u00ee\3")
        buf.write("\2\2\2,\u00f3\3\2\2\2.\u00f5\3\2\2\2\60\u00ff\3\2\2\2")
        buf.write("\62\u0109\3\2\2\2\64\u010d\3\2\2\2\66\u011f\3\2\2\28\u0132")
        buf.write("\3\2\2\2:\u0138\3\2\2\2<\u013c\3\2\2\2>\u013e\3\2\2\2")
        buf.write("@\u0146\3\2\2\2B\u014d\3\2\2\2D\u0151\3\2\2\2F\u0158\3")
        buf.write("\2\2\2H\u0166\3\2\2\2J\u0168\3\2\2\2L\u016c\3\2\2\2N\u0172")
        buf.write("\3\2\2\2P\u0176\3\2\2\2R\u017f\3\2\2\2T\u0186\3\2\2\2")
        buf.write("V\u018a\3\2\2\2X\u0190\3\2\2\2Z\u0198\3\2\2\2\\\u019d")
        buf.write("\3\2\2\2^\u019f\3\2\2\2`\u01a5\3\2\2\2b\u01a7\3\2\2\2")
        buf.write("d\u01bb\3\2\2\2f\u01c4\3\2\2\2h\u01c6\3\2\2\2j\u01c8\3")
        buf.write("\2\2\2l\u01cc\3\2\2\2n\u01cf\3\2\2\2p\u01d6\3\2\2\2r\u01dd")
        buf.write("\3\2\2\2t\u01e1\3\2\2\2v\u01e3\3\2\2\2xy\5\4\3\2yz\5\20")
        buf.write("\t\2z{\5\n\6\2{|\7\2\2\3|\3\3\2\2\2}\u0080\5\6\4\2~\u0080")
        buf.write("\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\5\3\2\2\2\u0081")
        buf.write("\u0082\5\b\5\2\u0082\u0083\5P)\2\u0083\u0084\5\6\4\2\u0084")
        buf.write("\u0087\3\2\2\2\u0085\u0087\5\b\5\2\u0086\u0081\3\2\2\2")
        buf.write("\u0086\u0085\3\2\2\2\u0087\7\3\2\2\2\u0088\u008b\5\64")
        buf.write("\33\2\u0089\u008b\5<\37\2\u008a\u0088\3\2\2\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\t\3\2\2\2\u008c\u008f\5\f\7\2\u008d\u008f")
        buf.write("\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\13\3\2\2\2\u0090\u0091\5\16\b\2\u0091\u0092\5P)\2\u0092")
        buf.write("\u0093\5\f\7\2\u0093\u0096\3\2\2\2\u0094\u0096\5\16\b")
        buf.write("\2\u0095\u0090\3\2\2\2\u0095\u0094\3\2\2\2\u0096\r\3\2")
        buf.write("\2\2\u0097\u009a\5\64\33\2\u0098\u009a\5J&\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u0098\3\2\2\2\u009a\17\3\2\2\2\u009b\u009c")
        buf.write("\7\17\2\2\u009c\u009d\7\3\2\2\u009d\u009e\7\35\2\2\u009e")
        buf.write("\u009f\5@!\2\u009f\u00a0\7\36\2\2\u00a0\u00a1\5P)\2\u00a1")
        buf.write("\u00a2\5v<\2\u00a2\21\3\2\2\2\u00a3\u00a4\t\2\2\2\u00a4")
        buf.write("\23\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6\25\3\2\2\2\u00a7")
        buf.write("\u00a8\7\37\2\2\u00a8\u00a9\5\30\r\2\u00a9\u00aa\7 \2")
        buf.write("\2\u00aa\27\3\2\2\2\u00ab\u00ae\5\32\16\2\u00ac\u00ae")
        buf.write("\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\31\3\2\2\2\u00af\u00b0\5\34\17\2\u00b0\u00b1\7!\2\2\u00b1")
        buf.write("\u00b2\5\32\16\2\u00b2\u00b5\3\2\2\2\u00b3\u00b5\5\34")
        buf.write("\17\2\u00b4\u00af\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\33")
        buf.write("\3\2\2\2\u00b6\u00b9\5 \21\2\u00b7\u00b9\5\26\f\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\35\3\2\2\2\u00ba")
        buf.write("\u00bb\7\61\2\2\u00bb\37\3\2\2\2\u00bc\u00bd\5\"\22\2")
        buf.write("\u00bd\u00be\7\'\2\2\u00be\u00bf\5\"\22\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00c2\5\"\22\2\u00c1\u00bc\3\2\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2!\3\2\2\2\u00c3\u00c4\5$\23\2\u00c4")
        buf.write("\u00c5\t\4\2\2\u00c5\u00c6\5$\23\2\u00c6\u00c9\3\2\2\2")
        buf.write("\u00c7\u00c9\5$\23\2\u00c8\u00c3\3\2\2\2\u00c8\u00c7\3")
        buf.write("\2\2\2\u00c9#\3\2\2\2\u00ca\u00cb\b\23\1\2\u00cb\u00cc")
        buf.write("\5&\24\2\u00cc\u00d2\3\2\2\2\u00cd\u00ce\f\4\2\2\u00ce")
        buf.write("\u00cf\t\5\2\2\u00cf\u00d1\5&\24\2\u00d0\u00cd\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3%\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6")
        buf.write("\b\24\1\2\u00d6\u00d7\5(\25\2\u00d7\u00dd\3\2\2\2\u00d8")
        buf.write("\u00d9\f\4\2\2\u00d9\u00da\t\6\2\2\u00da\u00dc\5(\25\2")
        buf.write("\u00db\u00d8\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3")
        buf.write("\2\2\2\u00dd\u00de\3\2\2\2\u00de\'\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00e0\u00e1\b\25\1\2\u00e1\u00e2\5*\26\2\u00e2")
        buf.write("\u00e8\3\2\2\2\u00e3\u00e4\f\4\2\2\u00e4\u00e5\t\7\2\2")
        buf.write("\u00e5\u00e7\5*\26\2\u00e6\u00e3\3\2\2\2\u00e7\u00ea\3")
        buf.write("\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9)")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ec\7\32\2\2\u00ec")
        buf.write("\u00ef\5*\26\2\u00ed\u00ef\5,\27\2\u00ee\u00eb\3\2\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef+\3\2\2\2\u00f0\u00f1\7*\2\2")
        buf.write("\u00f1\u00f4\5,\27\2\u00f2\u00f4\5\62\32\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4-\3\2\2\2\u00f5\u00f6")
        buf.write("\5\36\20\2\u00f6\u00f7\7\37\2\2\u00f7\u00f8\5\60\31\2")
        buf.write("\u00f8\u00f9\7 \2\2\u00f9/\3\2\2\2\u00fa\u0100\5 \21\2")
        buf.write("\u00fb\u00fc\5 \21\2\u00fc\u00fd\7!\2\2\u00fd\u00fe\5")
        buf.write("\60\31\2\u00fe\u0100\3\2\2\2\u00ff\u00fa\3\2\2\2\u00ff")
        buf.write("\u00fb\3\2\2\2\u0100\61\3\2\2\2\u0101\u010a\5\24\13\2")
        buf.write("\u0102\u010a\5\36\20\2\u0103\u010a\5.\30\2\u0104\u010a")
        buf.write("\5n8\2\u0105\u0106\7\35\2\2\u0106\u0107\5 \21\2\u0107")
        buf.write("\u0108\7\36\2\2\u0108\u010a\3\2\2\2\u0109\u0101\3\2\2")
        buf.write("\2\u0109\u0102\3\2\2\2\u0109\u0103\3\2\2\2\u0109\u0104")
        buf.write("\3\2\2\2\u0109\u0105\3\2\2\2\u010a\63\3\2\2\2\u010b\u010e")
        buf.write("\5\66\34\2\u010c\u010e\58\35\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e\65\3\2\2\2\u010f\u0110\5\22\n\2\u0110")
        buf.write("\u0113\5\36\20\2\u0111\u0112\7#\2\2\u0112\u0114\5 \21")
        buf.write("\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0120")
        buf.write("\3\2\2\2\u0115\u0116\7\r\2\2\u0116\u0117\5\36\20\2\u0117")
        buf.write("\u0118\7#\2\2\u0118\u0119\5 \21\2\u0119\u0120\3\2\2\2")
        buf.write("\u011a\u011b\7\16\2\2\u011b\u011c\5\36\20\2\u011c\u011d")
        buf.write("\7#\2\2\u011d\u011e\5 \21\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u010f\3\2\2\2\u011f\u0115\3\2\2\2\u011f\u011a\3\2\2\2")
        buf.write("\u0120\67\3\2\2\2\u0121\u0122\5\22\n\2\u0122\u0123\5\36")
        buf.write("\20\2\u0123\u0124\7\37\2\2\u0124\u0125\5:\36\2\u0125\u0128")
        buf.write("\7 \2\2\u0126\u0127\7#\2\2\u0127\u0129\5\26\f\2\u0128")
        buf.write("\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u0133\3\2\2\2")
        buf.write("\u012a\u012b\7\r\2\2\u012b\u012c\5\36\20\2\u012c\u012d")
        buf.write("\7\37\2\2\u012d\u012e\5:\36\2\u012e\u012f\7 \2\2\u012f")
        buf.write("\u0130\7#\2\2\u0130\u0131\5\26\f\2\u0131\u0133\3\2\2\2")
        buf.write("\u0132\u0121\3\2\2\2\u0132\u012a\3\2\2\2\u01339\3\2\2")
        buf.write("\2\u0134\u0135\7\4\2\2\u0135\u0136\7!\2\2\u0136\u0139")
        buf.write("\5:\36\2\u0137\u0139\7\4\2\2\u0138\u0134\3\2\2\2\u0138")
        buf.write("\u0137\3\2\2\2\u0139;\3\2\2\2\u013a\u013d\5> \2\u013b")
        buf.write("\u013d\5J&\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("=\3\2\2\2\u013e\u013f\7\17\2\2\u013f\u0140\5\36\20\2\u0140")
        buf.write("\u0141\7\35\2\2\u0141\u0142\5@!\2\u0142\u0143\7\36\2\2")
        buf.write("\u0143?\3\2\2\2\u0144\u0147\5B\"\2\u0145\u0147\3\2\2\2")
        buf.write("\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147A\3\2\2")
        buf.write("\2\u0148\u0149\5D#\2\u0149\u014a\7!\2\2\u014a\u014b\5")
        buf.write("B\"\2\u014b\u014e\3\2\2\2\u014c\u014e\5D#\2\u014d\u0148")
        buf.write("\3\2\2\2\u014d\u014c\3\2\2\2\u014eC\3\2\2\2\u014f\u0152")
        buf.write("\5F$\2\u0150\u0152\5H%\2\u0151\u014f\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152E\3\2\2\2\u0153\u0154\5\22\n\2\u0154\u0155")
        buf.write("\5\36\20\2\u0155\u0159\3\2\2\2\u0156\u0157\7\r\2\2\u0157")
        buf.write("\u0159\5\36\20\2\u0158\u0153\3\2\2\2\u0158\u0156\3\2\2")
        buf.write("\2\u0159G\3\2\2\2\u015a\u015b\5\22\n\2\u015b\u015c\5\36")
        buf.write("\20\2\u015c\u015d\7\37\2\2\u015d\u015e\5:\36\2\u015e\u015f")
        buf.write("\7 \2\2\u015f\u0167\3\2\2\2\u0160\u0161\7\r\2\2\u0161")
        buf.write("\u0162\5\36\20\2\u0162\u0163\7\37\2\2\u0163\u0164\5:\36")
        buf.write("\2\u0164\u0165\7 \2\2\u0165\u0167\3\2\2\2\u0166\u015a")
        buf.write("\3\2\2\2\u0166\u0160\3\2\2\2\u0167I\3\2\2\2\u0168\u0169")
        buf.write("\5> \2\u0169\u016a\5P)\2\u016a\u016b\5R*\2\u016bK\3\2")
        buf.write("\2\2\u016c\u016d\t\b\2\2\u016dM\3\2\2\2\u016e\u016f\7")
        buf.write("\"\2\2\u016f\u0173\5N(\2\u0170\u0173\7\"\2\2\u0171\u0173")
        buf.write("\7\2\2\3\u0172\u016e\3\2\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write("\u0171\3\2\2\2\u0173O\3\2\2\2\u0174\u0177\5N(\2\u0175")
        buf.write("\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2")
        buf.write("\u0177Q\3\2\2\2\u0178\u0179\5j\66\2\u0179\u017a\5L\'\2")
        buf.write("\u017a\u0180\3\2\2\2\u017b\u017c\5v<\2\u017c\u017d\5L")
        buf.write("\'\2\u017d\u0180\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u0178")
        buf.write("\3\2\2\2\u017f\u017b\3\2\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("S\3\2\2\2\u0181\u0182\5V,\2\u0182\u0183\5P)\2\u0183\u0184")
        buf.write("\5T+\2\u0184\u0187\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0181")
        buf.write("\3\2\2\2\u0186\u0185\3\2\2\2\u0187U\3\2\2\2\u0188\u018b")
        buf.write("\5b\62\2\u0189\u018b\5X-\2\u018a\u0188\3\2\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018bW\3\2\2\2\u018c\u018d\5Z.\2\u018d\u018e")
        buf.write("\5L\'\2\u018e\u0191\3\2\2\2\u018f\u0191\5\\/\2\u0190\u018c")
        buf.write("\3\2\2\2\u0190\u018f\3\2\2\2\u0191Y\3\2\2\2\u0192\u0199")
        buf.write("\5\64\33\2\u0193\u0199\5^\60\2\u0194\u0199\5f\64\2\u0195")
        buf.write("\u0199\5h\65\2\u0196\u0199\5j\66\2\u0197\u0199\5l\67\2")
        buf.write("\u0198\u0192\3\2\2\2\u0198\u0193\3\2\2\2\u0198\u0194\3")
        buf.write("\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199[\3\2\2\2\u019a\u019e\5d\63\2\u019b\u019e")
        buf.write("\5v<\2\u019c\u019e\5<\37\2\u019d\u019a\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019d\u019c\3\2\2\2\u019e]\3\2\2\2\u019f\u01a0")
        buf.write("\5`\61\2\u01a0\u01a1\7#\2\2\u01a1\u01a2\5 \21\2\u01a2")
        buf.write("_\3\2\2\2\u01a3\u01a6\5\36\20\2\u01a4\u01a6\5.\30\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6a\3\2\2\2\u01a7")
        buf.write("\u01a8\7\25\2\2\u01a8\u01a9\5 \21\2\u01a9\u01aa\5P)\2")
        buf.write("\u01aa\u01b2\5V,\2\u01ab\u01ac\7\27\2\2\u01ac\u01ad\5")
        buf.write(" \21\2\u01ad\u01ae\5P)\2\u01ae\u01af\5V,\2\u01af\u01b1")
        buf.write("\3\2\2\2\u01b0\u01ab\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7\26\2\2\u01b6\u01b7")
        buf.write("\5 \21\2\u01b7\u01b9\5P)\2\u01b8\u01ba\5V,\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01bac\3\2\2\2\u01bb\u01bc")
        buf.write("\7\20\2\2\u01bc\u01bd\5\36\20\2\u01bd\u01be\7\21\2\2\u01be")
        buf.write("\u01bf\5 \21\2\u01bf\u01c0\7\22\2\2\u01c0\u01c1\5 \21")
        buf.write("\2\u01c1\u01c2\5P)\2\u01c2\u01c3\5V,\2\u01c3e\3\2\2\2")
        buf.write("\u01c4\u01c5\7\23\2\2\u01c5g\3\2\2\2\u01c6\u01c7\7\24")
        buf.write("\2\2\u01c7i\3\2\2\2\u01c8\u01ca\7\f\2\2\u01c9\u01cb\5")
        buf.write(" \21\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cbk")
        buf.write("\3\2\2\2\u01cc\u01cd\5n8\2\u01cd\u01ce\5L\'\2\u01cem\3")
        buf.write("\2\2\2\u01cf\u01d0\5\36\20\2\u01d0\u01d1\7\35\2\2\u01d1")
        buf.write("\u01d2\5p9\2\u01d2\u01d3\7\36\2\2\u01d3o\3\2\2\2\u01d4")
        buf.write("\u01d7\5r:\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7q\3\2\2\2\u01d8\u01d9\5t;\2\u01d9")
        buf.write("\u01da\7!\2\2\u01da\u01db\5r:\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01de\5t;\2\u01dd\u01d8\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("s\3\2\2\2\u01df\u01e2\5D#\2\u01e0\u01e2\5 \21\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2u\3\2\2\2\u01e3")
        buf.write("\u01e4\7\30\2\2\u01e4\u01e5\5N(\2\u01e5\u01e6\5T+\2\u01e6")
        buf.write("\u01e7\7\31\2\2\u01e7\u01e8\5N(\2\u01e8w\3\2\2\2/\177")
        buf.write("\u0086\u008a\u008e\u0095\u0099\u00ad\u00b4\u00b8\u00c1")
        buf.write("\u00c8\u00d2\u00dd\u00e8\u00ee\u00f3\u00ff\u0109\u010d")
        buf.write("\u0113\u011f\u0128\u0132\u0138\u013c\u0146\u014d\u0151")
        buf.write("\u0158\u0166\u0172\u0176\u017f\u0186\u018a\u0190\u0198")
        buf.write("\u019d\u01a5\u01b2\u01b9\u01ca\u01d6\u01dd\u01e1")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
                     "'or'", "'('", "')'", "'['", "']'", "','", "'\n'", 
                     "'<-'", "'!='", "'>='", "'<='", "'...'", "'=='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBER_L", "BOOL_L", "STRING_L", 
                      "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                      "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "COMMA", "NEWLINE", "ASSIGN", "NEQ", "GTEQ", 
                      "LTEQ", "CONCAT", "STRING_EQ", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "GT", "LT", "NUMBER_EQ", "IDENTIFIER", 
                      "COMMENT", "WHITESPACE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_pre_declaration_list = 1
    RULE_pre_declaration_prime = 2
    RULE_pre_declaration = 3
    RULE_post_declaration_list = 4
    RULE_post_declaration_prime = 5
    RULE_post_declaration = 6
    RULE_main_function = 7
    RULE_primitive_type = 8
    RULE_primitive_literals = 9
    RULE_array_value = 10
    RULE_array_literal_list = 11
    RULE_array_literal_prime = 12
    RULE_array_literal = 13
    RULE_identifier = 14
    RULE_expression = 15
    RULE_relational_expr = 16
    RULE_logical_expr1 = 17
    RULE_numeric_expr1 = 18
    RULE_numeric_expr2 = 19
    RULE_logical_expr2 = 20
    RULE_numeric_expr3 = 21
    RULE_element_expr = 22
    RULE_index_op_expr = 23
    RULE_term = 24
    RULE_variable_declaration = 25
    RULE_primitive_type_declaration = 26
    RULE_array_type_declaration = 27
    RULE_number_literal_list = 28
    RULE_function_declaration = 29
    RULE_function_prototype_declaration = 30
    RULE_parameter_list = 31
    RULE_parameter_prime = 32
    RULE_parameter = 33
    RULE_primitive_parameter = 34
    RULE_array_parameter = 35
    RULE_function_full_declaration = 36
    RULE_newline = 37
    RULE_newline_list = 38
    RULE_nullable_newline_list = 39
    RULE_function_body = 40
    RULE_statement_list = 41
    RULE_statement = 42
    RULE_non_if_statement = 43
    RULE_simple_statement = 44
    RULE_compound_statement = 45
    RULE_assignment_statement = 46
    RULE_assignee = 47
    RULE_if_statement = 48
    RULE_for_statement = 49
    RULE_break_statement = 50
    RULE_continue_statement = 51
    RULE_return_statement = 52
    RULE_function_call_statement = 53
    RULE_function_call = 54
    RULE_argument_list = 55
    RULE_argument_prime = 56
    RULE_argument = 57
    RULE_block_statement = 58

    ruleNames =  [ "program", "pre_declaration_list", "pre_declaration_prime", 
                   "pre_declaration", "post_declaration_list", "post_declaration_prime", 
                   "post_declaration", "main_function", "primitive_type", 
                   "primitive_literals", "array_value", "array_literal_list", 
                   "array_literal_prime", "array_literal", "identifier", 
                   "expression", "relational_expr", "logical_expr1", "numeric_expr1", 
                   "numeric_expr2", "logical_expr2", "numeric_expr3", "element_expr", 
                   "index_op_expr", "term", "variable_declaration", "primitive_type_declaration", 
                   "array_type_declaration", "number_literal_list", "function_declaration", 
                   "function_prototype_declaration", "parameter_list", "parameter_prime", 
                   "parameter", "primitive_parameter", "array_parameter", 
                   "function_full_declaration", "newline", "newline_list", 
                   "nullable_newline_list", "function_body", "statement_list", 
                   "statement", "non_if_statement", "simple_statement", 
                   "compound_statement", "assignment_statement", "assignee", 
                   "if_statement", "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "function_call_statement", "function_call", 
                   "argument_list", "argument_prime", "argument", "block_statement" ]

    EOF = Token.EOF
    T__0=1
    NUMBER_L=2
    BOOL_L=3
    STRING_L=4
    TRUE=5
    FALSE=6
    NUMBER=7
    BOOL=8
    STRING=9
    RETURN=10
    VAR=11
    DYNAMIC=12
    FUNC=13
    FOR=14
    UNTIL=15
    BY=16
    BREAK=17
    CONTINUE=18
    IF=19
    ELSE=20
    ELIF=21
    BEGIN=22
    END=23
    NOT=24
    AND=25
    OR=26
    LPAREN=27
    RPAREN=28
    LBRACKET=29
    RBRACKET=30
    COMMA=31
    NEWLINE=32
    ASSIGN=33
    NEQ=34
    GTEQ=35
    LTEQ=36
    CONCAT=37
    STRING_EQ=38
    PLUS=39
    MINUS=40
    MUL=41
    DIV=42
    MOD=43
    GT=44
    LT=45
    NUMBER_EQ=46
    IDENTIFIER=47
    COMMENT=48
    WHITESPACE=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51
    ERROR_CHAR=52

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

        def pre_declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declaration_listContext,0)


        def main_function(self):
            return self.getTypedRuleContext(ZCodeParser.Main_functionContext,0)


        def post_declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declaration_listContext,0)


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
            self.state = 118
            self.pre_declaration_list()
            self.state = 119
            self.main_function()
            self.state = 120
            self.post_declaration_list()
            self.state = 121
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pre_declaration_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declaration_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_pre_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_declaration_list" ):
                return visitor.visitPre_declaration_list(self)
            else:
                return visitor.visitChildren(self)




    def pre_declaration_list(self):

        localctx = ZCodeParser.Pre_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pre_declaration_list)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.pre_declaration_prime()
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


    class Pre_declaration_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pre_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def pre_declaration_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declaration_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_pre_declaration_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_declaration_prime" ):
                return visitor.visitPre_declaration_prime(self)
            else:
                return visitor.visitChildren(self)




    def pre_declaration_prime(self):

        localctx = ZCodeParser.Pre_declaration_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pre_declaration_prime)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.pre_declaration()
                self.state = 128
                self.nullable_newline_list()
                self.state = 129
                self.pre_declaration_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.pre_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_pre_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_declaration" ):
                return visitor.visitPre_declaration(self)
            else:
                return visitor.visitChildren(self)




    def pre_declaration(self):

        localctx = ZCodeParser.Pre_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pre_declaration)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.function_declaration()
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


    class Post_declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def post_declaration_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declaration_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_post_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_declaration_list" ):
                return visitor.visitPost_declaration_list(self)
            else:
                return visitor.visitChildren(self)




    def post_declaration_list(self):

        localctx = ZCodeParser.Post_declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_post_declaration_list)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.post_declaration_prime()
                pass
            elif token in [ZCodeParser.EOF]:
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


    class Post_declaration_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def post_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def post_declaration_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declaration_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_post_declaration_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_declaration_prime" ):
                return visitor.visitPost_declaration_prime(self)
            else:
                return visitor.visitChildren(self)




    def post_declaration_prime(self):

        localctx = ZCodeParser.Post_declaration_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_post_declaration_prime)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.post_declaration()
                self.state = 143
                self.nullable_newline_list()
                self.state = 144
                self.post_declaration_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.post_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_full_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_full_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_post_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_declaration" ):
                return visitor.visitPost_declaration(self)
            else:
                return visitor.visitChildren(self)




    def post_declaration(self):

        localctx = ZCodeParser.Post_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_post_declaration)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.function_full_declaration()
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


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = ZCodeParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ZCodeParser.FUNC)
            self.state = 154
            self.match(ZCodeParser.T__0)
            self.state = 155
            self.match(ZCodeParser.LPAREN)
            self.state = 156
            self.parameter_list()
            self.state = 157
            self.match(ZCodeParser.RPAREN)
            self.state = 158
            self.nullable_newline_list()
            self.state = 159
            self.block_statement()
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
        self.enterRule(localctx, 16, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
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
        self.enterRule(localctx, 18, self.RULE_primitive_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
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
        self.enterRule(localctx, 20, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ZCodeParser.LBRACKET)
            self.state = 166
            self.array_literal_list()
            self.state = 167
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
        self.enterRule(localctx, 22, self.RULE_array_literal_list)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
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
        self.enterRule(localctx, 24, self.RULE_array_literal_prime)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.array_literal()
                self.state = 174
                self.match(ZCodeParser.COMMA)
                self.state = 175
                self.array_literal_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
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
        self.enterRule(localctx, 26, self.RULE_array_literal)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expression()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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
        self.enterRule(localctx, 28, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
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
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.relational_expr()
                self.state = 187
                self.match(ZCodeParser.CONCAT)
                self.state = 188
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
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
        self.enterRule(localctx, 32, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.logical_expr1(0)
                self.state = 194
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NEQ) | (1 << ZCodeParser.GTEQ) | (1 << ZCodeParser.LTEQ) | (1 << ZCodeParser.STRING_EQ) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.NUMBER_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 195
                self.logical_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_logical_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.numeric_expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr1)
                    self.state = 203
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 204
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 205
                    self.numeric_expr1(0) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_numeric_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.numeric_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr1)
                    self.state = 214
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 215
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 216
                    self.numeric_expr2(0) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_numeric_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.logical_expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr2)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.logical_expr2() 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_logical_expr2)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.NOT)
                self.state = 234
                self.logical_expr2()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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
        self.enterRule(localctx, 42, self.RULE_numeric_expr3)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(ZCodeParser.MINUS)
                self.state = 239
                self.numeric_expr3()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = ZCodeParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.identifier()
            self.state = 244
            self.match(ZCodeParser.LBRACKET)
            self.state = 245
            self.index_op_expr()
            self.state = 246
            self.match(ZCodeParser.RBRACKET)
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
        self.enterRule(localctx, 46, self.RULE_index_op_expr)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.expression()
                self.state = 250
                self.match(ZCodeParser.COMMA)
                self.state = 251
                self.index_op_expr()
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


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


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
        self.enterRule(localctx, 48, self.RULE_term)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.primitive_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.element_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.match(ZCodeParser.LPAREN)
                self.state = 260
                self.expression()
                self.state = 261
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
        self.enterRule(localctx, 50, self.RULE_variable_declaration)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.primitive_type_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 52, self.RULE_primitive_type_declaration)
        self._la = 0 # Token type
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.primitive_type()
                self.state = 270
                self.identifier()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 271
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 272
                    self.expression()


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(ZCodeParser.VAR)
                self.state = 276
                self.identifier()
                self.state = 277
                self.match(ZCodeParser.ASSIGN)
                self.state = 278
                self.expression()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(ZCodeParser.DYNAMIC)
                self.state = 281
                self.identifier()
                self.state = 282
                self.match(ZCodeParser.ASSIGN)
                self.state = 283
                self.expression()
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


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_declaration" ):
                return visitor.visitArray_type_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_type_declaration(self):

        localctx = ZCodeParser.Array_type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_type_declaration)
        self._la = 0 # Token type
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.primitive_type()
                self.state = 288
                self.identifier()
                self.state = 289
                self.match(ZCodeParser.LBRACKET)
                self.state = 290
                self.number_literal_list()
                self.state = 291
                self.match(ZCodeParser.RBRACKET)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 292
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 293
                    self.array_value()


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(ZCodeParser.VAR)
                self.state = 297
                self.identifier()
                self.state = 298
                self.match(ZCodeParser.LBRACKET)
                self.state = 299
                self.number_literal_list()
                self.state = 300
                self.match(ZCodeParser.RBRACKET)
                self.state = 301
                self.match(ZCodeParser.ASSIGN)
                self.state = 302
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
        self.enterRule(localctx, 56, self.RULE_number_literal_list)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(ZCodeParser.NUMBER_L)
                self.state = 307
                self.match(ZCodeParser.COMMA)
                self.state = 308
                self.number_literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
        self.enterRule(localctx, 58, self.RULE_function_declaration)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.function_prototype_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_prototype_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_prototype_declaration" ):
                return visitor.visitFunction_prototype_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_prototype_declaration(self):

        localctx = ZCodeParser.Function_prototype_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_function_prototype_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ZCodeParser.FUNC)
            self.state = 317
            self.identifier()
            self.state = 318
            self.match(ZCodeParser.LPAREN)
            self.state = 319
            self.parameter_list()
            self.state = 320
            self.match(ZCodeParser.RPAREN)
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
        self.enterRule(localctx, 62, self.RULE_parameter_list)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
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
        self.enterRule(localctx, 64, self.RULE_parameter_prime)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.parameter()
                self.state = 327
                self.match(ZCodeParser.COMMA)
                self.state = 328
                self.parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
        self.enterRule(localctx, 66, self.RULE_parameter)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.primitive_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_parameter" ):
                return visitor.visitPrimitive_parameter(self)
            else:
                return visitor.visitChildren(self)




    def primitive_parameter(self):

        localctx = ZCodeParser.Primitive_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_primitive_parameter)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.primitive_type()
                self.state = 338
                self.identifier()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(ZCodeParser.VAR)
                self.state = 341
                self.identifier()
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

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_parameter" ):
                return visitor.visitArray_parameter(self)
            else:
                return visitor.visitChildren(self)




    def array_parameter(self):

        localctx = ZCodeParser.Array_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_parameter)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.primitive_type()
                self.state = 345
                self.identifier()
                self.state = 346
                self.match(ZCodeParser.LBRACKET)
                self.state = 347
                self.number_literal_list()
                self.state = 348
                self.match(ZCodeParser.RBRACKET)
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(ZCodeParser.VAR)
                self.state = 351
                self.identifier()
                self.state = 352
                self.match(ZCodeParser.LBRACKET)
                self.state = 353
                self.number_literal_list()
                self.state = 354
                self.match(ZCodeParser.RBRACKET)
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


    class Function_full_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_prototype_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_prototype_declarationContext,0)


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
        self.enterRule(localctx, 72, self.RULE_function_full_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.function_prototype_declaration()
            self.state = 359
            self.nullable_newline_list()
            self.state = 360
            self.function_body()
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

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = ZCodeParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_newline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.EOF or _la==ZCodeParser.NEWLINE):
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


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_newline_list)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.match(ZCodeParser.NEWLINE)
                self.state = 365
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.match(ZCodeParser.EOF)
                pass


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
        self.enterRule(localctx, 78, self.RULE_nullable_newline_list)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
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


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


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
        self.enterRule(localctx, 80, self.RULE_function_body)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.return_statement()
                self.state = 375
                self.newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.block_statement()
                self.state = 378
                self.newline()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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
        self.enterRule(localctx, 82, self.RULE_statement_list)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.statement()
                self.state = 384
                self.nullable_newline_list()
                self.state = 385
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
        self.enterRule(localctx, 84, self.RULE_statement)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.if_statement()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
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


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


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
        self.enterRule(localctx, 86, self.RULE_non_if_statement)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.simple_statement()
                self.state = 395
                self.newline()
                pass
            elif token in [ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
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
        self.enterRule(localctx, 88, self.RULE_simple_statement)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 405
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


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_compound_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_statement" ):
                return visitor.visitCompound_statement(self)
            else:
                return visitor.visitChildren(self)




    def compound_statement(self):

        localctx = ZCodeParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_compound_statement)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.for_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.block_statement()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.function_declaration()
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.assignee()
            self.state = 414
            self.match(ZCodeParser.ASSIGN)
            self.state = 415
            self.expression()
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


        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignee" ):
                return visitor.visitAssignee(self)
            else:
                return visitor.visitChildren(self)




    def assignee(self):

        localctx = ZCodeParser.AssigneeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assignee)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.element_expr()
                pass


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

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def nullable_newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Nullable_newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(ZCodeParser.IF)
            self.state = 422
            self.expression()
            self.state = 423
            self.nullable_newline_list()
            self.state = 424
            self.statement()
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.ELIF:
                self.state = 425
                self.match(ZCodeParser.ELIF)
                self.state = 426
                self.expression()
                self.state = 427
                self.nullable_newline_list()
                self.state = 428
                self.statement()
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.match(ZCodeParser.ELSE)
            self.state = 436
            self.expression()
            self.state = 437
            self.nullable_newline_list()
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 438
                self.statement()


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
        self.enterRule(localctx, 98, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.FOR)
            self.state = 442
            self.identifier()
            self.state = 443
            self.match(ZCodeParser.UNTIL)
            self.state = 444
            self.expression()
            self.state = 445
            self.match(ZCodeParser.BY)
            self.state = 446
            self.expression()
            self.state = 447
            self.nullable_newline_list()
            self.state = 448
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ZCodeParser.BREAK)
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(ZCodeParser.CONTINUE)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(ZCodeParser.RETURN)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_L) | (1 << ZCodeParser.BOOL_L) | (1 << ZCodeParser.STRING_L) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 455
                self.expression()


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
        self.enterRule(localctx, 106, self.RULE_function_call_statement)
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
        self.enterRule(localctx, 108, self.RULE_function_call)
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
        self.enterRule(localctx, 110, self.RULE_argument_list)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
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
        self.enterRule(localctx, 112, self.RULE_argument_prime)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
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

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ZCodeParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_argument)
        try:
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.parameter()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.expression()
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
        self.enterRule(localctx, 116, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(ZCodeParser.BEGIN)
            self.state = 482
            self.newline_list()
            self.state = 483
            self.statement_list()
            self.state = 484
            self.match(ZCodeParser.END)
            self.state = 485
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
        self._predicates[17] = self.logical_expr1_sempred
        self._predicates[18] = self.numeric_expr1_sempred
        self._predicates[19] = self.numeric_expr2_sempred
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
         




