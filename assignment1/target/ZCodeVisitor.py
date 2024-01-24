# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primary.
    def visitPrimary(self, ctx:ZCodeParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_value.
    def visitElement_value(self, ctx:ZCodeParser.Element_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_expr.
    def visitString_expr(self, ctx:ZCodeParser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr1.
    def visitLogical_expr1(self, ctx:ZCodeParser.Logical_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_expr.
    def visitAdding_expr(self, ctx:ZCodeParser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplicating_expr.
    def visitMultiplicating_expr(self, ctx:ZCodeParser.Multiplicating_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr2.
    def visitLogical_expr2(self, ctx:ZCodeParser.Logical_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op_expr.
    def visitIndex_op_expr(self, ctx:ZCodeParser.Index_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)



del ZCodeParser