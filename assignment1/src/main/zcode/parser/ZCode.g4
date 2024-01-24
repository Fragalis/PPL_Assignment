grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: ;

// PARSER:

// TYPES
primitive_type
	:	BOOL 
	| 	NUMBER 
	| 	STRING
	;

primary
	:	BOOL_L | NUMBER_L | STRING_L
	|	IDENTIFIERS
	;

element_value
	:	expression
	|	primary
	;

// EXPRESSIONS
expression
	:	
	|	
	;

// STATEMENTS
statement_list
	:	statement statement_list
	|	
	;

statement
	:	statement_prime	NEWLINE
	;

statement_prime
	:	variable_declaration
	|	assignment
	|	if_statement
	|	for_statement
	|	break_statement
	|	continue_statement
	|	return_statement
	|	function_call_statement
	|	block_statement
	;

break_statement
	:	BREAK
	;

continue_statement
	:	CONTINUE
	;

return_statement
	:	RETURN expression
	|	RETURN
	;

function_call_statement
	:	IDENTIFIERS LP argument_list RP
	;

block_statement
	:	BEGIN block END
	;

// LEXER:

// FRAGMENTS SECTION
	
fragment DIGIT : [0-9];

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
NEWLINE : '\n';

// SEPARATORS
LP : '(';
RP : ')';
LB : '[';
RB : ']';
COMMA : ',';

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

// COMMENT SECTION

COMMENT
	:	'##' ~('\r' | '\n')*
	->	skip
	;	

// LITERALS SECTION
NUMBER_L
	:	DIGIT+ ('.' DIGIT*)? ([eE] [+-]? DIGIT+)?
	;
BOOL_L
	:	TRUE | FALSE
	;
STRING_L
	:	'"' ( '\\' [btnfr'\\] | ~["\\\r\n] )*? '"'
	{self.text = self.text[1:-1]}
	;

// IDENTIFIERS SECTION

IDENTIFIERS
	:	[a-zA-Z_] [a-zA-Z0-9_]*
	;

WHITESPACES: [ \t\r\f\b]+ -> skip; // skip spaces and tabs

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