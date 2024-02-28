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
        return Program(self.visit(ctx.declaration_list()))
    
# declaration_list
# 	:	declaration nullable_newline_list declaration_list
# 	|	
# 	;
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.declaration())] + self.visit(ctx.declaration_list())

# declaration
# 	:	variable_declaration
# 	|	function_declaration
# 	|	function_full_declaration
# 	;
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        if ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        if ctx.function_full_declaration():
            return self.visit(ctx.function_full_declaration())

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
        if ctx.NUMBER_L():    return NumberLiteral(float(ctx.NUMBER_L().getText()))
        if ctx.BOOL_L():      return BooleanLiteral(ctx.BOOL_L().getText())
        return StringLiteral(ctx.STRING_L().getText())

# array_value
# 	:	LBRACKET array_literal_list RBRACKET
# 	;
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return ArrayLiteral(self.visit(ctx.array_literal_list()))

# array_literal_list
# 	:	array_literal_prime
# 	|
# 	;
    def visitArray_literal_list(self, ctx:ZCodeParser.Array_literal_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.array_literal_prime())

# array_literal_prime
# 	:	array_literal COMMA array_literal_prime
# 	|	array_literal
# 	;
    def visitArray_literal_prime(self, ctx:ZCodeParser.Array_literal_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_literal())]
        return [self.visit(ctx.array_literal())] + self.visit(ctx.array_literal_prime())

# array_literal
# 	:	expression
# 	|	array_value
# 	;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visit(ctx.expression()) if ctx.expression() else self.visit(ctx.array_value())

# identifier
# 	:	IDENTIFIER
# 	;
    def visitIdentifier(self, ctx:ZCodeParser.IdentifierContext):
        return Id(ctx.IDENTIFIER().getText())

# expression				// CONCATENATION
# 	:	relational_expr CONCAT relational_expr
# 	|	relational_expr
# 	;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relational_expr(0))
        return BinaryOp(ctx.getChild(1).getText(),
                        left = self.visit(ctx.relational_expr(0)),
                        right = self.visit(ctx.relational_expr(1))
                        )

# relational_expr			// COMPARISON
# 	:	logical_expr1 	(	NUMBER_EQ 
# 					  	| 	STRING_EQ 
# 					  	|	NEQ
# 					  	|	LT
# 					  	|	GT
# 					  	|	LTEQ
# 					  	|	GTEQ
# 					  	)
# 		logical_expr1
# 	|	logical_expr1
# 	;
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logical_expr1(0))
        return BinaryOp(ctx.getChild(1).getText(),
                        left = self.visit(ctx.logical_expr1(0)),
                        right = self.visit(ctx.logical_expr1(1))
                        )

# logical_expr1 			// AND | OR
# 	:	logical_expr1 ( AND | OR ) numeric_expr1
# 	|	numeric_expr1
# 	;
    def visitLogical_expr1(self, ctx:ZCodeParser.Logical_expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.numeric_expr1())
        return BinaryOp(ctx.getChild(1).getText(),
                        left = self.visit(ctx.logical_expr1()),
                        right = self.visit(ctx.numeric_expr1())
                        )

# numeric_expr1
# 	:	numeric_expr1 ( PLUS | MINUS ) numeric_expr2
# 	|	numeric_expr2
# 	;
    def visitNumeric_expr1(self, ctx:ZCodeParser.Numeric_expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.numeric_expr2())
        return BinaryOp(ctx.getChild(1).getText(),
                        left = self.visit(ctx.numeric_expr1()),
                        right = self.visit(ctx.numeric_expr2())
                        )

# numeric_expr2
# 	:	numeric_expr2 ( MUL | DIV | MOD ) logical_expr2
# 	|	logical_expr2
# 	;
    def visitNumeric_expr2(self, ctx:ZCodeParser.Numeric_expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logical_expr2())
        return BinaryOp(ctx.getChild(1).getText(),
                        left = self.visit(ctx.numeric_expr2()),
                        right = self.visit(ctx.logical_expr2())
                        )

