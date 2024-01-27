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


    # Visit a parse tree produced by ZCodeParser#typer.
    def visitTyper(self, ctx:ZCodeParser.TyperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type.
    def visitArray_type(self, ctx:ZCodeParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_literal_list.
    def visitNumber_literal_list(self, ctx:ZCodeParser.Number_literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_literals.
    def visitPrimitive_literals(self, ctx:ZCodeParser.Primitive_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr1.
    def visitLogical_expr1(self, ctx:ZCodeParser.Logical_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numeric_expr1.
    def visitNumeric_expr1(self, ctx:ZCodeParser.Numeric_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr2.
    def visitLogical_expr2(self, ctx:ZCodeParser.Logical_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numeric_expr2.
    def visitNumeric_expr2(self, ctx:ZCodeParser.Numeric_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op_expr.
    def visitIndex_op_expr(self, ctx:ZCodeParser.Index_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        return self.visitChildren(ctx)



del ZCodeParser