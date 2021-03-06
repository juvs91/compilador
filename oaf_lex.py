import ply.lex as lex

# Reserved words
reserved = {
    'arc': 'ARC',
    'bool': 'BOOL',
    'brush': 'BRUSH',
    'char': 'CHAR',
    'circle': 'CIRCLE',
    'color': 'COLOR',
    'else': 'ELSE',
    'false': 'FALSE',
    'fd': 'FD',
    'figure': 'FIGURE',
    'float': 'FLOAT',
    'home': 'HOME',
    'if': 'IF',
    'int': 'INT',
    'length': 'LENGTH',
    'loop': 'LOOP',
    'main': 'MAIN',
    'pd': 'PD',
    'print': 'PRINT',
    'pu': 'PU',
    'read': 'READ',
    'return': 'RETURN',
    'rt': 'RT',
    'square': 'SQUARE',
    'triangle': 'TRIANGLE',
    'true': 'TRUE',
    'void': 'VOID',
    'speed': 'SPEED', 
    'clear':'CLEAR'
}

# List of token names
tokens = [
    # Literals
    'ID', 'ICONST', 'FCONST', 'CCONST', 'STRING',
    # Operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    # Separators
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'SEMI', 'COMMA',
    # Comparison
    'LESSTHAN', 'GREATHAN', 'GREATEQUAL', 'LESSEQUAL', 'DIFFERENT', 'TWOEQUAL',
    # Logical
    'AND', 'OR', 'NOT',
    # Assignment
    'EQUAL',
] + list(reserved.values())

# Regular expression rules
# Identifiers
def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'ID')
    return t

# Float
def t_FCONST(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Integer
def t_ICONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comments
def t_COMMENT(t):
    r'\#.*'
    # No return value, token discarded
    pass

# Literals
t_STRING     = r'".*"'
t_CCONST     = r'\'[ -~]\''
# Operators
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
# Separators
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_SEMI       = r';'
t_COMMA      = r','
# Comparison
t_LESSTHAN   = r'\<'
t_GREATHAN   = r'\>'
t_GREATEQUAL = r'\>='
t_LESSEQUAL  = r'\<='
t_DIFFERENT  = r'\<\>'
t_TWOEQUAL   = r'=='
# Logical
t_AND        = r'&&'
t_OR         = r'\|\|'
t_NOT        = r'!'
# Assignment
t_EQUAL      = r'='

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Compute column.
# input is the input text string
# token is a token instance
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3 + 4 * 10
  # 4.8 0.0
  # "" "hola"
  # derp 'c'
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
    # tok = lexer.token()
    # if not tok: break      # No more input
    # print tok