# logical_expr2
# 	:	NOT logical_expr2
# 	|	numeric_expr3
# 	;
    def visitLogical_expr2(self, ctx:ZCodeParser.Logical_expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.numeric_expr3())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.logical_expr2()))

# numeric_expr3
# 	:	MINUS numeric_expr3
# 	|	term
# 	;
    def visitNumeric_expr3(self, ctx:ZCodeParser.Numeric_expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.numeric_expr3()))

# element_expr
# 	:	identifier LBRACKET index_op_expr RBRACKET
# 	|	function_call LBRACKET index_op_expr RBRACKET
# 	;   
    def visitElement_expr(self, ctx:ZCodeParser.Element_exprContext):
        index_op = self.visit(ctx.index_op_expr())
        if ctx.identifier():
            return ArrayCell(self.visit(ctx.identifier()), index_op)
        return ArrayCell(self.visit(ctx.function_call_expr()), index_op)

# function_call_expr
# 	:	function_call
# 	;
    def visitFunction_call_expr(self, ctx:ZCodeParser.Function_call_exprContext):
        func_call_expr = self.visit(ctx.function_call())
        return CallExpr(func_call_expr[0], func_call_expr[1])

# index_op_expr
# 	:	expression COMMA index_op_expr
# 	|	expression
# 	;
    def visitIndex_op_expr(self, ctx:ZCodeParser.Index_op_exprContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.index_op_expr())

# term
# 	:	primitive_literals
# 	|	identifier
# 	|	element_expr
# 	|	function_call_expr
# 	|	LPAREN expression RPAREN
# 	;
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        if ctx.primitive_literals():  
            return self.visit(ctx.primitive_literals())
        elif ctx.identifier():
            return self.visit(ctx.identifier())
        elif ctx.element_expr():
            return self.visit(ctx.element_expr())
        elif ctx.function_call_expr():
            return self.visit(ctx.function_call_expr())
        return self.visit(ctx.expression())
    
# variable_declaration
# 	:	primitive_type_declaration
# 	|	array_type_declaration
# 	;
    def visitVariable_declaration(self, ctx:ZCodeParser.Variable_declarationContext):
        return self.visit(ctx.primitive_type_declaration()) if ctx.primitive_type_declaration() else self.visit(ctx.array_type_declaration())

# primitive_type_declaration
# 	:	primitive_type identifier
# 	|	primitive_type identifier ASSIGN expression
# 	|	VAR	identifier ASSIGN expression
# 	|	DYNAMIC	identifier ASSIGN expression
# 	;
    def visitPrimitive_type_declaration(self, ctx:ZCodeParser.Primitive_type_declarationContext):
        iden = self.visit(ctx.identifier())
        
        # primitive_type identifier
        if ctx.getChildCount() == 2:
            typer = self.visit(ctx.primitive_type())
            return VarDecl(iden, typer)
        
        expr = self.visit(ctx.expression())
        # primitive_type identifier ASSIGN expression
        if ctx.getChild(0) == ctx.primitive_type():
            typer = self.visit(ctx.primitive_type())
            return VarDecl(iden, typer, None, expr)
        
        # VAR identifier ASSIGN expression
        if ctx.getChild(0) == ctx.VAR():
            return VarDecl(iden, None, ctx.VAR().getText(), expr)
        
        # DYNAMIC identifier ASSIGN expression
        if ctx.getChild(0) == ctx.DYNAMIC():
            return VarDecl(iden, None, ctx.DYNAMIC().getText(), expr)

# array_type_declaration
# 	:	primitive_type identifier LBRACKET number_literal_list RBRACKET
# 	|	primitive_type identifier LBRACKET number_literal_list RBRACKET ASSIGN array_value
# 	;
    def visitArray_type_declaration(self, ctx:ZCodeParser.Array_type_declarationContext):
        array_type = ArrayType(self.visit(ctx.number_literal_list()), self.visit(ctx.primitive_type()))
        iden = self.visit(ctx.identifier())
        if ctx.getChildCount() == 5:
            return VarDecl(iden, array_type)
        return VarDecl(iden, array_type, None, self.visit(ctx.array_value()))

