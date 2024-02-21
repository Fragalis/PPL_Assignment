from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

# program
# 	:	nullable_newline_list
# 		declaration_list
# 		nullable_newline_list 
# 		EOF
# 	;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
    
# declaration_list
# 	:	declaration nullable_newline_list declaration_list
# 	|	
# 	;
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        return self.visitChildren(ctx)


    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)

# primitive_type
# 	:	NUMBER
# 	|	BOOL
# 	|	STRING
# 	;
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        if ctx.NUMBER():    return NumberType()
        if ctx.BOOL():      return BoolType()
        return StringType()

# primitive_literals
# 	:	NUMBER_L
# 	|	BOOL_L
# 	|	STRING_L
# 	;
    def visitPrimitive_literals(self, ctx:ZCodeParser.Primitive_literalsContext):
        if ctx.NUMBER_L():    return NumberLiteral(ctx.NUMBER_L().getText())
        if ctx.BOOL_L():      return BooleanLiteral(ctx.BOOL_L().getText())
        return StringLiteral(ctx.STRING_L().getText())


    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    def visitArray_literal_list(self, ctx:ZCodeParser.Array_literal_listContext):
        return self.visitChildren(ctx)


    def visitArray_literal_prime(self, ctx:ZCodeParser.Array_literal_primeContext):
        return self.visitChildren(ctx)


    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)

# identifier
# 	:	IDENTIFIER
# 	;
    def visitIdentifier(self, ctx:ZCodeParser.IdentifierContext):
        return Id(ctx.IDENTIFIER().getText())


    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    def visitLogical_expr1(self, ctx:ZCodeParser.Logical_expr1Context):
        return self.visitChildren(ctx)


    def visitNumeric_expr1(self, ctx:ZCodeParser.Numeric_expr1Context):
        return self.visitChildren(ctx)


    def visitNumeric_expr2(self, ctx:ZCodeParser.Numeric_expr2Context):
        return self.visitChildren(ctx)


    def visitLogical_expr2(self, ctx:ZCodeParser.Logical_expr2Context):
        return self.visitChildren(ctx)


    def visitNumeric_expr3(self, ctx:ZCodeParser.Numeric_expr3Context):
        return self.visitChildren(ctx)


    def visitElement_expr(self, ctx:ZCodeParser.Element_exprContext):
        return self.visitChildren(ctx)


    def visitIndex_op_expr(self, ctx:ZCodeParser.Index_op_exprContext):
        return self.visitChildren(ctx)


    def visitTerm(self, ctx:ZCodeParser.TermContext):
        return self.visitChildren(ctx)


    def visitVariable_declaration(self, ctx:ZCodeParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    def visitPrimitive_type_declaration(self, ctx:ZCodeParser.Primitive_type_declarationContext):
        return self.visitChildren(ctx)


    def visitArray_type_declaration(self, ctx:ZCodeParser.Array_type_declarationContext):
        return self.visitChildren(ctx)


    def visitNumber_literal_list(self, ctx:ZCodeParser.Number_literal_listContext):
        return self.visitChildren(ctx)


    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    def visitFunction_prototype_declaration(self, ctx:ZCodeParser.Function_prototype_declarationContext):
        return self.visitChildren(ctx)


    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    def visitParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        return self.visitChildren(ctx)


    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    def visitPrimitive_parameter(self, ctx:ZCodeParser.Primitive_parameterContext):
        return self.visitChildren(ctx)


    def visitArray_parameter(self, ctx:ZCodeParser.Array_parameterContext):
        return self.visitChildren(ctx)


    def visitFunction_full_declaration(self, ctx:ZCodeParser.Function_full_declarationContext):
        return self.visitChildren(ctx)


    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)


    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    def visitNewline(self, ctx:ZCodeParser.NewlineContext):
        return self.visitChildren(ctx)


    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    def visitNon_if_statement(self, ctx:ZCodeParser.Non_if_statementContext):
        return self.visitChildren(ctx)


    def visitSimple_statement(self, ctx:ZCodeParser.Simple_statementContext):
        return self.visitChildren(ctx)


    def visitCompound_statement(self, ctx:ZCodeParser.Compound_statementContext):
        return self.visitChildren(ctx)


    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    def visitAssignee(self, ctx:ZCodeParser.AssigneeContext):
        return self.visitChildren(ctx)


    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    def visitIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        return self.visitChildren(ctx)

    def visitElif_clause_list(self, ctx:ZCodeParser.Elif_clause_listContext):
        return self.visitChildren(ctx)

    def visitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        return self.visitChildren(ctx)

    def visitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        return self.visitChildren(ctx)

    def visitConditional_expr(self, ctx:ZCodeParser.Conditional_exprContext):
        return self.visitChildren(ctx)

    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)

# break_statement
# 	:	BREAK newline
# 	;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()

# continue_statement
# 	:	CONTINUE newline
# 	;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)

    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)

    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)
    
    def visitArgument_list(self, ctx:ZCodeParser.Argument_listContext):
        return self.visitChildren(ctx)

    def visitArgument_prime(self, ctx:ZCodeParser.Argument_primeContext):
        return self.visitChildren(ctx)

    def visitArgument(self, ctx:ZCodeParser.ArgumentContext):
        return self.visitChildren(ctx)

    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)