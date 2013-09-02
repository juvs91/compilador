# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LKEY    = r'\{' 
t_RKEY    = r'\}'
t_LBRACKET= r'\['
t_RBRACKET= r'\]'  
t_TERMINAL= r';' 
t_COMMA   = r','
t_GREATHAN= r'\<'
t_LESSTHAN= r'\>' 
t_DOT     = r'\.'
t_TWODOTS = r':'  
t_DIFERENT= r'\<\>' 
t_EQUAL   = r'='
t_TWOEQUAL= r'=='

                                                                                 

#all the reserved words
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'int' : 'INT',
   'float' : 'FLOAT',
   'bool' : 'BOOL',
   'double' : 'DOUBLE',
   'char' : 'CHAR',
   'public' : 'PUBLIC',
   'private' : 'PRIVATE',
   'loop' : 'LOOP',
   'function' : 'FUNCTION',
   'main' : 'MAIN', 
   'var' : 'VARS', 
   'print' : 'PRINT'
}


# List of token names.   This is always required

tokens = ['NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN','LKEY','RKEY','LBRACKET','RBRACKET','TERMINAL','ID','COMMA','GREATHAN','LESSTHAN','DOT','TWODOTS','DIFERENT','EQUAL','TWOEQUAL'] +  list(reserved.values())

#s reqgular exprsion that takes the fisrts leter then another letter or a number 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


#get al the comments that are with #
def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
       last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):   
    column = find_column(t.value[0],t)
    print "Illegal character"+t.value[0] +" in column '%d' and on line " %column  
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
3 + 4 * 10
  + -20 *2
  [ ] { } adfasd d33 if else @~> 333mil function loop int float double var  main , . < > <> :  = == print ;
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
