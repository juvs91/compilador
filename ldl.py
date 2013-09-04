import ply.lex as lex

# Reserved words
reserved = {
    'else' : 'ELSE',
    'float' : 'FLOAT',
	'if' : 'IF',
    'int' : 'INT',
    'print' : 'PRINT',
    'program' : 'PROGRAM',
    'var' : 'VAR',
}

# List of token names
tokens = [
    # Literals
    'ID', 'ICONST', 'FCONST', 'SCONST',
    # Operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'GREATER', 'LESS', 'NOTEQUAL',
    # Separators
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COLON', 'SEMI', 'COMMA', 'PERIOD',
    # Assignment
    'EQUAL',
] + list(reserved.values())

# Regular expression rules for tokens ordered on decreasing length for rule matching
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value,'ID')
    return t

def t_FCONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t
    
def t_ICONST(t):
    r'\d+'
    t.value = int(t.value)    
    return t
    
# Literals
t_SCONST    = r'".*"'
# Operators
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_GREATER   = r'>'
t_LESS      = r'<'
t_NOTEQUAL  = r'<>'
#Separators
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COLON     = r':'
t_SEMI      = r';'
t_COMMA     = r','
t_PERIOD    = r'\.'
# Assignment
t_EQUAL     = r'='

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3 + 4 * 10
  # 4.8 4. 0.0 .2
  # "" "hola"
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
    # tok = lexer.token()
    # if not tok: break      # No more input
    # print tok