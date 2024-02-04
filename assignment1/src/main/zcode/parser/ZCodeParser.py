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
        buf.write("\u01e1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4\177\n\4\3\5\3")
        buf.write("\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\5\6\u0089\n\6\3\7\3\7")
        buf.write("\5\7\u008d\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b1")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13\u00b7\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\5\r\u00bf\n\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00c6\n\16\3\17\3\17\5\17\u00ca\n\17\3\20\3\20\5\20\u00ce")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\5\23\u00db\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00e2")
        buf.write("\n\24\3\25\3\25\5\25\u00e6\n\25\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00fd\n\30\3\31\3")
        buf.write("\31\5\31\u0101\n\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0109\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\5\34\u0114\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u011b")
        buf.write("\n\35\3\36\3\36\5\36\u011f\n\36\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\5!\u0131\n!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0140\n#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\5$\u014a\n$\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\5&\u0153\n&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\5,\u0171")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u0178\n-\3.\3.\3.\3.\3.\3.\5.\u0180")
        buf.write("\n.\3/\3/\3/\3/\3/\5/\u0187\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\5\60\u018e\n\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u0196")
        buf.write("\n\61\f\61\16\61\u0199\13\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u01a1\n\62\f\62\16\62\u01a4\13\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\7\63\u01ac\n\63\f\63\16\63\u01af")
        buf.write("\13\63\3\64\3\64\3\64\5\64\u01b4\n\64\3\65\3\65\3\65\5")
        buf.write("\65\u01b9\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u01c3\n\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38")
        buf.write("\38\38\38\38\38\38\58\u01d4\n8\39\39\39\39\39\39\79\u01dc")
        buf.write("\n9\f9\169\u01df\139\39\2\6`bdp:\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnp\2\7\3\2\t\13\4\2$(*+\3\2\33\34\3\2,-")
        buf.write("\3\2.\60\2\u01da\2r\3\2\2\2\4u\3\2\2\2\6~\3\2\2\2\b\u0083")
        buf.write("\3\2\2\2\n\u0088\3\2\2\2\f\u008c\3\2\2\2\16\u009e\3\2")
        buf.write("\2\2\20\u00a0\3\2\2\2\22\u00b0\3\2\2\2\24\u00b6\3\2\2")
        buf.write("\2\26\u00b8\3\2\2\2\30\u00be\3\2\2\2\32\u00c5\3\2\2\2")
        buf.write("\34\u00c9\3\2\2\2\36\u00cd\3\2\2\2 \u00cf\3\2\2\2\"\u00d5")
        buf.write("\3\2\2\2$\u00da\3\2\2\2&\u00e1\3\2\2\2(\u00e5\3\2\2\2")
        buf.write("*\u00e7\3\2\2\2,\u00ea\3\2\2\2.\u00fc\3\2\2\2\60\u0100")
        buf.write("\3\2\2\2\62\u0108\3\2\2\2\64\u010a\3\2\2\2\66\u0113\3")
        buf.write("\2\2\28\u011a\3\2\2\2:\u011e\3\2\2\2<\u0120\3\2\2\2>\u0124")
        buf.write("\3\2\2\2@\u0130\3\2\2\2B\u0132\3\2\2\2D\u013f\3\2\2\2")
        buf.write("F\u0149\3\2\2\2H\u014b\3\2\2\2J\u0152\3\2\2\2L\u0154\3")
        buf.write("\2\2\2N\u0159\3\2\2\2P\u0162\3\2\2\2R\u0165\3\2\2\2T\u0168")
        buf.write("\3\2\2\2V\u0170\3\2\2\2X\u0177\3\2\2\2Z\u017f\3\2\2\2")
        buf.write("\\\u0186\3\2\2\2^\u018d\3\2\2\2`\u018f\3\2\2\2b\u019a")
        buf.write("\3\2\2\2d\u01a5\3\2\2\2f\u01b3\3\2\2\2h\u01b8\3\2\2\2")
        buf.write("j\u01c2\3\2\2\2l\u01c4\3\2\2\2n\u01d3\3\2\2\2p\u01d5\3")
        buf.write("\2\2\2rs\5\4\3\2st\7\2\2\3t\3\3\2\2\2uv\5\6\4\2vw\5\b")
        buf.write("\5\2wx\5.\30\2xy\5\n\6\2yz\5\6\4\2z\5\3\2\2\2{|\7\"\2")
        buf.write("\2|\177\5\6\4\2}\177\3\2\2\2~{\3\2\2\2~}\3\2\2\2\177\7")
        buf.write("\3\2\2\2\u0080\u0084\5\f\7\2\u0081\u0084\5\36\20\2\u0082")
        buf.write("\u0084\3\2\2\2\u0083\u0080\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0083\u0082\3\2\2\2\u0084\t\3\2\2\2\u0085\u0089\5\f\7")
        buf.write("\2\u0086\u0089\5\"\22\2\u0087\u0089\3\2\2\2\u0088\u0085")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\13\3\2\2\2\u008a\u008d\5\16\b\2\u008b\u008d\5\22\n\2")
        buf.write("\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\r\3\2\2")
        buf.write("\2\u008e\u008f\5\20\t\2\u008f\u0090\7\62\2\2\u0090\u009f")
        buf.write("\3\2\2\2\u0091\u0092\5\20\t\2\u0092\u0093\7\62\2\2\u0093")
        buf.write("\u0094\7#\2\2\u0094\u0095\5\\/\2\u0095\u009f\3\2\2\2\u0096")
        buf.write("\u0097\7\r\2\2\u0097\u0098\7\62\2\2\u0098\u0099\7#\2\2")
        buf.write("\u0099\u009f\5\\/\2\u009a\u009b\7\16\2\2\u009b\u009c\7")
        buf.write("\62\2\2\u009c\u009d\7#\2\2\u009d\u009f\5\\/\2\u009e\u008e")
        buf.write("\3\2\2\2\u009e\u0091\3\2\2\2\u009e\u0096\3\2\2\2\u009e")
        buf.write("\u009a\3\2\2\2\u009f\17\3\2\2\2\u00a0\u00a1\t\2\2\2\u00a1")
        buf.write("\21\3\2\2\2\u00a2\u00a3\5\20\t\2\u00a3\u00a4\7\62\2\2")
        buf.write("\u00a4\u00a5\7\37\2\2\u00a5\u00a6\5\24\13\2\u00a6\u00a7")
        buf.write("\7 \2\2\u00a7\u00b1\3\2\2\2\u00a8\u00a9\5\20\t\2\u00a9")
        buf.write("\u00aa\7\62\2\2\u00aa\u00ab\7\37\2\2\u00ab\u00ac\5\24")
        buf.write("\13\2\u00ac\u00ad\7 \2\2\u00ad\u00ae\7#\2\2\u00ae\u00af")
        buf.write("\5\26\f\2\u00af\u00b1\3\2\2\2\u00b0\u00a2\3\2\2\2\u00b0")
        buf.write("\u00a8\3\2\2\2\u00b1\23\3\2\2\2\u00b2\u00b3\7\4\2\2\u00b3")
        buf.write("\u00b4\7!\2\2\u00b4\u00b7\5\24\13\2\u00b5\u00b7\7\4\2")
        buf.write("\2\u00b6\u00b2\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\25\3")
        buf.write("\2\2\2\u00b8\u00b9\7\37\2\2\u00b9\u00ba\5\30\r\2\u00ba")
        buf.write("\u00bb\7 \2\2\u00bb\27\3\2\2\2\u00bc\u00bf\5\32\16\2\u00bd")
        buf.write("\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00bf\31\3\2\2\2\u00c0\u00c1\5\34\17\2\u00c1\u00c2\7")
        buf.write("!\2\2\u00c2\u00c3\5\32\16\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c6\5\34\17\2\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c6\33\3\2\2\2\u00c7\u00ca\5\\/\2\u00c8\u00ca\5\26")
        buf.write("\f\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\35")
        buf.write("\3\2\2\2\u00cb\u00ce\5 \21\2\u00cc\u00ce\5\"\22\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\37\3\2\2\2\u00cf")
        buf.write("\u00d0\7\17\2\2\u00d0\u00d1\7\62\2\2\u00d1\u00d2\7\35")
        buf.write("\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d4\7\36\2\2\u00d4!\3")
        buf.write("\2\2\2\u00d5\u00d6\5 \21\2\u00d6\u00d7\5\60\31\2\u00d7")
        buf.write("#\3\2\2\2\u00d8\u00db\5&\24\2\u00d9\u00db\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db%\3\2\2\2\u00dc")
        buf.write("\u00dd\5(\25\2\u00dd\u00de\7!\2\2\u00de\u00df\5&\24\2")
        buf.write("\u00df\u00e2\3\2\2\2\u00e0\u00e2\5(\25\2\u00e1\u00dc\3")
        buf.write("\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\'\3\2\2\2\u00e3\u00e6")
        buf.write("\5*\26\2\u00e4\u00e6\5,\27\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6)\3\2\2\2\u00e7\u00e8\5\20\t\2\u00e8")
        buf.write("\u00e9\7\62\2\2\u00e9+\3\2\2\2\u00ea\u00eb\5\20\t\2\u00eb")
        buf.write("\u00ec\7\62\2\2\u00ec\u00ed\7\37\2\2\u00ed\u00ee\5\24")
        buf.write("\13\2\u00ee\u00ef\7 \2\2\u00ef-\3\2\2\2\u00f0\u00f1\7")
        buf.write("\17\2\2\u00f1\u00f2\7\3\2\2\u00f2\u00f3\7\35\2\2\u00f3")
        buf.write("\u00f4\7\36\2\2\u00f4\u00f5\5\6\4\2\u00f5\u00f6\5\60\31")
        buf.write("\2\u00f6\u00fd\3\2\2\2\u00f7\u00f8\7\17\2\2\u00f8\u00f9")
        buf.write("\7\3\2\2\u00f9\u00fa\7\35\2\2\u00fa\u00fb\7\36\2\2\u00fb")
        buf.write("\u00fd\5\6\4\2\u00fc\u00f0\3\2\2\2\u00fc\u00f7\3\2\2\2")
        buf.write("\u00fd/\3\2\2\2\u00fe\u0101\5\62\32\2\u00ff\u0101\5\64")
        buf.write("\33\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\61")
        buf.write("\3\2\2\2\u0102\u0103\7\f\2\2\u0103\u0104\5\\/\2\u0104")
        buf.write("\u0105\7\"\2\2\u0105\u0109\3\2\2\2\u0106\u0107\7\f\2\2")
        buf.write("\u0107\u0109\7\"\2\2\u0108\u0102\3\2\2\2\u0108\u0106\3")
        buf.write("\2\2\2\u0109\63\3\2\2\2\u010a\u010b\7\30\2\2\u010b\u010c")
        buf.write("\5\66\34\2\u010c\u010d\58\35\2\u010d\u010e\7\31\2\2\u010e")
        buf.write("\u010f\5\66\34\2\u010f\65\3\2\2\2\u0110\u0111\7\"\2\2")
        buf.write("\u0111\u0114\5\66\34\2\u0112\u0114\7\"\2\2\u0113\u0110")
        buf.write("\3\2\2\2\u0113\u0112\3\2\2\2\u0114\67\3\2\2\2\u0115\u0116")
        buf.write("\5:\36\2\u0116\u0117\5\6\4\2\u0117\u0118\58\35\2\u0118")
        buf.write("\u011b\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u0115\3\2\2\2")
        buf.write("\u011a\u0119\3\2\2\2\u011b9\3\2\2\2\u011c\u011f\5<\37")
        buf.write("\2\u011d\u011f\5F$\2\u011e\u011c\3\2\2\2\u011e\u011d\3")
        buf.write("\2\2\2\u011f;\3\2\2\2\u0120\u0121\5> \2\u0121\u0122\5")
        buf.write("@!\2\u0122\u0123\5D#\2\u0123=\3\2\2\2\u0124\u0125\7\25")
        buf.write("\2\2\u0125\u0126\7\35\2\2\u0126\u0127\5\\/\2\u0127\u0128")
        buf.write("\7\36\2\2\u0128\u0129\5\6\4\2\u0129\u012a\5:\36\2\u012a")
        buf.write("\u012b\5\6\4\2\u012b?\3\2\2\2\u012c\u012d\5B\"\2\u012d")
        buf.write("\u012e\5@!\2\u012e\u0131\3\2\2\2\u012f\u0131\3\2\2\2\u0130")
        buf.write("\u012c\3\2\2\2\u0130\u012f\3\2\2\2\u0131A\3\2\2\2\u0132")
        buf.write("\u0133\7\27\2\2\u0133\u0134\7\35\2\2\u0134\u0135\5\\/")
        buf.write("\2\u0135\u0136\7\36\2\2\u0136\u0137\5\6\4\2\u0137\u0138")
        buf.write("\5:\36\2\u0138\u0139\5\6\4\2\u0139C\3\2\2\2\u013a\u013b")
        buf.write("\7\26\2\2\u013b\u013c\5\6\4\2\u013c\u013d\5:\36\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013a\3\2\2\2")
        buf.write("\u013f\u013e\3\2\2\2\u0140E\3\2\2\2\u0141\u014a\5\f\7")
        buf.write("\2\u0142\u014a\5H%\2\u0143\u014a\5N(\2\u0144\u014a\5P")
        buf.write(")\2\u0145\u014a\5R*\2\u0146\u014a\5\62\32\2\u0147\u014a")
        buf.write("\5T+\2\u0148\u014a\5\64\33\2\u0149\u0141\3\2\2\2\u0149")
        buf.write("\u0142\3\2\2\2\u0149\u0143\3\2\2\2\u0149\u0144\3\2\2\2")
        buf.write("\u0149\u0145\3\2\2\2\u0149\u0146\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u0149\u0148\3\2\2\2\u014aG\3\2\2\2\u014b\u014c")
        buf.write("\5J&\2\u014c\u014d\7#\2\2\u014d\u014e\5\\/\2\u014e\u014f")
        buf.write("\7\"\2\2\u014fI\3\2\2\2\u0150\u0153\7\62\2\2\u0151\u0153")
        buf.write("\5L\'\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("K\3\2\2\2\u0154\u0155\7\62\2\2\u0155\u0156\7\37\2\2\u0156")
        buf.write("\u0157\7\4\2\2\u0157\u0158\7 \2\2\u0158M\3\2\2\2\u0159")
        buf.write("\u015a\7\20\2\2\u015a\u015b\7\62\2\2\u015b\u015c\7\21")
        buf.write("\2\2\u015c\u015d\5\\/\2\u015d\u015e\7\22\2\2\u015e\u015f")
        buf.write("\5\\/\2\u015f\u0160\5\6\4\2\u0160\u0161\5:\36\2\u0161")
        buf.write("O\3\2\2\2\u0162\u0163\7\23\2\2\u0163\u0164\7\"\2\2\u0164")
        buf.write("Q\3\2\2\2\u0165\u0166\7\24\2\2\u0166\u0167\7\"\2\2\u0167")
        buf.write("S\3\2\2\2\u0168\u0169\7\62\2\2\u0169\u016a\7\35\2\2\u016a")
        buf.write("\u016b\5V,\2\u016b\u016c\7\36\2\2\u016c\u016d\7\"\2\2")
        buf.write("\u016dU\3\2\2\2\u016e\u0171\5X-\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171W\3\2\2")
        buf.write("\2\u0172\u0173\5Z.\2\u0173\u0174\7!\2\2\u0174\u0175\5")
        buf.write("X-\2\u0175\u0178\3\2\2\2\u0176\u0178\5Z.\2\u0177\u0172")
        buf.write("\3\2\2\2\u0177\u0176\3\2\2\2\u0178Y\3\2\2\2\u0179\u017a")
        buf.write("\7\62\2\2\u017a\u017b\7\37\2\2\u017b\u017c\5\24\13\2\u017c")
        buf.write("\u017d\7 \2\2\u017d\u0180\3\2\2\2\u017e\u0180\5\\/\2\u017f")
        buf.write("\u0179\3\2\2\2\u017f\u017e\3\2\2\2\u0180[\3\2\2\2\u0181")
        buf.write("\u0182\5^\60\2\u0182\u0183\7)\2\2\u0183\u0184\5^\60\2")
        buf.write("\u0184\u0187\3\2\2\2\u0185\u0187\5^\60\2\u0186\u0181\3")
        buf.write("\2\2\2\u0186\u0185\3\2\2\2\u0187]\3\2\2\2\u0188\u0189")
        buf.write("\5`\61\2\u0189\u018a\t\3\2\2\u018a\u018b\5`\61\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018e\5`\61\2\u018d\u0188\3\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e_\3\2\2\2\u018f\u0190\b\61\1")
        buf.write("\2\u0190\u0191\5b\62\2\u0191\u0197\3\2\2\2\u0192\u0193")
        buf.write("\f\4\2\2\u0193\u0194\t\4\2\2\u0194\u0196\5b\62\2\u0195")
        buf.write("\u0192\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198a\3\2\2\2\u0199\u0197\3\2\2")
        buf.write("\2\u019a\u019b\b\62\1\2\u019b\u019c\5d\63\2\u019c\u01a2")
        buf.write("\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f\t\5\2\2\u019f")
        buf.write("\u01a1\5d\63\2\u01a0\u019d\3\2\2\2\u01a1\u01a4\3\2\2\2")
        buf.write("\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3c\3\2\2")
        buf.write("\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\b\63\1\2\u01a6\u01a7")
        buf.write("\5f\64\2\u01a7\u01ad\3\2\2\2\u01a8\u01a9\f\4\2\2\u01a9")
        buf.write("\u01aa\t\6\2\2\u01aa\u01ac\5f\64\2\u01ab\u01a8\3\2\2\2")
        buf.write("\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01aee\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1")
        buf.write("\7\32\2\2\u01b1\u01b4\5f\64\2\u01b2\u01b4\5h\65\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4g\3\2\2\2\u01b5")
        buf.write("\u01b6\7-\2\2\u01b6\u01b9\5h\65\2\u01b7\u01b9\5j\66\2")
        buf.write("\u01b8\u01b5\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9i\3\2\2")
        buf.write("\2\u01ba\u01c3\7\4\2\2\u01bb\u01c3\7\62\2\2\u01bc\u01c3")
        buf.write("\5l\67\2\u01bd\u01c3\5n8\2\u01be\u01bf\7\35\2\2\u01bf")
        buf.write("\u01c0\5\\/\2\u01c0\u01c1\7\36\2\2\u01c1\u01c3\3\2\2\2")
        buf.write("\u01c2\u01ba\3\2\2\2\u01c2\u01bb\3\2\2\2\u01c2\u01bc\3")
        buf.write("\2\2\2\u01c2\u01bd\3\2\2\2\u01c2\u01be\3\2\2\2\u01c3k")
        buf.write("\3\2\2\2\u01c4\u01c5\7\62\2\2\u01c5\u01c6\7\35\2\2\u01c6")
        buf.write("\u01c7\5V,\2\u01c7\u01c8\7\36\2\2\u01c8m\3\2\2\2\u01c9")
        buf.write("\u01ca\7\62\2\2\u01ca\u01cb\7\35\2\2\u01cb\u01cc\5p9\2")
        buf.write("\u01cc\u01cd\7\36\2\2\u01cd\u01d4\3\2\2\2\u01ce\u01cf")
        buf.write("\5l\67\2\u01cf\u01d0\7\37\2\2\u01d0\u01d1\5p9\2\u01d1")
        buf.write("\u01d2\7\36\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01c9\3\2\2")
        buf.write("\2\u01d3\u01ce\3\2\2\2\u01d4o\3\2\2\2\u01d5\u01d6\b9\1")
        buf.write("\2\u01d6\u01d7\5\\/\2\u01d7\u01dd\3\2\2\2\u01d8\u01d9")
        buf.write("\f\4\2\2\u01d9\u01da\7!\2\2\u01da\u01dc\5\\/\2\u01db\u01d8")
        buf.write("\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01deq\3\2\2\2\u01df\u01dd\3\2\2\2\'~\u0083")
        buf.write("\u0088\u008c\u009e\u00b0\u00b6\u00be\u00c5\u00c9\u00cd")
        buf.write("\u00da\u00e1\u00e5\u00fc\u0100\u0108\u0113\u011a\u011e")
        buf.write("\u0130\u013f\u0149\u0152\u0170\u0177\u017f\u0186\u018d")
        buf.write("\u0197\u01a2\u01ad\u01b3\u01b8\u01c2\u01d3\u01dd")
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
                     "'else'", "'elif'", "'begin'", "'end'", "'not'", "'or'", 
                     "'and'", "'('", "')'", "'['", "']'", "','", "'\n'", 
                     "'<-'", "'!='", "'>='", "'<='", "'>'", "'<'", "'...'", 
                     "'=='", "'='", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "NUMBERLIT", "BOOLLIT", 
                      "STRINGLIT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "OR", "AND", "LEFT_PAR", "RIGHT_PAR", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "NEWLN", 
                      "ASSIGN", "NOTEQ", "GRATER_EQ", "LESS_EQ", "GRATER", 
                      "LESS", "STR_CONCAT", "STR_EQ", "EQ", "NUM_ADD", "NUM_SUB", 
                      "NUM_MUL", "NUM_DIV", "NUM_REMAINDER", "COMMENT", 
                      "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_structure = 1
    RULE_newlinelist = 2
    RULE_predeclist = 3
    RULE_postdeclist = 4
    RULE_vardecl = 5
    RULE_keywords_decl = 6
    RULE_typename = 7
    RULE_arraydecl = 8
    RULE_numberlit_list = 9
    RULE_arrpass_value = 10
    RULE_arrvalue_list = 11
    RULE_arrvalueprime = 12
    RULE_arrvalue = 13
    RULE_funcdecl = 14
    RULE_prototypedecl = 15
    RULE_completed_funcdecl = 16
    RULE_paramlist = 17
    RULE_paramprime = 18
    RULE_parameter = 19
    RULE_typeparamdecl = 20
    RULE_arrparramdecl = 21
    RULE_main_func = 22
    RULE_body = 23
    RULE_returnstmt = 24
    RULE_blockstmt = 25
    RULE_nonempt_newlnlist = 26
    RULE_stmtlist = 27
    RULE_stmt = 28
    RULE_ifstmt = 29
    RULE_ifclause = 30
    RULE_eliflist = 31
    RULE_elifclause = 32
    RULE_elseclause = 33
    RULE_otherstmt = 34
    RULE_assignstmt = 35
    RULE_lhs = 36
    RULE_arrelement = 37
    RULE_forstmt = 38
    RULE_breakstmt = 39
    RULE_contstmt = 40
    RULE_funcallstmt = 41
    RULE_argumentlist = 42
    RULE_argprime = 43
    RULE_argument = 44
    RULE_expression = 45
    RULE_stringop = 46
    RULE_relationalop = 47
    RULE_logicalop = 48
    RULE_addop = 49
    RULE_mulop = 50
    RULE_logicalop1 = 51
    RULE_signop = 52
    RULE_functioncall = 53
    RULE_element_expression = 54
    RULE_indexop = 55

    ruleNames =  [ "program", "structure", "newlinelist", "predeclist", 
                   "postdeclist", "vardecl", "keywords_decl", "typename", 
                   "arraydecl", "numberlit_list", "arrpass_value", "arrvalue_list", 
                   "arrvalueprime", "arrvalue", "funcdecl", "prototypedecl", 
                   "completed_funcdecl", "paramlist", "paramprime", "parameter", 
                   "typeparamdecl", "arrparramdecl", "main_func", "body", 
                   "returnstmt", "blockstmt", "nonempt_newlnlist", "stmtlist", 
                   "stmt", "ifstmt", "ifclause", "eliflist", "elifclause", 
                   "elseclause", "otherstmt", "assignstmt", "lhs", "arrelement", 
                   "forstmt", "breakstmt", "contstmt", "funcallstmt", "argumentlist", 
                   "argprime", "argument", "expression", "stringop", "relationalop", 
                   "logicalop", "addop", "mulop", "logicalop1", "signop", 
                   "functioncall", "element_expression", "indexop" ]

    EOF = Token.EOF
    T__0=1
    NUMBERLIT=2
    BOOLLIT=3
    STRINGLIT=4
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
    OR=25
    AND=26
    LEFT_PAR=27
    RIGHT_PAR=28
    LEFT_BRACKET=29
    RIGHT_BRACKET=30
    COMMA=31
    NEWLN=32
    ASSIGN=33
    NOTEQ=34
    GRATER_EQ=35
    LESS_EQ=36
    GRATER=37
    LESS=38
    STR_CONCAT=39
    STR_EQ=40
    EQ=41
    NUM_ADD=42
    NUM_SUB=43
    NUM_MUL=44
    NUM_DIV=45
    NUM_REMAINDER=46
    COMMENT=47
    IDENTIFIER=48
    WS=49
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

        def structure(self):
            return self.getTypedRuleContext(ZCodeParser.StructureContext,0)


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
            self.state = 112
            self.structure()
            self.state = 113
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def predeclist(self):
            return self.getTypedRuleContext(ZCodeParser.PredeclistContext,0)


        def main_func(self):
            return self.getTypedRuleContext(ZCodeParser.Main_funcContext,0)


        def postdeclist(self):
            return self.getTypedRuleContext(ZCodeParser.PostdeclistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_structure

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructure" ):
                return visitor.visitStructure(self)
            else:
                return visitor.visitChildren(self)




    def structure(self):

        localctx = ZCodeParser.StructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.newlinelist()
            self.state = 116
            self.predeclist()
            self.state = 117
            self.main_func()
            self.state = 118
            self.postdeclist()
            self.state = 119
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlinelist" ):
                return visitor.visitNewlinelist(self)
            else:
                return visitor.visitChildren(self)




    def newlinelist(self):

        localctx = ZCodeParser.NewlinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newlinelist)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(ZCodeParser.NEWLN)
                self.state = 122
                self.newlinelist()
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


    class PredeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_predeclist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredeclist" ):
                return visitor.visitPredeclist(self)
            else:
                return visitor.visitChildren(self)




    def predeclist(self):

        localctx = ZCodeParser.PredeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_predeclist)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.funcdecl()
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


    class PostdeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def completed_funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.Completed_funcdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_postdeclist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostdeclist" ):
                return visitor.visitPostdeclist(self)
            else:
                return visitor.visitChildren(self)




    def postdeclist(self):

        localctx = ZCodeParser.PostdeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_postdeclist)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.completed_funcdecl()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLN]:
                self.enterOuterAlt(localctx, 3)

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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keywords_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Keywords_declContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.keywords_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.arraydecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keywords_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(ZCodeParser.TypenameContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_keywords_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywords_decl" ):
                return visitor.visitKeywords_decl(self)
            else:
                return visitor.visitChildren(self)




    def keywords_decl(self):

        localctx = ZCodeParser.Keywords_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keywords_decl)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.typename()
                self.state = 141
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.typename()
                self.state = 144
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 145
                self.match(ZCodeParser.ASSIGN)
                self.state = 146
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.match(ZCodeParser.VAR)
                self.state = 149
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 150
                self.match(ZCodeParser.ASSIGN)
                self.state = 151
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(ZCodeParser.DYNAMIC)
                self.state = 153
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 154
                self.match(ZCodeParser.ASSIGN)
                self.state = 155
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypenameContext(ParserRuleContext):
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
            return ZCodeParser.RULE_typename

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypename" ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = ZCodeParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typename)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(ZCodeParser.TypenameContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def numberlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numberlit_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def arrpass_value(self):
            return self.getTypedRuleContext(ZCodeParser.Arrpass_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraydecl)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.typename()
                self.state = 161
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 162
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 163
                self.numberlit_list()
                self.state = 164
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.typename()
                self.state = 167
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 168
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 169
                self.numberlit_list()
                self.state = 170
                self.match(ZCodeParser.RIGHT_BRACKET)
                self.state = 171
                self.match(ZCodeParser.ASSIGN)
                self.state = 172
                self.arrpass_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numberlit_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numberlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numberlit_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numberlit_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberlit_list" ):
                return visitor.visitNumberlit_list(self)
            else:
                return visitor.visitChildren(self)




    def numberlit_list(self):

        localctx = ZCodeParser.Numberlit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numberlit_list)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 177
                self.match(ZCodeParser.COMMA)
                self.state = 178
                self.numberlit_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrpass_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def arrvalue_list(self):
            return self.getTypedRuleContext(ZCodeParser.Arrvalue_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrpass_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrpass_value" ):
                return visitor.visitArrpass_value(self)
            else:
                return visitor.visitChildren(self)




    def arrpass_value(self):

        localctx = ZCodeParser.Arrpass_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrpass_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 183
            self.arrvalue_list()
            self.state = 184
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrvalue_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrvalueprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrvalueprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrvalue_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrvalue_list" ):
                return visitor.visitArrvalue_list(self)
            else:
                return visitor.visitChildren(self)




    def arrvalue_list(self):

        localctx = ZCodeParser.Arrvalue_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrvalue_list)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT, ZCodeParser.NOT, ZCodeParser.LEFT_PAR, ZCodeParser.LEFT_BRACKET, ZCodeParser.NUM_SUB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.arrvalueprime()
                pass
            elif token in [ZCodeParser.RIGHT_BRACKET]:
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


    class ArrvalueprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrvalue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrvalueContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrvalueprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArrvalueprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrvalueprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrvalueprime" ):
                return visitor.visitArrvalueprime(self)
            else:
                return visitor.visitChildren(self)




    def arrvalueprime(self):

        localctx = ZCodeParser.ArrvalueprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrvalueprime)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.arrvalue()
                self.state = 191
                self.match(ZCodeParser.COMMA)
                self.state = 192
                self.arrvalueprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.arrvalue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def arrpass_value(self):
            return self.getTypedRuleContext(ZCodeParser.Arrpass_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrvalue" ):
                return visitor.visitArrvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrvalue(self):

        localctx = ZCodeParser.ArrvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrvalue)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT, ZCodeParser.NOT, ZCodeParser.LEFT_PAR, ZCodeParser.NUM_SUB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.expression()
                pass
            elif token in [ZCodeParser.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.arrpass_value()
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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototypedecl(self):
            return self.getTypedRuleContext(ZCodeParser.PrototypedeclContext,0)


        def completed_funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.Completed_funcdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcdecl)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.prototypedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.completed_funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_prototypedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototypedecl" ):
                return visitor.visitPrototypedecl(self)
            else:
                return visitor.visitChildren(self)




    def prototypedecl(self):

        localctx = ZCodeParser.PrototypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prototypedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.FUNC)
            self.state = 206
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 207
            self.match(ZCodeParser.LEFT_PAR)
            self.state = 208
            self.paramlist()
            self.state = 209
            self.match(ZCodeParser.RIGHT_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Completed_funcdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototypedecl(self):
            return self.getTypedRuleContext(ZCodeParser.PrototypedeclContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_completed_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompleted_funcdecl" ):
                return visitor.visitCompleted_funcdecl(self)
            else:
                return visitor.visitChildren(self)




    def completed_funcdecl(self):

        localctx = ZCodeParser.Completed_funcdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_completed_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.prototypedecl()
            self.state = 212
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramlist)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.paramprime()
                pass
            elif token in [ZCodeParser.RIGHT_PAR]:
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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramprime)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.parameter()
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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

        def typeparamdecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypeparamdeclContext,0)


        def arrparramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArrparramdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.typeparamdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.arrparramdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeparamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(ZCodeParser.TypenameContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typeparamdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeparamdecl" ):
                return visitor.visitTypeparamdecl(self)
            else:
                return visitor.visitChildren(self)




    def typeparamdecl(self):

        localctx = ZCodeParser.TypeparamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeparamdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.typename()
            self.state = 230
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrparramdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(ZCodeParser.TypenameContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def numberlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numberlit_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrparramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrparramdecl" ):
                return visitor.visitArrparramdecl(self)
            else:
                return visitor.visitChildren(self)




    def arrparramdecl(self):

        localctx = ZCodeParser.ArrparramdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrparramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.typename()
            self.state = 233
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 234
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 235
            self.numberlit_list()
            self.state = 236
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




    def main_func(self):

        localctx = ZCodeParser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_main_func)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(ZCodeParser.FUNC)
                self.state = 239
                self.match(ZCodeParser.T__0)
                self.state = 240
                self.match(ZCodeParser.LEFT_PAR)
                self.state = 241
                self.match(ZCodeParser.RIGHT_PAR)
                self.state = 242
                self.newlinelist()
                self.state = 243
                self.body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(ZCodeParser.FUNC)
                self.state = 246
                self.match(ZCodeParser.T__0)
                self.state = 247
                self.match(ZCodeParser.LEFT_PAR)
                self.state = 248
                self.match(ZCodeParser.RIGHT_PAR)
                self.state = 249
                self.newlinelist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_body)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.blockstmt()
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


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnstmt)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(ZCodeParser.RETURN)
                self.state = 257
                self.expression()
                self.state = 258
                self.match(ZCodeParser.NEWLN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(ZCodeParser.RETURN)
                self.state = 261
                self.match(ZCodeParser.NEWLN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def nonempt_newlnlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Nonempt_newlnlistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Nonempt_newlnlistContext,i)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.BEGIN)
            self.state = 265
            self.nonempt_newlnlist()
            self.state = 266
            self.stmtlist()
            self.state = 267
            self.match(ZCodeParser.END)
            self.state = 268
            self.nonempt_newlnlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nonempt_newlnlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def nonempt_newlnlist(self):
            return self.getTypedRuleContext(ZCodeParser.Nonempt_newlnlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nonempt_newlnlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonempt_newlnlist" ):
                return visitor.visitNonempt_newlnlist(self)
            else:
                return visitor.visitChildren(self)




    def nonempt_newlnlist(self):

        localctx = ZCodeParser.Nonempt_newlnlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_nonempt_newlnlist)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(ZCodeParser.NEWLN)
                self.state = 271
                self.nonempt_newlnlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(ZCodeParser.NEWLN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmtlist)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.stmt()
                self.state = 276
                self.newlinelist()
                self.state = 277
                self.stmtlist()
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def otherstmt(self):
            return self.getTypedRuleContext(ZCodeParser.OtherstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.ifstmt()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.otherstmt()
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


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifclause(self):
            return self.getTypedRuleContext(ZCodeParser.IfclauseContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def elseclause(self):
            return self.getTypedRuleContext(ZCodeParser.ElseclauseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.ifclause()
            self.state = 287
            self.eliflist()
            self.state = 288
            self.elseclause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfclause" ):
                return visitor.visitIfclause(self)
            else:
                return visitor.visitChildren(self)




    def ifclause(self):

        localctx = ZCodeParser.IfclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(ZCodeParser.IF)
            self.state = 291
            self.match(ZCodeParser.LEFT_PAR)
            self.state = 292
            self.expression()
            self.state = 293
            self.match(ZCodeParser.RIGHT_PAR)
            self.state = 294
            self.newlinelist()
            self.state = 295
            self.stmt()
            self.state = 296
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifclause(self):
            return self.getTypedRuleContext(ZCodeParser.ElifclauseContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_eliflist)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.elifclause()
                self.state = 299
                self.eliflist()
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


    class ElifclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def newlinelist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinelistContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,i)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifclause" ):
                return visitor.visitElifclause(self)
            else:
                return visitor.visitChildren(self)




    def elifclause(self):

        localctx = ZCodeParser.ElifclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elifclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.ELIF)
            self.state = 305
            self.match(ZCodeParser.LEFT_PAR)
            self.state = 306
            self.expression()
            self.state = 307
            self.match(ZCodeParser.RIGHT_PAR)
            self.state = 308
            self.newlinelist()
            self.state = 309
            self.stmt()
            self.state = 310
            self.newlinelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseclause" ):
                return visitor.visitElseclause(self)
            else:
                return visitor.visitChildren(self)




    def elseclause(self):

        localctx = ZCodeParser.ElseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elseclause)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(ZCodeParser.ELSE)
                self.state = 313
                self.newlinelist()
                self.state = 314
                self.stmt()
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


    class OtherstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def funcallstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_otherstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherstmt" ):
                return visitor.visitOtherstmt(self)
            else:
                return visitor.visitChildren(self)




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_otherstmt)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.contstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.returnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 325
                self.funcallstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 326
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.lhs()
            self.state = 330
            self.match(ZCodeParser.ASSIGN)
            self.state = 331
            self.expression()
            self.state = 332
            self.match(ZCodeParser.NEWLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrelement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrelementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_lhs)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.arrelement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrelement" ):
                return visitor.visitArrelement(self)
            else:
                return visitor.visitChildren(self)




    def arrelement(self):

        localctx = ZCodeParser.ArrelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arrelement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 339
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 340
            self.match(ZCodeParser.NUMBERLIT)
            self.state = 341
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newlinelist(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinelistContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.FOR)
            self.state = 344
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 345
            self.match(ZCodeParser.UNTIL)
            self.state = 346
            self.expression()
            self.state = 347
            self.match(ZCodeParser.BY)
            self.state = 348
            self.expression()
            self.state = 349
            self.newlinelist()
            self.state = 350
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.BREAK)
            self.state = 353
            self.match(ZCodeParser.NEWLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = ZCodeParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ZCodeParser.CONTINUE)
            self.state = 356
            self.match(ZCodeParser.NEWLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def NEWLN(self):
            return self.getToken(ZCodeParser.NEWLN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcallstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncallstmt" ):
                return visitor.visitFuncallstmt(self)
            else:
                return visitor.visitChildren(self)




    def funcallstmt(self):

        localctx = ZCodeParser.FuncallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_funcallstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 359
            self.match(ZCodeParser.LEFT_PAR)
            self.state = 360
            self.argumentlist()
            self.state = 361
            self.match(ZCodeParser.RIGHT_PAR)
            self.state = 362
            self.match(ZCodeParser.NEWLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argumentlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = ZCodeParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentlist)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBERLIT, ZCodeParser.NOT, ZCodeParser.LEFT_PAR, ZCodeParser.NUM_SUB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.argprime()
                pass
            elif token in [ZCodeParser.RIGHT_PAR]:
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


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = ZCodeParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argprime)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.argument()
                self.state = 369
                self.match(ZCodeParser.COMMA)
                self.state = 370
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def numberlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numberlit_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

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
        self.enterRule(localctx, 88, self.RULE_argument)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 376
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 377
                self.numberlit_list()
                self.state = 378
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.expression()
                pass


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

        def stringop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringopContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringopContext,i)


        def STR_CONCAT(self):
            return self.getToken(ZCodeParser.STR_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expression)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.stringop()
                self.state = 384
                self.match(ZCodeParser.STR_CONCAT)
                self.state = 385
                self.stringop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.stringop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.RelationalopContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.RelationalopContext,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def STR_EQ(self):
            return self.getToken(ZCodeParser.STR_EQ, 0)

        def NOTEQ(self):
            return self.getToken(ZCodeParser.NOTEQ, 0)

        def GRATER(self):
            return self.getToken(ZCodeParser.GRATER, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def GRATER_EQ(self):
            return self.getToken(ZCodeParser.GRATER_EQ, 0)

        def LESS_EQ(self):
            return self.getToken(ZCodeParser.LESS_EQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stringop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringop" ):
                return visitor.visitStringop(self)
            else:
                return visitor.visitChildren(self)




    def stringop(self):

        localctx = ZCodeParser.StringopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stringop)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.relationalop(0)
                self.state = 391
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOTEQ) | (1 << ZCodeParser.GRATER_EQ) | (1 << ZCodeParser.LESS_EQ) | (1 << ZCodeParser.GRATER) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.STR_EQ) | (1 << ZCodeParser.EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 392
                self.relationalop(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.relationalop(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalop(self):
            return self.getTypedRuleContext(ZCodeParser.LogicalopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(ZCodeParser.RelationalopContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relationalop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalop" ):
                return visitor.visitRelationalop(self)
            else:
                return visitor.visitChildren(self)



    def relationalop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.RelationalopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_relationalop, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.logicalop(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.RelationalopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalop)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.OR or _la==ZCodeParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.logicalop(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addop(self):
            return self.getTypedRuleContext(ZCodeParser.AddopContext,0)


        def logicalop(self):
            return self.getTypedRuleContext(ZCodeParser.LogicalopContext,0)


        def NUM_ADD(self):
            return self.getToken(ZCodeParser.NUM_ADD, 0)

        def NUM_SUB(self):
            return self.getToken(ZCodeParser.NUM_SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logicalop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalop" ):
                return visitor.visitLogicalop(self)
            else:
                return visitor.visitChildren(self)



    def logicalop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.LogicalopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_logicalop, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.addop(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.LogicalopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalop)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.NUM_ADD or _la==ZCodeParser.NUM_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.addop(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulop(self):
            return self.getTypedRuleContext(ZCodeParser.MulopContext,0)


        def addop(self):
            return self.getTypedRuleContext(ZCodeParser.AddopContext,0)


        def NUM_MUL(self):
            return self.getToken(ZCodeParser.NUM_MUL, 0)

        def NUM_DIV(self):
            return self.getToken(ZCodeParser.NUM_DIV, 0)

        def NUM_REMAINDER(self):
            return self.getToken(ZCodeParser.NUM_REMAINDER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_addop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddop" ):
                return visitor.visitAddop(self)
            else:
                return visitor.visitChildren(self)



    def addop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.AddopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_addop, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.mulop()
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.AddopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addop)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_MUL) | (1 << ZCodeParser.NUM_DIV) | (1 << ZCodeParser.NUM_REMAINDER))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.mulop() 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def mulop(self):
            return self.getTypedRuleContext(ZCodeParser.MulopContext,0)


        def logicalop1(self):
            return self.getTypedRuleContext(ZCodeParser.Logicalop1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_mulop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulop" ):
                return visitor.visitMulop(self)
            else:
                return visitor.visitChildren(self)




    def mulop(self):

        localctx = ZCodeParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_mulop)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(ZCodeParser.NOT)
                self.state = 431
                self.mulop()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.LEFT_PAR, ZCodeParser.NUM_SUB, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.logicalop1()
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


    class Logicalop1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_SUB(self):
            return self.getToken(ZCodeParser.NUM_SUB, 0)

        def logicalop1(self):
            return self.getTypedRuleContext(ZCodeParser.Logicalop1Context,0)


        def signop(self):
            return self.getTypedRuleContext(ZCodeParser.SignopContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logicalop1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalop1" ):
                return visitor.visitLogicalop1(self)
            else:
                return visitor.visitChildren(self)




    def logicalop1(self):

        localctx = ZCodeParser.Logicalop1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_logicalop1)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.NUM_SUB)
                self.state = 436
                self.logicalop1()
                pass
            elif token in [ZCodeParser.NUMBERLIT, ZCodeParser.LEFT_PAR, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.signop()
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


    class SignopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def functioncall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctioncallContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_signop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignop" ):
                return visitor.visitSignop(self)
            else:
                return visitor.visitChildren(self)




    def signop(self):

        localctx = ZCodeParser.SignopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_signop)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.functioncall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.element_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 444
                self.match(ZCodeParser.LEFT_PAR)
                self.state = 445
                self.expression()
                self.state = 446
                self.match(ZCodeParser.RIGHT_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArgumentlistContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functioncall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)




    def functioncall(self):

        localctx = ZCodeParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 451
            self.match(ZCodeParser.LEFT_PAR)
            self.state = 452
            self.argumentlist()
            self.state = 453
            self.match(ZCodeParser.RIGHT_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFT_PAR(self):
            return self.getToken(ZCodeParser.LEFT_PAR, 0)

        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def RIGHT_PAR(self):
            return self.getToken(ZCodeParser.RIGHT_PAR, 0)

        def functioncall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctioncallContext,0)


        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_element_expression)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 456
                self.match(ZCodeParser.LEFT_PAR)
                self.state = 457
                self.indexop(0)
                self.state = 458
                self.match(ZCodeParser.RIGHT_PAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.functioncall()
                self.state = 461
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 462
                self.indexop(0)
                self.state = 463
                self.match(ZCodeParser.RIGHT_PAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)



    def indexop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.IndexopContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_indexop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.IndexopContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_indexop)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 471
                    self.match(ZCodeParser.COMMA)
                    self.state = 472
                    self.expression() 
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[47] = self.relationalop_sempred
        self._predicates[48] = self.logicalop_sempred
        self._predicates[49] = self.addop_sempred
        self._predicates[55] = self.indexop_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relationalop_sempred(self, localctx:RelationalopContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def logicalop_sempred(self, localctx:LogicalopContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def addop_sempred(self, localctx:AddopContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def indexop_sempred(self, localctx:IndexopContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




