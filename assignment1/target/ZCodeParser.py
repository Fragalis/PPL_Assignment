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
        buf.write("\u01f5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\u008b\n\3\3\4\3\4\5\4\u008f\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u009d\n\6\3\7\3\7\5\7\u00a1\n\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\5\13\u00ad\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00b4\n\f\3\r\3\r\5\r\u00b8\n\r\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00c1\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00c8\n\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\7\21\u00d0\n\21\f\21\16\21\u00d3\13\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u00db\n\22\f\22\16\22\u00de\13\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e6\n\23\f\23\16")
        buf.write("\23\u00e9\13\23\3\24\3\24\3\24\5\24\u00ee\n\24\3\25\3")
        buf.write("\25\3\25\5\25\u00f3\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u00ff\n\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0106\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0110\n\30\3\31\3\31\5\31\u0114\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0128\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u0138\n\33\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u013e\n\34\3\35\3\35\5\35\u0142\n\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\5\37\u014d\n\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u0154\n \3!\3!\5!\u0158\n!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\5%\u016d\n")
        buf.write("%\3&\3&\3&\5&\u0172\n&\3\'\3\'\3(\3(\5(\u0178\n(\3)\3")
        buf.write(")\3)\3)\3)\5)\u017f\n)\3*\3*\5*\u0183\n*\3+\3+\5+\u0187")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\5,\u018f\n,\3-\3-\5-\u0193\n-\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\5/\u019c\n/\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u01ab")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01b7\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\3")
        buf.write("9\39\39\39\39\39\59\u01d2\n9\3:\3:\3:\3;\3;\3;\3;\3;\3")
        buf.write("<\3<\5<\u01de\n<\3=\3=\3=\3=\3=\5=\u01e5\n=\3>\3>\3>\3")
        buf.write(">\3>\3>\5>\u01ed\n>\3?\3?\3?\3?\3?\3?\3?\2\5 \"$@\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|\2\b\3\2\t\13\3")
        buf.write("\2\4\6\5\2$&((.\60\3\2\33\34\3\2)*\3\2+-\2\u01e7\2~\3")
        buf.write("\2\2\2\4\u008a\3\2\2\2\6\u008e\3\2\2\2\b\u0090\3\2\2\2")
        buf.write("\n\u009c\3\2\2\2\f\u00a0\3\2\2\2\16\u00a2\3\2\2\2\20\u00a4")
        buf.write("\3\2\2\2\22\u00a6\3\2\2\2\24\u00ac\3\2\2\2\26\u00b3\3")
        buf.write("\2\2\2\30\u00b7\3\2\2\2\32\u00b9\3\2\2\2\34\u00c0\3\2")
        buf.write("\2\2\36\u00c7\3\2\2\2 \u00c9\3\2\2\2\"\u00d4\3\2\2\2$")
        buf.write("\u00df\3\2\2\2&\u00ed\3\2\2\2(\u00f2\3\2\2\2*\u00fe\3")
        buf.write("\2\2\2,\u0105\3\2\2\2.\u010f\3\2\2\2\60\u0113\3\2\2\2")
        buf.write("\62\u0127\3\2\2\2\64\u0137\3\2\2\2\66\u013d\3\2\2\28\u0141")
        buf.write("\3\2\2\2:\u0143\3\2\2\2<\u014c\3\2\2\2>\u0153\3\2\2\2")
        buf.write("@\u0157\3\2\2\2B\u0159\3\2\2\2D\u015c\3\2\2\2F\u0162\3")
        buf.write("\2\2\2H\u016c\3\2\2\2J\u0171\3\2\2\2L\u0173\3\2\2\2N\u0177")
        buf.write("\3\2\2\2P\u017e\3\2\2\2R\u0182\3\2\2\2T\u0186\3\2\2\2")
        buf.write("V\u018e\3\2\2\2X\u0192\3\2\2\2Z\u0194\3\2\2\2\\\u019b")
        buf.write("\3\2\2\2^\u019d\3\2\2\2`\u01a1\3\2\2\2b\u01aa\3\2\2\2")
        buf.write("d\u01ac\3\2\2\2f\u01b6\3\2\2\2h\u01b8\3\2\2\2j\u01bc\3")
        buf.write("\2\2\2l\u01c5\3\2\2\2n\u01c8\3\2\2\2p\u01d1\3\2\2\2r\u01d3")
        buf.write("\3\2\2\2t\u01d6\3\2\2\2v\u01dd\3\2\2\2x\u01e4\3\2\2\2")
        buf.write("z\u01ec\3\2\2\2|\u01ee\3\2\2\2~\177\5H%\2\177\u0080\5")
        buf.write("\4\3\2\u0080\u0081\5\b\5\2\u0081\u0082\5\n\6\2\u0082\u0083")
        buf.write("\5H%\2\u0083\u0084\7\2\2\3\u0084\3\3\2\2\2\u0085\u0086")
        buf.write("\5\6\4\2\u0086\u0087\5H%\2\u0087\u0088\5\4\3\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0085\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\5\3\2\2\2\u008c\u008f\5\60\31\2\u008d")
        buf.write("\u008f\58\35\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\7\3\2\2\2\u0090\u0091\7\17\2\2\u0091\u0092\7\3")
        buf.write("\2\2\u0092\u0093\7\35\2\2\u0093\u0094\7\36\2\2\u0094\u0095")
        buf.write("\5H%\2\u0095\u0096\5N(\2\u0096\t\3\2\2\2\u0097\u0098\5")
        buf.write("\f\7\2\u0098\u0099\5H%\2\u0099\u009a\5\n\6\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u0097\3\2\2\2\u009c")
        buf.write("\u009b\3\2\2\2\u009d\13\3\2\2\2\u009e\u00a1\5\60\31\2")
        buf.write("\u009f\u00a1\5F$\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2")
        buf.write("\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\t\2\2\2\u00a3\17\3\2")
        buf.write("\2\2\u00a4\u00a5\t\3\2\2\u00a5\21\3\2\2\2\u00a6\u00a7")
        buf.write("\7\37\2\2\u00a7\u00a8\5\24\13\2\u00a8\u00a9\7 \2\2\u00a9")
        buf.write("\23\3\2\2\2\u00aa\u00ad\5\26\f\2\u00ab\u00ad\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\25\3\2\2\2\u00ae")
        buf.write("\u00af\5\30\r\2\u00af\u00b0\7!\2\2\u00b0\u00b1\5\26\f")
        buf.write("\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4\5\30\r\2\u00b3\u00ae")
        buf.write("\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\27\3\2\2\2\u00b5\u00b8")
        buf.write("\5\34\17\2\u00b6\u00b8\5\22\n\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\31\3\2\2\2\u00b9\u00ba\7\61\2\2\u00ba")
        buf.write("\33\3\2\2\2\u00bb\u00bc\5\36\20\2\u00bc\u00bd\7\'\2\2")
        buf.write("\u00bd\u00be\5\36\20\2\u00be\u00c1\3\2\2\2\u00bf\u00c1")
        buf.write("\5\36\20\2\u00c0\u00bb\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\35\3\2\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\t\4\2\2\u00c4")
        buf.write("\u00c5\5 \21\2\u00c5\u00c8\3\2\2\2\u00c6\u00c8\5 \21\2")
        buf.write("\u00c7\u00c2\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\37\3\2")
        buf.write("\2\2\u00c9\u00ca\b\21\1\2\u00ca\u00cb\5\"\22\2\u00cb\u00d1")
        buf.write("\3\2\2\2\u00cc\u00cd\f\4\2\2\u00cd\u00ce\t\5\2\2\u00ce")
        buf.write("\u00d0\5\"\22\2\u00cf\u00cc\3\2\2\2\u00d0\u00d3\3\2\2")
        buf.write("\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2!\3\2")
        buf.write("\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\b\22\1\2\u00d5\u00d6")
        buf.write("\5$\23\2\u00d6\u00dc\3\2\2\2\u00d7\u00d8\f\4\2\2\u00d8")
        buf.write("\u00d9\t\6\2\2\u00d9\u00db\5$\23\2\u00da\u00d7\3\2\2\2")
        buf.write("\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd#\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0")
        buf.write("\b\23\1\2\u00e0\u00e1\5&\24\2\u00e1\u00e7\3\2\2\2\u00e2")
        buf.write("\u00e3\f\4\2\2\u00e3\u00e4\t\7\2\2\u00e4\u00e6\5&\24\2")
        buf.write("\u00e5\u00e2\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3")
        buf.write("\2\2\2\u00e7\u00e8\3\2\2\2\u00e8%\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00eb\7\32\2\2\u00eb\u00ee\5&\24\2\u00ec")
        buf.write("\u00ee\5(\25\2\u00ed\u00ea\3\2\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\'\3\2\2\2\u00ef\u00f0\7*\2\2\u00f0\u00f3\5(\25")
        buf.write("\2\u00f1\u00f3\5.\30\2\u00f2\u00ef\3\2\2\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f3)\3\2\2\2\u00f4\u00f5\5\32\16\2\u00f5\u00f6")
        buf.write("\7\37\2\2\u00f6\u00f7\5,\27\2\u00f7\u00f8\7 \2\2\u00f8")
        buf.write("\u00ff\3\2\2\2\u00f9\u00fa\5t;\2\u00fa\u00fb\7\37\2\2")
        buf.write("\u00fb\u00fc\5,\27\2\u00fc\u00fd\7 \2\2\u00fd\u00ff\3")
        buf.write("\2\2\2\u00fe\u00f4\3\2\2\2\u00fe\u00f9\3\2\2\2\u00ff+")
        buf.write("\3\2\2\2\u0100\u0101\5\34\17\2\u0101\u0102\7!\2\2\u0102")
        buf.write("\u0103\5,\27\2\u0103\u0106\3\2\2\2\u0104\u0106\5\34\17")
        buf.write("\2\u0105\u0100\3\2\2\2\u0105\u0104\3\2\2\2\u0106-\3\2")
        buf.write("\2\2\u0107\u0110\5\20\t\2\u0108\u0110\5\32\16\2\u0109")
        buf.write("\u0110\5*\26\2\u010a\u0110\5t;\2\u010b\u010c\7\35\2\2")
        buf.write("\u010c\u010d\5\34\17\2\u010d\u010e\7\36\2\2\u010e\u0110")
        buf.write("\3\2\2\2\u010f\u0107\3\2\2\2\u010f\u0108\3\2\2\2\u010f")
        buf.write("\u0109\3\2\2\2\u010f\u010a\3\2\2\2\u010f\u010b\3\2\2\2")
        buf.write("\u0110/\3\2\2\2\u0111\u0114\5\62\32\2\u0112\u0114\5\64")
        buf.write("\33\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\61")
        buf.write("\3\2\2\2\u0115\u0116\5\16\b\2\u0116\u0117\5\32\16\2\u0117")
        buf.write("\u0128\3\2\2\2\u0118\u0119\5\16\b\2\u0119\u011a\5\32\16")
        buf.write("\2\u011a\u011b\7#\2\2\u011b\u011c\5\34\17\2\u011c\u0128")
        buf.write("\3\2\2\2\u011d\u011e\7\r\2\2\u011e\u011f\5\32\16\2\u011f")
        buf.write("\u0120\7#\2\2\u0120\u0121\5\34\17\2\u0121\u0128\3\2\2")
        buf.write("\2\u0122\u0123\7\16\2\2\u0123\u0124\5\32\16\2\u0124\u0125")
        buf.write("\7#\2\2\u0125\u0126\5\34\17\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0115\3\2\2\2\u0127\u0118\3\2\2\2\u0127\u011d\3\2\2\2")
        buf.write("\u0127\u0122\3\2\2\2\u0128\63\3\2\2\2\u0129\u012a\5\16")
        buf.write("\b\2\u012a\u012b\5\32\16\2\u012b\u012c\7\37\2\2\u012c")
        buf.write("\u012d\5\66\34\2\u012d\u012e\7 \2\2\u012e\u0138\3\2\2")
        buf.write("\2\u012f\u0130\5\16\b\2\u0130\u0131\5\32\16\2\u0131\u0132")
        buf.write("\7\37\2\2\u0132\u0133\5\66\34\2\u0133\u0134\7 \2\2\u0134")
        buf.write("\u0135\7#\2\2\u0135\u0136\5\22\n\2\u0136\u0138\3\2\2\2")
        buf.write("\u0137\u0129\3\2\2\2\u0137\u012f\3\2\2\2\u0138\65\3\2")
        buf.write("\2\2\u0139\u013a\7\4\2\2\u013a\u013b\7!\2\2\u013b\u013e")
        buf.write("\5\66\34\2\u013c\u013e\7\4\2\2\u013d\u0139\3\2\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\67\3\2\2\2\u013f\u0142\5:\36\2\u0140")
        buf.write("\u0142\5F$\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("9\3\2\2\2\u0143\u0144\7\17\2\2\u0144\u0145\5\32\16\2\u0145")
        buf.write("\u0146\7\35\2\2\u0146\u0147\5<\37\2\u0147\u0148\7\36\2")
        buf.write("\2\u0148\u0149\5L\'\2\u0149;\3\2\2\2\u014a\u014d\5> \2")
        buf.write("\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b\3")
        buf.write("\2\2\2\u014d=\3\2\2\2\u014e\u014f\5@!\2\u014f\u0150\7")
        buf.write("!\2\2\u0150\u0151\5> \2\u0151\u0154\3\2\2\2\u0152\u0154")
        buf.write("\5@!\2\u0153\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154?")
        buf.write("\3\2\2\2\u0155\u0158\5B\"\2\u0156\u0158\5D#\2\u0157\u0155")
        buf.write("\3\2\2\2\u0157\u0156\3\2\2\2\u0158A\3\2\2\2\u0159\u015a")
        buf.write("\5\16\b\2\u015a\u015b\5\32\16\2\u015bC\3\2\2\2\u015c\u015d")
        buf.write("\5\16\b\2\u015d\u015e\5\32\16\2\u015e\u015f\7\37\2\2\u015f")
        buf.write("\u0160\5\66\34\2\u0160\u0161\7 \2\2\u0161E\3\2\2\2\u0162")
        buf.write("\u0163\7\17\2\2\u0163\u0164\5\32\16\2\u0164\u0165\7\35")
        buf.write("\2\2\u0165\u0166\5<\37\2\u0166\u0167\7\36\2\2\u0167\u0168")
        buf.write("\5H%\2\u0168\u0169\5N(\2\u0169G\3\2\2\2\u016a\u016d\5")
        buf.write("J&\2\u016b\u016d\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016dI\3\2\2\2\u016e\u016f\7\"\2\2\u016f\u0172")
        buf.write("\5J&\2\u0170\u0172\7\"\2\2\u0171\u016e\3\2\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172K\3\2\2\2\u0173\u0174\7\"\2\2\u0174M\3\2")
        buf.write("\2\2\u0175\u0178\5p9\2\u0176\u0178\5|?\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0176\3\2\2\2\u0178O\3\2\2\2\u0179\u017a")
        buf.write("\5R*\2\u017a\u017b\5H%\2\u017b\u017c\5P)\2\u017c\u017f")
        buf.write("\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u0179\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017fQ\3\2\2\2\u0180\u0183\5^\60\2\u0181")
        buf.write("\u0183\5T+\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("S\3\2\2\2\u0184\u0187\5V,\2\u0185\u0187\5X-\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0185\3\2\2\2\u0187U\3\2\2\2\u0188\u018f")
        buf.write("\5\60\31\2\u0189\u018f\5Z.\2\u018a\u018f\5l\67\2\u018b")
        buf.write("\u018f\5n8\2\u018c\u018f\5p9\2\u018d\u018f\5r:\2\u018e")
        buf.write("\u0188\3\2\2\2\u018e\u0189\3\2\2\2\u018e\u018a\3\2\2\2")
        buf.write("\u018e\u018b\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3")
        buf.write("\2\2\2\u018fW\3\2\2\2\u0190\u0193\5j\66\2\u0191\u0193")
        buf.write("\5|?\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193Y")
        buf.write("\3\2\2\2\u0194\u0195\5\\/\2\u0195\u0196\7#\2\2\u0196\u0197")
        buf.write("\5\34\17\2\u0197\u0198\5L\'\2\u0198[\3\2\2\2\u0199\u019c")
        buf.write("\5\32\16\2\u019a\u019c\5*\26\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c]\3\2\2\2\u019d\u019e\5`\61\2\u019e")
        buf.write("\u019f\5b\62\2\u019f\u01a0\5f\64\2\u01a0_\3\2\2\2\u01a1")
        buf.write("\u01a2\7\25\2\2\u01a2\u01a3\5h\65\2\u01a3\u01a4\5H%\2")
        buf.write("\u01a4\u01a5\5R*\2\u01a5a\3\2\2\2\u01a6\u01a7\5d\63\2")
        buf.write("\u01a7\u01a8\5b\62\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\3")
        buf.write("\2\2\2\u01aa\u01a6\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abc")
        buf.write("\3\2\2\2\u01ac\u01ad\7\27\2\2\u01ad\u01ae\5h\65\2\u01ae")
        buf.write("\u01af\5H%\2\u01af\u01b0\5R*\2\u01b0e\3\2\2\2\u01b1\u01b2")
        buf.write("\7\26\2\2\u01b2\u01b3\5H%\2\u01b3\u01b4\5R*\2\u01b4\u01b7")
        buf.write("\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7g\3\2\2\2\u01b8\u01b9\7\35\2\2\u01b9")
        buf.write("\u01ba\5\34\17\2\u01ba\u01bb\7\36\2\2\u01bbi\3\2\2\2\u01bc")
        buf.write("\u01bd\7\20\2\2\u01bd\u01be\5\32\16\2\u01be\u01bf\7\21")
        buf.write("\2\2\u01bf\u01c0\5\34\17\2\u01c0\u01c1\7\22\2\2\u01c1")
        buf.write("\u01c2\5\34\17\2\u01c2\u01c3\5H%\2\u01c3\u01c4\5R*\2\u01c4")
        buf.write("k\3\2\2\2\u01c5\u01c6\7\23\2\2\u01c6\u01c7\5L\'\2\u01c7")
        buf.write("m\3\2\2\2\u01c8\u01c9\7\24\2\2\u01c9\u01ca\5L\'\2\u01ca")
        buf.write("o\3\2\2\2\u01cb\u01cc\7\f\2\2\u01cc\u01cd\5\34\17\2\u01cd")
        buf.write("\u01ce\5L\'\2\u01ce\u01d2\3\2\2\2\u01cf\u01d0\7\f\2\2")
        buf.write("\u01d0\u01d2\5L\'\2\u01d1\u01cb\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2q\3\2\2\2\u01d3\u01d4\5t;\2\u01d4\u01d5\5")
        buf.write("L\'\2\u01d5s\3\2\2\2\u01d6\u01d7\5\32\16\2\u01d7\u01d8")
        buf.write("\7\35\2\2\u01d8\u01d9\5v<\2\u01d9\u01da\7\36\2\2\u01da")
        buf.write("u\3\2\2\2\u01db\u01de\5x=\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01dew\3\2\2\2\u01df")
        buf.write("\u01e0\5z>\2\u01e0\u01e1\7!\2\2\u01e1\u01e2\5x=\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e5\5z>\2\u01e4\u01df\3\2\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5y\3\2\2\2\u01e6\u01ed\5\34\17\2\u01e7")
        buf.write("\u01e8\5\32\16\2\u01e8\u01e9\7\37\2\2\u01e9\u01ea\5\66")
        buf.write("\34\2\u01ea\u01eb\7 \2\2\u01eb\u01ed\3\2\2\2\u01ec\u01e6")
        buf.write("\3\2\2\2\u01ec\u01e7\3\2\2\2\u01ed{\3\2\2\2\u01ee\u01ef")
        buf.write("\7\30\2\2\u01ef\u01f0\5J&\2\u01f0\u01f1\5P)\2\u01f1\u01f2")
        buf.write("\7\31\2\2\u01f2\u01f3\5J&\2\u01f3}\3\2\2\2*\u008a\u008e")
        buf.write("\u009c\u00a0\u00ac\u00b3\u00b7\u00c0\u00c7\u00d1\u00dc")
        buf.write("\u00e7\u00ed\u00f2\u00fe\u0105\u010f\u0113\u0127\u0137")
        buf.write("\u013d\u0141\u014c\u0153\u0157\u016c\u0171\u0177\u017e")
        buf.write("\u0182\u0186\u018e\u0192\u019b\u01aa\u01b6\u01d1\u01dd")
        buf.write("\u01e4\u01ec")
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
                      "COMMENT", "WHITESPACE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_pre_declaration_list = 1
    RULE_pre_declaration = 2
    RULE_main_function = 3
    RULE_post_declaration_list = 4
    RULE_post_declaration = 5
    RULE_primitive_type = 6
    RULE_primitive_literals = 7
    RULE_array_value = 8
    RULE_array_literal_list = 9
    RULE_array_literal_prime = 10
    RULE_array_literal = 11
    RULE_identifier = 12
    RULE_expression = 13
    RULE_relational_expr = 14
    RULE_logical_expr1 = 15
    RULE_numeric_expr1 = 16
    RULE_numeric_expr2 = 17
    RULE_logical_expr2 = 18
    RULE_numeric_expr3 = 19
    RULE_element_expr = 20
    RULE_index_op_expr = 21
    RULE_term = 22
    RULE_variable_declaration = 23
    RULE_primitive_type_declaration = 24
    RULE_array_type_declaration = 25
    RULE_number_literal_list = 26
    RULE_function_declaration = 27
    RULE_function_prototype_declaration = 28
    RULE_parameter_list = 29
    RULE_parameter_prime = 30
    RULE_parameter = 31
    RULE_primitive_parameter = 32
    RULE_array_parameter = 33
    RULE_function_full_declaration = 34
    RULE_nullable_newline_list = 35
    RULE_newline_list = 36
    RULE_newline = 37
    RULE_function_body = 38
    RULE_statement_list = 39
    RULE_statement = 40
    RULE_non_if_statement = 41
    RULE_simple_statement = 42
    RULE_compound_statement = 43
    RULE_assignment_statement = 44
    RULE_assignee = 45
    RULE_if_statement = 46
    RULE_if_clause = 47
    RULE_elif_clause_list = 48
    RULE_elif_clause = 49
    RULE_else_clause = 50
    RULE_conditional_expr = 51
    RULE_for_statement = 52
    RULE_break_statement = 53
    RULE_continue_statement = 54
    RULE_return_statement = 55
    RULE_function_call_statement = 56
    RULE_function_call = 57
    RULE_argument_list = 58
    RULE_argument_prime = 59
    RULE_argument = 60
    RULE_block_statement = 61

    ruleNames =  [ "program", "pre_declaration_list", "pre_declaration", 
                   "main_function", "post_declaration_list", "post_declaration", 
                   "primitive_type", "primitive_literals", "array_value", 
                   "array_literal_list", "array_literal_prime", "array_literal", 
                   "identifier", "expression", "relational_expr", "logical_expr1", 
                   "numeric_expr1", "numeric_expr2", "logical_expr2", "numeric_expr3", 
                   "element_expr", "index_op_expr", "term", "variable_declaration", 
                   "primitive_type_declaration", "array_type_declaration", 
                   "number_literal_list", "function_declaration", "function_prototype_declaration", 
                   "parameter_list", "parameter_prime", "parameter", "primitive_parameter", 
                   "array_parameter", "function_full_declaration", "nullable_newline_list", 
                   "newline_list", "newline", "function_body", "statement_list", 
                   "statement", "non_if_statement", "simple_statement", 
                   "compound_statement", "assignment_statement", "assignee", 
                   "if_statement", "if_clause", "elif_clause_list", "elif_clause", 
                   "else_clause", "conditional_expr", "for_statement", "break_statement", 
                   "continue_statement", "return_statement", "function_call_statement", 
                   "function_call", "argument_list", "argument_prime", "argument", 
                   "block_statement" ]

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
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
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

        def nullable_newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Nullable_newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,i)


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
            self.state = 124
            self.nullable_newline_list()
            self.state = 125
            self.pre_declaration_list()
            self.state = 126
            self.main_function()
            self.state = 127
            self.post_declaration_list()
            self.state = 128
            self.nullable_newline_list()
            self.state = 129
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

        def pre_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def pre_declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Pre_declaration_listContext,0)


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
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.pre_declaration()
                self.state = 132
                self.nullable_newline_list()
                self.state = 133
                self.pre_declaration_list()
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
        self.enterRule(localctx, 4, self.RULE_pre_declaration)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function" ):
                return visitor.visitMain_function(self)
            else:
                return visitor.visitChildren(self)




    def main_function(self):

        localctx = ZCodeParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(ZCodeParser.FUNC)
            self.state = 143
            self.match(ZCodeParser.T__0)
            self.state = 144
            self.match(ZCodeParser.LPAREN)
            self.state = 145
            self.match(ZCodeParser.RPAREN)
            self.state = 146
            self.nullable_newline_list()
            self.state = 147
            self.function_body()
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

        def post_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declarationContext,0)


        def nullable_newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newline_listContext,0)


        def post_declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Post_declaration_listContext,0)


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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.post_declaration()
                self.state = 150
                self.nullable_newline_list()
                self.state = 151
                self.post_declaration_list()
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
        self.enterRule(localctx, 10, self.RULE_post_declaration)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
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
        self.enterRule(localctx, 12, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
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
        self.enterRule(localctx, 14, self.RULE_primitive_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
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
        self.enterRule(localctx, 16, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZCodeParser.LBRACKET)
            self.state = 165
            self.array_literal_list()
            self.state = 166
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
        self.enterRule(localctx, 18, self.RULE_array_literal_list)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACKET, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
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
        self.enterRule(localctx, 20, self.RULE_array_literal_prime)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.array_literal()
                self.state = 173
                self.match(ZCodeParser.COMMA)
                self.state = 174
                self.array_literal_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
        self.enterRule(localctx, 22, self.RULE_array_literal)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.expression()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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
        self.enterRule(localctx, 24, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
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
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.relational_expr()
                self.state = 186
                self.match(ZCodeParser.CONCAT)
                self.state = 187
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
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
        self.enterRule(localctx, 28, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.logical_expr1(0)
                self.state = 193
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NEQ) | (1 << ZCodeParser.GTEQ) | (1 << ZCodeParser.LTEQ) | (1 << ZCodeParser.STRING_EQ) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.NUMBER_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.logical_expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_logical_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.numeric_expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr1)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 203
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.numeric_expr1(0) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_numeric_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.numeric_expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr1)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.numeric_expr2(0) 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_numeric_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.logical_expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Numeric_expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_numeric_expr2)
                    self.state = 224
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 225
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 226
                    self.logical_expr2() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_logical_expr2)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(ZCodeParser.NOT)
                self.state = 233
                self.logical_expr2()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
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
        self.enterRule(localctx, 38, self.RULE_numeric_expr3)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.MINUS)
                self.state = 238
                self.numeric_expr3()
                pass
            elif token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
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

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = ZCodeParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_element_expr)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.identifier()
                self.state = 243
                self.match(ZCodeParser.LBRACKET)
                self.state = 244
                self.index_op_expr()
                self.state = 245
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.function_call()
                self.state = 248
                self.match(ZCodeParser.LBRACKET)
                self.state = 249
                self.index_op_expr()
                self.state = 250
                self.match(ZCodeParser.RBRACKET)
                pass


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
        self.enterRule(localctx, 42, self.RULE_index_op_expr)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.expression()
                self.state = 255
                self.match(ZCodeParser.COMMA)
                self.state = 256
                self.index_op_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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
        self.enterRule(localctx, 44, self.RULE_term)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.primitive_literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.element_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.match(ZCodeParser.LPAREN)
                self.state = 266
                self.expression()
                self.state = 267
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
        self.enterRule(localctx, 46, self.RULE_variable_declaration)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.primitive_type_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
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
        self.enterRule(localctx, 48, self.RULE_primitive_type_declaration)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.primitive_type()
                self.state = 276
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.primitive_type()
                self.state = 279
                self.identifier()
                self.state = 280
                self.match(ZCodeParser.ASSIGN)
                self.state = 281
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(ZCodeParser.VAR)
                self.state = 284
                self.identifier()
                self.state = 285
                self.match(ZCodeParser.ASSIGN)
                self.state = 286
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.match(ZCodeParser.DYNAMIC)
                self.state = 289
                self.identifier()
                self.state = 290
                self.match(ZCodeParser.ASSIGN)
                self.state = 291
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
        self.enterRule(localctx, 50, self.RULE_array_type_declaration)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.primitive_type()
                self.state = 296
                self.identifier()
                self.state = 297
                self.match(ZCodeParser.LBRACKET)
                self.state = 298
                self.number_literal_list()
                self.state = 299
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.primitive_type()
                self.state = 302
                self.identifier()
                self.state = 303
                self.match(ZCodeParser.LBRACKET)
                self.state = 304
                self.number_literal_list()
                self.state = 305
                self.match(ZCodeParser.RBRACKET)
                self.state = 306
                self.match(ZCodeParser.ASSIGN)
                self.state = 307
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
        self.enterRule(localctx, 52, self.RULE_number_literal_list)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(ZCodeParser.NUMBER_L)
                self.state = 312
                self.match(ZCodeParser.COMMA)
                self.state = 313
                self.number_literal_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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
        self.enterRule(localctx, 54, self.RULE_function_declaration)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.function_prototype_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
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
        self.enterRule(localctx, 56, self.RULE_function_prototype_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.FUNC)
            self.state = 322
            self.identifier()
            self.state = 323
            self.match(ZCodeParser.LPAREN)
            self.state = 324
            self.parameter_list()
            self.state = 325
            self.match(ZCodeParser.RPAREN)
            self.state = 326
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
        self.enterRule(localctx, 58, self.RULE_parameter_list)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
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
        self.enterRule(localctx, 60, self.RULE_parameter_prime)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.parameter()
                self.state = 333
                self.match(ZCodeParser.COMMA)
                self.state = 334
                self.parameter_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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
        self.enterRule(localctx, 62, self.RULE_parameter)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.primitive_parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
        self.enterRule(localctx, 64, self.RULE_primitive_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.primitive_type()
            self.state = 344
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
        self.enterRule(localctx, 66, self.RULE_array_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.primitive_type()
            self.state = 347
            self.identifier()
            self.state = 348
            self.match(ZCodeParser.LBRACKET)
            self.state = 349
            self.number_literal_list()
            self.state = 350
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
        self.enterRule(localctx, 68, self.RULE_function_full_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.FUNC)
            self.state = 353
            self.identifier()
            self.state = 354
            self.match(ZCodeParser.LPAREN)
            self.state = 355
            self.parameter_list()
            self.state = 356
            self.match(ZCodeParser.RPAREN)
            self.state = 357
            self.nullable_newline_list()
            self.state = 358
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
        self.enterRule(localctx, 70, self.RULE_nullable_newline_list)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
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
        self.enterRule(localctx, 72, self.RULE_newline_list)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
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
        self.enterRule(localctx, 74, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
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
        self.enterRule(localctx, 76, self.RULE_function_body)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.return_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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
        self.enterRule(localctx, 78, self.RULE_statement_list)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.statement()
                self.state = 376
                self.nullable_newline_list()
                self.state = 377
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
        self.enterRule(localctx, 80, self.RULE_statement)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.if_statement()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
        self.enterRule(localctx, 82, self.RULE_non_if_statement)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.simple_statement()
                pass
            elif token in [ZCodeParser.FOR, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
        self.enterRule(localctx, 84, self.RULE_simple_statement)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.break_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.continue_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 394
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 395
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
        self.enterRule(localctx, 86, self.RULE_compound_statement)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.for_statement()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.assignee()
            self.state = 403
            self.match(ZCodeParser.ASSIGN)
            self.state = 404
            self.expression()
            self.state = 405
            self.newline()
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
        self.enterRule(localctx, 90, self.RULE_assignee)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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
        self.enterRule(localctx, 92, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.if_clause()
            self.state = 412
            self.elif_clause_list()
            self.state = 413
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
        self.enterRule(localctx, 94, self.RULE_if_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(ZCodeParser.IF)
            self.state = 416
            self.conditional_expr()
            self.state = 417
            self.nullable_newline_list()
            self.state = 418
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
        self.enterRule(localctx, 96, self.RULE_elif_clause_list)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.elif_clause()
                self.state = 421
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
        self.enterRule(localctx, 98, self.RULE_elif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(ZCodeParser.ELIF)
            self.state = 427
            self.conditional_expr()
            self.state = 428
            self.nullable_newline_list()
            self.state = 429
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
        self.enterRule(localctx, 100, self.RULE_else_clause)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(ZCodeParser.ELSE)
                self.state = 432
                self.nullable_newline_list()
                self.state = 433
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
        self.enterRule(localctx, 102, self.RULE_conditional_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(ZCodeParser.LPAREN)
            self.state = 439
            self.expression()
            self.state = 440
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
        self.enterRule(localctx, 104, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(ZCodeParser.FOR)
            self.state = 443
            self.identifier()
            self.state = 444
            self.match(ZCodeParser.UNTIL)
            self.state = 445
            self.expression()
            self.state = 446
            self.match(ZCodeParser.BY)
            self.state = 447
            self.expression()
            self.state = 448
            self.nullable_newline_list()
            self.state = 449
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
        self.enterRule(localctx, 106, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.BREAK)
            self.state = 452
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
        self.enterRule(localctx, 108, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(ZCodeParser.CONTINUE)
            self.state = 455
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
        self.enterRule(localctx, 110, self.RULE_return_statement)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.RETURN)
                self.state = 458
                self.expression()
                self.state = 459
                self.newline()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(ZCodeParser.RETURN)
                self.state = 462
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
        self.enterRule(localctx, 112, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.function_call()
            self.state = 466
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
        self.enterRule(localctx, 114, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.identifier()
            self.state = 469
            self.match(ZCodeParser.LPAREN)
            self.state = 470
            self.argument_list()
            self.state = 471
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
        self.enterRule(localctx, 116, self.RULE_argument_list)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_L, ZCodeParser.BOOL_L, ZCodeParser.STRING_L, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
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
        self.enterRule(localctx, 118, self.RULE_argument_prime)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.argument()
                self.state = 478
                self.match(ZCodeParser.COMMA)
                self.state = 479
                self.argument_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
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
        self.enterRule(localctx, 120, self.RULE_argument)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.identifier()
                self.state = 486
                self.match(ZCodeParser.LBRACKET)
                self.state = 487
                self.number_literal_list()
                self.state = 488
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
        self.enterRule(localctx, 122, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(ZCodeParser.BEGIN)
            self.state = 493
            self.newline_list()
            self.state = 494
            self.statement_list()
            self.state = 495
            self.match(ZCodeParser.END)
            self.state = 496
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
        self._predicates[15] = self.logical_expr1_sempred
        self._predicates[16] = self.numeric_expr1_sempred
        self._predicates[17] = self.numeric_expr2_sempred
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
         




