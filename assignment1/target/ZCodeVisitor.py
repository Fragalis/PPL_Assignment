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


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_literals.
    def visitPrimitive_literals(self, ctx:ZCodeParser.Primitive_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_list.
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_prime.
    def visitExpression_prime(self, ctx:ZCodeParser.Expression_primeContext):
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


    # Visit a parse tree produced by ZCodeParser#variable_declaration.
    def visitVariable_declaration(self, ctx:ZCodeParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type_declaration.
    def visitPrimitive_type_declaration(self, ctx:ZCodeParser.Primitive_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_type_declaration.
    def visitArray_type_declaration(self, ctx:ZCodeParser.Array_type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_literal_list.
    def visitNumber_literal_list(self, ctx:ZCodeParser.Number_literal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_prototype_declaration.
    def visitFunction_prototype_declaration(self, ctx:ZCodeParser.Function_prototype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_list.
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_prime.
    def visitParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_parameter.
    def visitPrimitive_parameter(self, ctx:ZCodeParser.Primitive_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_parameter.
    def visitArray_parameter(self, ctx:ZCodeParser.Array_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_full_declaration.
    def visitFunction_full_declaration(self, ctx:ZCodeParser.Function_full_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_body.
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_core.
    def visitStatement_core(self, ctx:ZCodeParser.Statement_coreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)



del ZCodeParser