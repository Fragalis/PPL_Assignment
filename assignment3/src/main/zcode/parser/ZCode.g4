grammar ZCode;
//2110866
@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program
	:	nullable_newline_list
		declaration_list
		nullable_newline_list 
		EOF
	;

declaration_list
	:	declaration nullable_newline_list declaration_list
	|	
	;

declaration
	:	variable_declaration
	|	function_declaration
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
	:	logical_expr1   (	NUMBER_EQ 
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
	:	logical_expr1 (AND | OR) numeric_expr1
	|	numeric_expr1
	;

numeric_expr1
	:	numeric_expr1 (PLUS | MINUS) numeric_expr2
	|	numeric_expr2
	;

numeric_expr2
	:	numeric_expr2 (MUL | DIV | MOD) logical_expr2
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
	|	function_call_expr LBRACKET index_op_expr RBRACKET
	;
function_call_expr
	:	function_call
	;
index_op_expr
	:	expression COMMA index_op_expr
	|	expression
	;
	
term
	:	primitive_literals
	|	identifier
	|	element_expr
	|	function_call_expr
	|	array_value
	|	LPAREN expression RPAREN
	;

// DECLARATIONS

// VARIABLES
variable_declaration
	:	primitive_type_declaration
	|	array_type_declaration
	;

primitive_type_declaration
	:	primitive_type identifier
	|	DYNAMIC	identifier
	|	primitive_type identifier ASSIGN expression
	|	VAR	identifier ASSIGN expression
	|	DYNAMIC	identifier ASSIGN expression
	;

array_type_declaration
	:	primitive_type identifier LBRACKET number_literal_list RBRACKET
	|	primitive_type identifier LBRACKET number_literal_list RBRACKET ASSIGN expression
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
	:	FUNC identifier LPAREN parameter_list RPAREN newline
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
	;

array_parameter
	:	primitive_type identifier LBRACKET number_literal_list RBRACKET
	;

function_full_declaration
	:	FUNC identifier LPAREN parameter_list RPAREN nullable_newline_list function_body
	;

nullable_newline_list
	:	newline_list
	|
	;
newline_list
	:	NEWLINE newline_list
	|	NEWLINE
	;
newline : NEWLINE;

function_body
	:	return_statement
	|	block_statement
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
	:	simple_statement
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
	;

assignment_statement
	:	assignee ASSIGN expression newline
	;
assignee
	:	identifier
	|	array_cell
	;
array_cell
	:	identifier LBRACKET index_op_expr RBRACKET
	;

if_statement
	:	if_clause elif_clause_list else_clause
	;
if_clause
	:	IF conditional_expr nullable_newline_list statement
	;
elif_clause_list
	:	elif_clause elif_clause_list
	|
	;
elif_clause
	:	ELIF conditional_expr nullable_newline_list statement
	;
else_clause
	:	ELSE nullable_newline_list statement
	|
	;
conditional_expr
	:	LPAREN expression RPAREN
	;


for_statement
	:	FOR identifier UNTIL expression BY expression nullable_newline_list statement
	;

break_statement
	:	BREAK newline
	;

continue_statement
	:	CONTINUE newline
	;

return_statement
	:	RETURN expression newline
	|	RETURN newline
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
	:	expression
	|	identifier LBRACKET number_literal_list RBRACKET
	;

block_statement
	:	BEGIN newline_list statement_list END newline_list
	;

// LEXER:

// LITERALS
NUMBER_L
	:	INT DEC? EXP?
	;
BOOL_L
	:	TRUE
	| 	FALSE
	;
STRING_L
	:	QUOTE STRING_CHAR* QUOTE
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

// IDENTIFIER
IDENTIFIER
	:	NONDIGIT (NONDIGIT | DIGIT)*
	;

// COMMENT
COMMENT
	:	'##' ~ [\r\n]*
	-> 	skip
	;	

WHITESPACE
	: 	[ \t\f\r\b]+ 
	-> 	skip
	; 	// skip spaces and tabs

// FRAGMENTS

fragment NONDIGIT : [a-zA-Z_];
fragment DIGIT : [0-9];

fragment INT : DIGIT+;
fragment DEC : '.' DIGIT*;
fragment EXP : [eE] [+-]? DIGIT+;
fragment QUOTE : '"';
fragment QUOTE_IN_STR : '\''["] | '\\' [']["];
fragment CHARACTER : ~["\\\r\n\f];
fragment ESCAPE_SEQ : '\\' [brfnt'\\];
fragment ILLEGAL_ESCAPE_SEQ : '\\' ~[brfnt'\\];
fragment STRING_CHAR : QUOTE_IN_STR | ESCAPE_SEQ | CHARACTER;

// ERROR HANDLER
ILLEGAL_ESCAPE
	:	QUOTE STRING_CHAR* ILLEGAL_ESCAPE_SEQ
	{
		self.text = self.text[1:]
		raise IllegalEscape(self.text)
	}
	;

UNCLOSE_STRING
	:	QUOTE STRING_CHAR*
	{
		self.text = self.text[1:]
		raise UncloseString(self.text)
	};

ERROR_CHAR: . {raise ErrorToken(self.text)};