# number_literal_list
# 	:	NUMBER_L COMMA number_literal_list
# 	|	NUMBER_L
# 	;
    def visitNumber_literal_list(self, ctx:ZCodeParser.Number_literal_listContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBER_L().getText())]
        return [float(ctx.NUMBER_L().getText())] + self.visit(ctx.number_literal_list())

# function_declaration
# 	:	function_prototype_declaration
# 	|	function_full_declaration
# 	;
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visit(ctx.function_prototype_declaration()) if ctx.function_prototype_declaration() else self.visit(ctx.function_full_declaration())

# function_prototype_declaration
# 	:	FUNC identifier LPAREN parameter_list RPAREN newline
# 	;
    def visitFunction_prototype_declaration(self, ctx:ZCodeParser.Function_prototype_declarationContext):
        return FuncDecl(self.visit(ctx.identifier()), self.visit(ctx.parameter_list()), None)

# parameter_list
# 	:	parameter_prime
# 	|	
# 	;
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameter_prime())

# parameter_prime
# 	:	parameter COMMA parameter_prime
# 	|	parameter
# 	;
    def visitParameter_prime(self, ctx:ZCodeParser.Parameter_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameter_prime())

# parameter
# 	:	primitive_parameter
# 	|	array_parameter
# 	;
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visit(ctx.primitive_parameter()) if ctx.primitive_parameter() else self.visit(ctx.array_parameter())

# primitive_parameter
# 	:	primitive_type identifier
# 	;
    def visitPrimitive_parameter(self, ctx:ZCodeParser.Primitive_parameterContext):
        return VarDecl(self.visit(ctx.identifier()), self.visit(ctx.primitive_type()), None, None)

# array_parameter
# 	:	primitive_type identifier LBRACKET number_literal_list RBRACKET
# 	;
    def visitArray_parameter(self, ctx:ZCodeParser.Array_parameterContext):
        arr_type = ArrayType(self.visit(ctx.number_literal_list()), self.visit(ctx.primitive_type()))
        return VarDecl(self.visit(ctx.identifier()),arr_type)

# function_full_declaration
# 	:	FUNC identifier LPAREN parameter_list RPAREN nullable_newline_list function_body
# 	;
    def visitFunction_full_declaration(self, ctx:ZCodeParser.Function_full_declarationContext):
        return FuncDecl(self.visit(ctx.identifier()),
                        self.visit(ctx.parameter_list()),
                        self.visit(ctx.function_body())
                        )

# nullable_newline_list
# 	:	newline_list
# 	|
# 	;
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return None

# newline_list
# 	:	NEWLINE newline_list
# 	|	NEWLINE
# 	;
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return None

# newline : NEWLINE;
    def visitNewline(self, ctx:ZCodeParser.NewlineContext):
        return None

# function_body
# 	:	return_statement
# 	|	block_statement
# 	;
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visit(ctx.return_statement()) if ctx.return_statement() else self.visit(ctx.block_statement())

# statement_list
# 	:	statement nullable_newline_list statement_list
# 	|	
# 	;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())

# statement
# 	:	if_statement
# 	|	non_if_statement
# 	;
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visit(ctx.if_statement()) if ctx.if_statement() else self.visit(ctx.non_if_statement())

# non_if_statement
# 	:	simple_statement
# 	|	compound_statement
# 	;
    def visitNon_if_statement(self, ctx:ZCodeParser.Non_if_statementContext):
        return self.visit(ctx.simple_statement()) if ctx.simple_statement() else self.visit(ctx.compound_statement())

