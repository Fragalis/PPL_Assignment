grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: pre_declaration_list main_function post_declaration_list EOF;
pre_declaration_list
	:	pre_declaration_prime
	|
	;

pre_declaration_prime
	:	pre_declaration nullable_newline_list pre_declaration_prime
	|	pre_declaration
	;

pre_declaration
	:	variable_declaration
	|	function_declaration
	;


post_declaration_list
	:	post_declaration_prime
	|
	;

post_declaration_prime
	:	post_declaration nullable_newline_list post_declaration_prime
	|	post_declaration
	;

post_declaration
	:	variable_declaration
	|	function_full_declaration
	;

main_function
	:	FUNC 'main' LPAREN parameter_list RPAREN nullable_newline_list block_statement
	;

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
	:	LBRACKET array_literal_list RBRACKET
	;

array_literal_list
	:	array_literal_prime
	|
	;

array_literal_prime
	:	array_literal COMMA array_literal_prime
	|	array_literal
	;

array_literal
	:	expression
	|	array_value
	;

identifier
	:	IDENTIFIER
	;

// EXPRESSIONS
expression				// CONCATENATION
	:	relational_expr CONCAT relational_expr
	|	relational_expr
	;

relational_expr			// COMPARISON
	:	logical_expr1 	(	NUMBER_EQ 
					  	| 	STRING_EQ 
					  	|	NEQ
					  	|	LT
					  	|	GT
					  	|	LTEQ
					  	|	GTEQ
					  	)
		logical_expr1
	|	logical_expr1
	;

logical_expr1 			// AND | OR
	:	logical_expr1 ( AND | OR ) numeric_expr1
	|	numeric_expr1
	;

numeric_expr1
	:	numeric_expr1 ( PLUS | MINUS ) numeric_expr2
	|	numeric_expr2
	;

numeric_expr2
	:	numeric_expr2 ( MUL | DIV | MOD ) logical_expr2
	|	logical_expr2
	;

logical_expr2
	:	NOT logical_expr2
	|	numeric_expr3
	;

numeric_expr3
	:	MINUS numeric_expr3
	|	term
	;

element_expr
	:	identifier LBRACKET index_op_expr RBRACKET
	;
index_op_expr
	:	expression
	|	expression COMMA index_op_expr
	;
	
term
	:	primitive_literals
	|	identifier
	|	element_expr
	|	function_call
	|	LPAREN expression RPAREN
	;

// DECLARATIONS

// VARIABLES
variable_declaration
	:	primitive_type_declaration
	|	array_type_declaration
	;

primitive_type_declaration
	:	primitive_type identifier (ASSIGN expression)?
	|	VAR	identifier ASSIGN expression
	|	DYNAMIC	identifier ASSIGN expression
	;

array_type_declaration
	:	primitive_type identifier LBRACKET number_literal_list RBRACKET (ASSIGN array_value)?
	|	VAR	identifier LBRACKET number_literal_list RBRACKET ASSIGN array_value
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
	:	FUNC identifier LPAREN parameter_list RPAREN
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
	:	primitive_type identifier
	|	VAR	identifier
	;

array_parameter
	:	primitive_type identifier LBRACKET number_literal_list RBRACKET
	|	VAR	identifier LBRACKET number_literal_list RBRACKET
	;

function_full_declaration
	:	function_prototype_declaration nullable_newline_list function_body
	;

newline : NEWLINE | EOF;
newline_list
	:	NEWLINE newline_list
	|	NEWLINE | EOF
	;
nullable_newline_list
	:	newline_list
	|
	;

function_body
	:	return_statement newline
	|	block_statement	newline
	|
	;

// STATEMENTS
statement_list
	:	statement nullable_newline_list statement_list
	|	
	;

statement
	:	if_statement
	|	non_if_statement
	;

non_if_statement
	:	simple_statement newline
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
	:	for_statement
	|	block_statement
	|	function_declaration
	;

assignment_statement
	:	assignee ASSIGN expression
	;
assignee
	:	identifier
	|	element_expr
	;

if_statement
	:	IF expression nullable_newline_list statement
		(ELIF expression nullable_newline_list statement)*
		ELSE expression nullable_newline_list statement?
	;

for_statement
	:	FOR identifier UNTIL expression BY expression nullable_newline_list statement
	;

break_statement
	:	BREAK
	;

continue_statement
	:	CONTINUE
	;

return_statement
	:	RETURN expression?
	;

function_call_statement
	:	function_call newline
	;
function_call
	:	identifier LPAREN argument_list RPAREN
	;
argument_list
	:	argument_prime
	|	
	;
argument_prime
	:	argument COMMA argument_prime
	|	argument
	;
argument
	:	parameter
	|	expression
	;

block_statement
	:	BEGIN newline_list statement_list END newline_list
	;

// LEXER:

// LITERALS SECTION
NUMBER_L
	:	INT DEC? EXP?
	;
BOOL_L
	:	TRUE 
	| 	FALSE
	;
STRING_L
	:	QUOTE ( ESCAPE_SEQ | ILLEGAL_NL_STR | QUOTE_IN_STR )* QUOTE
	{self.text = self.text[1:-1]}

	;

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
fragment QUOTE : '"';
fragment QUOTE_IN_STR : '\''["];
fragment ILLEGAL_NL_STR : ~["\r\n];
fragment ESCAPE_SEQ : '\\' [brfnt'\\];
fragment ILLEGAL_ESCAPE_SEQ : '\\' ~[brfnt"'\\];

UNCLOSE_STRING
	: QUOTE ( QUOTE_IN_STR | ESCAPE_SEQ | ILLEGAL_NL_STR )*
	{
		self.text = self.text[1:]
		raise UncloseString(self.text)
	};

ILLEGAL_ESCAPE
	: QUOTE ( QUOTE_IN_STR | ILLEGAL_ESCAPE_SEQ | ILLEGAL_NL_STR )*
	{
		self.text = self.text[1:]
		raise IllegalEscape(self.text)
	}
	;

ERROR_CHAR: . {raise ErrorToken(self.text)};