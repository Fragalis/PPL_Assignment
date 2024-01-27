grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: statement_list;

// PARSER:
// TYPES - VALUES
primitive_type
	:	NUMBER
	|	BOOL
	|	STRING
	;

primitive_literals
	:	NUMBER_L
	|	BOOL_L
	|	STRING_L
	;

array_value
	:   LBRACKET expression_list RBRACKET
	;

expression_list
	:	expression_prime
	|
	;

expression_prime
	:	expression COMMA expression_prime
	|	expression
	;


// EXPRESSIONS
expression				// CONCATENATION
	:	expression CONCAT expression
	|	relational_expr
	;

relational_expr			// COMPARISON
	:	relational_expr (	NUMBER_EQ 
					  	| 	STRING_EQ 
					  	|	NEQ
					  	|	LT
					  	|	GT
					  	|	LTEQ
					  	|	GTEQ
					  	)
		relational_expr
	|	logical_expr1
	;

logical_expr1 			// AND | OR
	:	logical_expr1 ( AND | OR ) numeric_expr1
	|	numeric_expr1
	;

numeric_expr1
	:	numeric_expr1 ( MUL | DIV | MOD ) logical_expr2
	|	numeric_expr1 ( PLUS | MINUS ) logical_expr2
	|	logical_expr2
	;

logical_expr2
	:	NOT logical_expr2
	|	numeric_expr2
	;

numeric_expr2
	:	MINUS numeric_expr2
	|	index_op_expr
	;

index_op_expr
	:	index_op_expr LBRACKET term RBRACKET
	|	term
	;

term
	:	primitive_literals
	|	IDENTIFIER
	|	LPAREN expression RPAREN
	;

// DECLARATIONS

// VARIABLES
variable_declaration
	:	primitive_type_declaration
	|	array_type_declaration
	;

primitive_type_declaration
	:	primitive_type IDENTIFIER (ASSIGN expression)?
	|	VAR	IDENTIFIER ASSIGN expression
	|	DYNAMIC	IDENTIFIER ASSIGN expression
	;

array_type_declaration
	:	primitive_type IDENTIFIER LBRACKET number_literal_list RBRACKET (ASSIGN expression)?
	|	VAR	IDENTIFIER LBRACKET number_literal_list RBRACKET ASSIGN expression
	;

number_literal_list
	:	NUMBER_L COMMA number_literal_list
	|	NUMBER_L
	;

function_declaration
	:	function_prototype_declaration
	|	function_full_declaration
	;

function_prototype_declaration
	:	FUNC IDENTIFIER LPAREN parameter_list RPAREN
	;
parameter_list
	:	parameter_prime
	|	
	;
parameter_prime
	:	parameter COMMA parameter_prime
	|	parameter
	;
parameter
	:	primitive_parameter
	|	array_parameter
	;

primitive_parameter
	:	primitive_type IDENTIFIER
	|	VAR	IDENTIFIER
	;

array_parameter
	:	primitive_type IDENTIFIER LBRACKET number_literal_list RBRACKET
	|	VAR	IDENTIFIER LBRACKET number_literal_list RBRACKET
	;

function_full_declaration
	:	function_prototype_declaration nullable_newline_list function_body
	;

newline_list
	:	NEWLINE newline_list
	|	NEWLINE
	;
nullable_newline_list
	:	newline_list
	|
	;

function_body
	:	return_statement NEWLINE
	|	block_statement	NEWLINE
	|
	;

// STATEMENTS
statement_list
	:	statement nullable_newline_list statement_list
	|
	;

statement
	:	simple_statement NEWLINE
	|	compound_statement
	;

simple_statement
	:	variable_declaration
	|	assignment_statement
	|	break_statement
	|	continue_statement
	|	return_statement
	|	function_call_statement
	;

compound_statement
	:	if_statement
	|	for_statement
	|	block_statement
	|	function_declaration
	;

assignment_statement
	:	
	;

if_statement
	:
	;

for_statement
	:	FOR IDENTIFIER UNTIL expression BY expression nullable_newline_list statement
	;

break_statement
	:	BREAK NEWLINE
	;

continue_statement
	:	CONTINUE NEWLINE
	;

return_statement
	:	RETURN expression? NEWLINE
	;

function_call_statement
	:	IDENTIFIER LPAREN parameter_list RPAREN	NEWLINE
	;

block_statement
	:	BEGIN newline_list statement_list END newline_list
	;

// LEXER:

// KEYWORDS
TRUE : 'true';
FALSE : 'false';
NUMBER : 'number';
BOOL : 'bool';
STRING : 'string';
RETURN : 'return';
VAR : 'var';
DYNAMIC : 'dynamic';
FUNC : 'func';
FOR : 'for';
UNTIL : 'until';
BY : 'by';
BREAK : 'break';
CONTINUE : 'continue';
IF : 'if';
ELSE : 'else';
ELIF : 'elif';
BEGIN : 'begin';
END : 'end';
NOT : 'not';
AND : 'and';
OR : 'or';

// SEPARATORS
LPAREN : '(';
RPAREN : ')';
LBRACKET : '[';
RBRACKET : ']';
COMMA : ',';
NEWLINE : '\n';

// OPERATORS
ASSIGN : '<-';
NEQ : '!=';
GTEQ : '>=';
LTEQ : '<=';
CONCAT : '...';
STRING_EQ : '==';

PLUS : '+';
MINUS : '-';
MUL : '*';
DIV : '/';
MOD : '%';
GT : '>';
LT : '<';
NUMBER_EQ : '=';

IDENTIFIER
	:	NONDIGIT (NONDIGIT | DIGIT)*
	;

// LITERALS SECTION
NUMBER_L
	:	INT DEC? EXP?
	;
BOOL_L
	:	TRUE 
	| 	FALSE
	;
STRING_L
	:	'"' ( '\\' [btnfr'\\] | ~["\\\r\n] | [']["])* '"'
	{self.text = self.text[1:-1]}
	;

// COMMENT SECTION

COMMENT
	:	'##' ~ [\r\n]*
	-> skip
	;	

WHITESPACE
	: [ \t\r\f\b]+ 
	-> skip
	; // skip spaces and tabs

// FRAGMENTS SECTION

fragment NONDIGIT : [a-zA-Z_];
fragment DIGIT : [0-9];
fragment INT : DIGIT+;
fragment DEC : '.' DIGIT*;
fragment EXP : [eE] [+-]? DIGIT+;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING
	: '"' ( '\\'  [btnfr'\\] | ~[\b\t\f\r\n\\"] )*
	{
		self.text = self.text[1:]
		raise ErrorToken(self.text)
	}
	;
ILLEGAL_ESCAPE
	: '"' ( '\\' ~[btnfr'\\] | ~'\\')*
	{
		self.text = self.text[1:]
		raise ErrorToken(self.text)
	}
	;