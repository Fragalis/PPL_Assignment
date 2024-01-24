grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.


program: decllist EOF; // write your rule here
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

//And some other rules for variable declaration, function declaration and other rules

idlist: ID COMMA idlist | ID;

paramlist:	param | ;
param:	typer idlist SEMI param | typer idlist;

statementlist: statement statementlist | ;
statement: assignment | call | ret SEMI;
assignment: ID EQ expr;
call: ID LP exprlist RP;
ret: RETURN expr;

vardecllist: vardecl vardecllist | ;
vardecl: typer idlist SEMI;

funcdecl: typer ID LP paramlist RP body;
typer: INT | FLOAT;

exprlist: expr COMMA exprlist | ;
expr: 'expr';
body: LCB vardecllist | statementlist RCB;

INT: 'int';
FLOAT: 'float';
COMMA: ',';
SEMI: ';';
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
EQ: '=';
RETURN: 'return';
ID: [a-zA-Z]+;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;