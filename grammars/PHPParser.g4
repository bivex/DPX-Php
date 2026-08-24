parser grammar PHPParser;

options { tokenVocab=PHPLexer; }

phpFile
    : PHP_OPEN? declareStatement* namespaceStatement? topLevelStatement* EOF
    ;

declareStatement
    : DECLARE LPAREN qualifiedName EQUAL literal RPAREN SEMI
    ;

namespaceStatement
    : NAMESPACE qualifiedName (SEMI | LBRACE topLevelStatement* RBRACE)
    ;

useStatement
    : USE useDeclarationList SEMI
    | USE qualifiedName DOUBLE_COLON LBRACE useItem (COMMA useItem)* RBRACE SEMI
    ;

useDeclarationList
    : useItem (COMMA useItem)*
    ;

useItem
    : qualifiedName (AS IDENTIFIER)?
    ;

topLevelStatement
    : useStatement
    | classDeclaration
    | interfaceDeclaration
    | traitDeclaration
    | enumDeclaration
    | functionDeclaration
    | statement
    ;

classDeclaration
    : classModifier* CLASS IDENTIFIER (EXTENDS qualifiedName)? (IMPLEMENTS qualifiedNameList)? LBRACE classMember* RBRACE
    ;

interfaceDeclaration
    : INTERFACE IDENTIFIER (EXTENDS qualifiedNameList)? LBRACE classMember* RBRACE
    ;

traitDeclaration
    : TRAIT IDENTIFIER LBRACE classMember* RBRACE
    ;

enumDeclaration
    : ENUM IDENTIFIER (COLON type)? (IMPLEMENTS qualifiedNameList)? LBRACE classMember* RBRACE
    ;

classMember
    : methodDeclaration
    | propertyDeclaration
    | constDeclaration
    | useTraitStatement
    | statement
    ;

useTraitStatement
    : USE qualifiedNameList SEMI
    ;

constDeclaration
    : memberModifier* CONST IDENTIFIER EQUAL expression SEMI
    ;

propertyDeclaration
    : memberModifier+ type? VARIABLE (EQUAL expression)? (COMMA VARIABLE (EQUAL expression)?)* SEMI
    ;

methodDeclaration
    : memberModifier* FUNCTION methodName LPAREN parameterList? RPAREN (COLON type)? (block | SEMI)
    ;

functionDeclaration
    : FUNCTION IDENTIFIER LPAREN parameterList? RPAREN (COLON type)? block
    ;

methodName
    : IDENTIFIER
    | keywordAsIdentifier
    ;

keywordAsIdentifier
    : MATCH | SWITCH | CASE | DEFAULT | IF | ELSEIF | ELSE | WHILE | FOR | FOREACH
    | NEW | CLONE | THROW | TRY | CATCH | FINALLY | CLASS | INTERFACE | TRAIT | ENUM
    | EXTENDS | IMPLEMENTS | FUNCTION | PUBLIC | PROTECTED | PRIVATE | STATIC
    | FINAL | ABSTRACT | READONLY | CONST | RETURN | USE | AS | INSTANCEOF
    ;

parameterList
    : parameter (COMMA parameter)* COMMA?
    ;

parameter
    : memberModifier* type? AMP? ELLIPSIS? VARIABLE (EQUAL expression)?
    ;

classModifier
    : ABSTRACT
    | FINAL
    | READONLY
    ;

memberModifier
    : PUBLIC
    | PROTECTED
    | PRIVATE
    | STATIC
    | FINAL
    | ABSTRACT
    | READONLY
    ;

qualifiedNameList
    : qualifiedName (COMMA qualifiedName)*
    ;

qualifiedName
    : BACKSLASH? (IDENTIFIER | keywordAsIdentifier) (qualifiedSeparator (IDENTIFIER | keywordAsIdentifier))*
    ;

qualifiedSeparator
    : BACKSLASH
    | DOUBLE_COLON
    | OTHER_OP
    ;

type
    : QUESTION? qualifiedName (PIPE qualifiedName)*
    ;

block
    : LBRACE statement* RBRACE
    ;

statement
    : block
    | RETURN expression? SEMI
    | THROW expression SEMI
    | IF LPAREN expression RPAREN statement (ELSEIF LPAREN expression RPAREN statement)* (ELSE statement)?
    | SWITCH LPAREN expression RPAREN LBRACE switchBlock* RBRACE
    | WHILE LPAREN expression RPAREN statement
    | FOR LPAREN expression? SEMI expression? SEMI expression? RPAREN statement
    | FOREACH LPAREN expression AS (expression DOUBLE_ARROW)? expression RPAREN statement
    | TRY block (CATCH LPAREN type VARIABLE RPAREN block)* (FINALLY block)?
    | expression SEMI
    | SEMI
    ;

switchBlock
    : (CASE expression | DEFAULT) COLON statement*
    ;

expression
    : primaryExpression (operator primaryExpression)*
    ;

primaryExpression
    : VARIABLE
    | literal
    | qualifiedName
    | matchExpression
    | newExpression
    | cloneExpression
    | closureExpression
    | arrayExpression
    | functionCall
    | memberAccess
    | LPAREN expression RPAREN
    ;

newExpression
    : NEW qualifiedName (LPAREN argumentList? RPAREN)?
    | NEW CLASS (EXTENDS qualifiedName)? (IMPLEMENTS qualifiedNameList)? LPAREN argumentList? RPAREN LBRACE classMember* RBRACE
    ;

cloneExpression
    : CLONE expression
    ;

closureExpression
    : (STATIC)? FUNCTION LPAREN parameterList? RPAREN (USE LPAREN parameterList? RPAREN)? (COLON type)? block
    | (STATIC)? FN LPAREN parameterList? RPAREN (COLON type)? DOUBLE_ARROW expression
    ;

arrayExpression
    : LBRACK (arrayElement (COMMA arrayElement)* COMMA?)? RBRACK
    ;

arrayElement
    : (expression DOUBLE_ARROW)? expression
    ;

matchExpression
    : MATCH LPAREN expression RPAREN LBRACE (matchArm (COMMA matchArm)* COMMA?)? RBRACE
    ;

matchArm
    : (expression (COMMA expression)* | DEFAULT) DOUBLE_ARROW expression
    ;

functionCall
    : qualifiedName LPAREN argumentList? RPAREN
    ;

memberAccess
    : (VARIABLE | qualifiedName | LPAREN expression RPAREN) (ARROW | NULLSAFE_ARROW | DOUBLE_COLON) (IDENTIFIER | VARIABLE | functionCall)
    ;

argumentList
    : argument (COMMA argument)* COMMA?
    ;

argument
    : (IDENTIFIER COLON)? ELLIPSIS? expression
    ;

literal
    : NUMBER
    | STRING_LITERAL
    ;

operator
    : EQUAL
    | DOUBLE_ARROW
    | ARROW
    | NULLSAFE_ARROW
    | DOUBLE_COLON
    | DOT
    | PIPE
    | AMP
    | INSTANCEOF
    | OTHER_OP
    ;
