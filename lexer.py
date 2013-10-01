import ply.lex as lex

class MyLexer:
    # Regular expression rules for simple tokens
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_LBRACE    = r'\{'
    t_RBRACE    = r'\}'
    t_LBRACKET  = r'\['
    t_RBRACKET  = r'\]'
    t_SEMI      = r';'
    t_COMMA     = r','
    t_LESSTHAN  = r'\<'
    t_GREATHAN  = r'\>'
    t_GREATEQUAL= r'\>='
    t_LESSEQUAL = r'\<='
    t_DIFFERENT = r'\<\>'
    t_EQUAL     = r'='
    t_TWOEQUAL  = r'=='
    t_AND       = r'&&'
    t_OR        = r'\|\|'
    t_STRING    = r'".*"'


    #all the reserved words
    reserved = {
        'if' : 'IF',
        'else' : 'ELSE',
        'loop' : 'LOOP',
        'int' : 'INT',
        'float' : 'FLOAT',
        'bool' : 'BOOL',
        'char' : 'CHAR',
        'loop' : 'LOOP',
        'main' : 'MAIN',
        'print' : 'PRINT',
        'brush' : 'BRUSH',
        'pd' : 'PD',
        'pu' : 'PU',
        'fd' : 'FD',
        'rt' : 'RT',
        'read' : 'READ',
        'circle' : 'CIRCLE',
        'square' : 'SQUARE',
        'arc' : 'ARC',
        'void' : 'VOID',
        'color' : 'COLOR',
        'true' : 'TRUE',
        'false' : 'FALSE',
		'home' : 'HOME'
    }
    # List of token names.   This is always required

    tokens = ['GREATEQUAL','LESSEQUAL','INTEGER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN','LBRACE','RBRACE','LBRACKET','RBRACKET','SEMI','ID','COMMA','GREATHAN','LESSTHAN','DIFFERENT','EQUAL','TWOEQUAL','AND','OR','STRING'] +  list(reserved.values())


    listOfTokens = []
    #s reqgular exprsion that takes the fisrts leter then another letter or a number
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        self.listOfTokens.append(t)
        return t


    #get al the comments that are with #
    def t_COMMENT(self,t):
        r'\#.*'
        pass
        # No return value. Token discarded

    #get all the floats
    def t_FLOAT(self,t):
        r'\d+\.\d+'
        t.value=float(t.value)
        self.listOfTokens.append(t)
        return t

    # A regular expression rule with some action code
    def t_INTEGER(self,t):
        r'\d+'
        t.value = int(t.value)
        self.listOfTokens.append(t)
        return t


    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Compute column.
    #     input is the input text string
    #     token is a token instance
    def find_column(self,input,token):
        last_cr = input.rfind('\n',0,token.lexpos)
        if last_cr < 0:
           last_cr = 0
        column = (token.lexpos - last_cr) + 1
        return column


    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    def getAllTokens(self):
        return self.listOfTokens

    # Error handling rule
    def t_error(self,t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            print tok

# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
m.test('''+ 234 oo   22.22 {} []  main == <> < > >= <= && || if  " yolo" ''')     # Test it

print m.getAllTokens()