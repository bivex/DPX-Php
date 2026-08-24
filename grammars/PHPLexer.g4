lexer grammar PHPLexer;

PHP_OPEN : '<?php' | '<?=' | '<?' ;

// Keywords
NAMESPACE     : 'namespace' ;
USE           : 'use' ;
AS            : 'as' ;
CLASS         : 'class' ;
INTERFACE     : 'interface' ;
TRAIT         : 'trait' ;
ENUM          : 'enum' ;
EXTENDS       : 'extends' ;
IMPLEMENTS    : 'implements' ;
FUNCTION      : 'function' ;
FN            : 'fn' ;
PUBLIC        : 'public' ;
PROTECTED     : 'protected' ;
PRIVATE       : 'private' ;
STATIC        : 'static' ;
FINAL         : 'final' ;
ABSTRACT      : 'abstract' ;
READONLY      : 'readonly' ;
CONST         : 'const' ;
RETURN        : 'return' ;
MATCH         : 'match' ;
SWITCH        : 'switch' ;
CASE          : 'case' ;
DEFAULT       : 'default' ;
IF            : 'if' ;
ELSEIF        : 'elseif' ;
ELSE          : 'else' ;
WHILE         : 'while' ;
FOR           : 'for' ;
FOREACH       : 'foreach' ;
NEW           : 'new' ;
CLONE         : 'clone' ;
THROW         : 'throw' ;
TRY           : 'try' ;
CATCH         : 'catch' ;
FINALLY       : 'finally' ;
INSTANCEOF    : 'instanceof' ;
DECLARE       : 'declare' ;

// Punctuation
SEMI          : ';' ;
COLON         : ':' ;
COMMA         : ',' ;
DOT           : '.' ;
ARROW         : '->' ;
NULLSAFE_ARROW: '?->' ;
DOUBLE_COLON  : '::' ;
BACKSLASH     : '\\' ;
DOUBLE_ARROW  : '=>' ;
LPAREN        : '(' ;
RPAREN        : ')' ;
LBRACE        : '{' ;
RBRACE        : '}' ;
LBRACK        : '[' ;
RBRACK        : ']' ;
QUESTION      : '?' ;
PIPE          : '|' ;
AMP           : '&' ;
ELLIPSIS      : '...' ;
EQUAL         : '=' ;

// Literals & Identifiers
VARIABLE      : '$' [a-zA-Z_\u007f-\uffff][a-zA-Z0-9_\u007f-\uffff]* ;
IDENTIFIER    : [a-zA-Z_\u007f-\uffff][a-zA-Z0-9_\u007f-\uffff]* ;
NUMBER        : [0-9]+ ('.' [0-9]+)? ;
STRING_LITERAL: '"' (~["\\] | '\\' .)* '"' | '\'' (~['\\] | '\\' .)* '\'' ;

// Comments & Whitespace
LINE_COMMENT  : ('//' | '#') ~[\r\n]* -> channel(HIDDEN) ;
BLOCK_COMMENT : '/*' .*? '*/' -> channel(HIDDEN) ;
WS            : [ \t\r\n]+ -> channel(HIDDEN) ;

// Fallback for other operators
OTHER_OP      : [+\-*/%^!~<>&|?]+ ;
