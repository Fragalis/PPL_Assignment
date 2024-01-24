grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: ;

// PARSER:


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
MULT : '*';
DIV : '/';
MOD : '%';
GT : '>';
LT : '<';
NUMBER_EQ : '=';

// COMMENT SECTION

COMMENT
	:	'##' ~('\r' | '\n')*
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