# simple_statement
# 	:	variable_declaration
# 	|	assignment_statement
# 	|	break_statement
# 	|	continue_statement
# 	|	return_statement
# 	|	function_call_statement
# 	;
    def visitSimple_statement(self, ctx:ZCodeParser.Simple_statementContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():   
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():    
            return self.visit(ctx.return_statement())
        return self.visit(ctx.function_call_statement())

# compound_statement
# 	:	for_statement
# 	|	block_statement
# 	;
    def visitCompound_statement(self, ctx:ZCodeParser.Compound_statementContext):
        return self.visit(ctx.for_statement()) if ctx.for_statement() else self.visit(ctx.block_statement())

# assignment_statement
# 	:	assignee ASSIGN expression newline
# 	;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return Assign(self.visit(ctx.assignee()), self.visit(ctx.expression()))

# assignee
# 	:	identifier
# 	|	array_cell
# 	;
    def visitAssignee(self, ctx:ZCodeParser.AssigneeContext):
        return self.visit(ctx.identifier()) if ctx.identifier() else self.visit(ctx.array_cell())
    
# array_cell
# 	:	identifier LBRACKET index_op_expr RBRACKET
# 	;
    def visitArray_cell(self, ctx:ZCodeParser.Array_cellContext):
        return ArrayCell(self.visit(ctx.identifier()), self.visit(ctx.index_op_expr()))

# if_statement
# 	:	if_clause elif_clause_list else_clause
# 	;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        if_cl = self.visit(ctx.if_clause())
        elif_cl_list = self.visit(ctx.elif_clause_list())
        else_cl = self.visit(ctx.else_clause())
        return If(if_cl[0], if_cl[1], elif_cl_list, else_cl)

# if_clause
# 	:	IF conditional_expr nullable_newline_list statement
# 	;
    def visitIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        return [self.visit(ctx.conditional_expr()), self.visit(ctx.statement())]
    
# elif_clause_list
# 	:	elif_clause elif_clause_list
# 	|
# 	;
    def visitElif_clause_list(self, ctx:ZCodeParser.Elif_clause_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elif_clause())] + self.visit(ctx.elif_clause_list())
    
# elif_clause
# 	:	ELIF conditional_expr nullable_newline_list statement
# 	;
    def visitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        return tuple((self.visit(ctx.conditional_expr()), self.visit(ctx.statement())))


    def visitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        return self.visitChildren(ctx)

    def visitConditional_expr(self, ctx:ZCodeParser.Conditional_exprContext):
        return self.visitChildren(ctx)

# for_statement
# 	:	FOR identifier UNTIL expression BY expression nullable_newline_list statement
# 	;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return For(self.visit(ctx.identifier()),
                   self.visit(ctx.expression(0)),
                   self.visit(ctx.expression(1)),
                   self.visit(ctx.statement())
                    )

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
    
# return_statement
# 	:	RETURN expression newline
# 	|	RETURN newline
# 	;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()
    
# function_call_statement
# 	:	function_call newline
# 	;
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        func_call_stmt = self.visit(ctx.function_call())
        return CallStmt(func_call_stmt[0], func_call_stmt[1])
    
# function_call
# 	:	identifier LPAREN argument_list RPAREN
# 	; 
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return [self.visit(ctx.identifier()), self.visit(ctx.argument_list())]

# argument_list
# 	:	argument_prime
# 	|	
# 	;
    def visitArgument_list(self, ctx:ZCodeParser.Argument_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.argument_prime())
    
# argument_prime
# 	:	argument COMMA argument_prime
# 	|	argument
# 	;
    def visitArgument_prime(self, ctx:ZCodeParser.Argument_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argument())]
        return [self.visit(ctx.argument())] + self.visit(ctx.argument_prime())

# argument
# 	:	expression
# 	|	identifier LBRACKET number_literal_list RBRACKET
# 	;
    def visitArgument(self, ctx:ZCodeParser.ArgumentContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression())
        return 

# block_statement
# 	:	BEGIN newline_list statement_list END newline_list
# 	;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(self.visit(ctx.statement_list()))