grammar BKOOL;

program: EOF;

IDEN : [a-z] [a-z0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
