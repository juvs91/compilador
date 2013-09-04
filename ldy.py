import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from ldl import tokens

def p_main(p):
    'main : PROGRAM ID SEMI vars block'
    
def p_vars(p):
    '''vars : varlist
            | empty'''
    
def p_varlist(p):
    'varlist : VAR idlist COLON type SEMI varlist1'
           
def p_varlist_1(p):
    '''varlist1 : idlist COLON type SEMI varlist1
                | empty'''
                
def p_idlist(p):
    'idlist : ID idlist1'
    
def p_idlist_1(p):
    '''idlist1 : COMMA idlist
               | empty'''
    
def p_type(p):
    '''type : INT
            | FLOAT'''
            
def p_block(p):
    'block : LBRACE block1 RBRACE'
    
def p_block_1(p):
    '''block1 : instr
              | empty'''
              
def p_instr(p):
    '''instr : assign
             | cond
             | write'''
             
def p_assign(p):
    'assign : ID EQUAL expr SEMI'
    
def p_cond(p):
    'cond : IF LPAREN expr RPAREN block cond1 SEMI'
    
def p_write(p):
    'write : PRINT LPAREN write1 RPAREN SEMI'
    
def p_write_1(p):
    '''write1 : expr write2
              | SCONST write2'''
               
def p_write_2(p):
    '''write2 : COMMA write1
              | empty'''
    
def p_cond_1(p):
    '''cond1 : ELSE block
             | empty'''
    
def p_expr(p):
    'expr : exp expr1'
    
def p_expr_1(p):
    '''expr1 : GREATER exp
             | LESS exp
             | NOTEQUAL exp
             | empty'''

def p_exp(p):
    'exp : term exp1'
    
def p_exp_1(p):
    '''exp1 : PLUS exp
            | MINUS exp
            | empty'''

def p_term(p):
    'term : factor term1'
    
def p_factor(p):
    '''factor : LPAREN expr RPAREN
              | factor1 const'''
              
def p_factor_1(p):
    '''factor1 : PLUS
               | MINUS
               | empty'''
    
def p_term_1(p):
    '''term1 : TIMES term
             | DIVIDE term
             | empty'''
             
def p_const(p):
    '''const : ID
             | ICONST
             | FCONST'''
            
# def p_expression_plus(p):
    # 'expression : expression PLUS term'
    # p[0] = p[1] + p[3]

# def p_expression_minus(p):
    # 'expression : expression MINUS term'
    # p[0] = p[1] - p[3]

# def p_expression_term(p):
    # 'expression : term'
    # p[0] = p[1]

# def p_term_times(p):
    # 'term : term TIMES factor'
    # p[0] = p[1] * p[3]

# def p_term_div(p):
    # 'term : term DIVIDE factor'
    # p[0] = p[1] / p[3]

# def p_term_factor(p):
    # 'term : factor'
    # p[0] = p[1]

# def p_factor_num(p):
    # 'factor : ICONST'
    # p[0] = p[1]

# def p_factor_expr(p):
    # 'factor : LPAREN expression RPAREN'
    # p[0] = p[2]

# Empty production
def p_empty(p):
    'empty :'
    pass
    
# Error rule for syntax errors
def p_error(p):
    try:
        print "Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, p.lexpos, p.value)
    except:
        pass
#   print repr(p)

# Build the parser
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    for line in f:
        result = parser.parse(line)
        print result