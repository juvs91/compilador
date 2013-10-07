import ply.yacc as yacc

# debug
import sys

# Get semantic variables
import oaf_sem as sem

# Get tokens from the lexer
from oaf_lex import tokens
# Get the lexer
from oaf_lex import lexer
from oaf_lex import find_column

def p_program(p):
    '''Program : Declaration Function Main'''

def p_main(p):
    '''Main : MAIN Change_Scope LPAREN RPAREN FBlock'''

def p_declaration(p):
    '''Declaration : Primitive ID Array Array Seen_Variable SEMI Declaration
                   | empty'''

def p_array(p):
    '''Array : LBRACKET ICONST RBRACKET
             | empty'''

def p_function(p):
    '''Function : Function1
                | RFunction
                | empty'''

def p_function_1(p):
    '''Function1 : VOID ID Change_Scope LPAREN ParamList RPAREN FBlock Restore_Scope Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID Change_Scope LPAREN ParamList RPAREN RFBlock Restore_Scope Function'''

def p_block(p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fblock(p):
    '''FBlock : LBRACE Declaration Instruction RBRACE'''

def p_rfblock(p):
    '''RFBlock : LBRACE Declaration Instruction RETURN SuperExpr SEMI RBRACE'''

def p_conditional(p):
    '''Conditional : IF LPAREN SuperExpr RPAREN Block Else'''

def p_else(p):
    '''Else : ELSE Block
            | empty'''

def p_superexpr(p):
    '''SuperExpr : Expression SuperExpr1'''

def p_superexpr_1(p):
    '''SuperExpr1 : AND SuperExpr
                  | OR SuperExpr
                  | empty'''

def p_expression(p):
    '''Expression : Expr Expression1'''

def p_expression_1(p):
    '''Expression1 : LESSTHAN Expr
                   | GREATHAN Expr
                   | DIFFERENT Expr
                   | TWOEQUAL Expr
                   | GREATEQUAL Expr
                   | LESSEQUAL Expr
                   | empty'''

def p_expr(p):
    '''Expr : Term Expr1'''

def p_expr_1(p):
    '''Expr1 : MINUS Expr
             | PLUS Expr
             | empty'''

def p_term(p):
    '''Term : Factor Term1'''

def p_term_1(p):
    '''Term1 : DIVIDE Term
             | TIMES Term
             | empty'''

def p_factor(p):
    '''Factor : LPAREN SuperExpr RPAREN
              | Factor1'''

def p_factor_1(p):
    '''Factor1 : MINUS Constant
               | PLUS Constant
               | Constant'''

def p_params(p):
    '''Params : Params2
              | empty'''

def p_params_1(p):
    '''Params1 : Params2'''

def p_params_2(p):
    '''Params2 : SuperExpr Params3
               | STRING Params3'''

def p_params_3(p):
    '''Params3 : COMMA Params2
               | empty'''

def p_loop(p):
    '''Loop : LOOP LPAREN SuperExpr RPAREN Block'''

def p_assign(p):
    '''Assign : ID EQUAL Assign1'''

def p_assign_1(p):
    '''Assign1 : SuperExpr
               | Call
               | STRING
               | CCONST'''

def p_call(p):
    '''Call : ID LPAREN Params RPAREN'''

def p_read(p):
    '''Read : READ LPAREN Type COMMA ID RPAREN'''

def p_type(p):
    '''Type : Primitive
            | STRING'''

def p_print(p):
    '''Print : PRINT LPAREN Params1 RPAREN'''

def p_brush(p):
    '''Brush : BRUSH LPAREN Color COMMA SuperExpr RPAREN'''

def p_color(p):
    '''Color : COLOR LPAREN SuperExpr COMMA SuperExpr COMMA SuperExpr RPAREN'''

def p_pendown(p):
    '''PenDown : PD LPAREN RPAREN'''

def p_penup(p):
    '''PenUp : PU LPAREN RPAREN'''

def p_home(p):
    '''Home : HOME LPAREN RPAREN'''

def p_forward(p):
    '''Forward : FD LPAREN SuperExpr RPAREN'''

def p_rotate(p):
    '''Rotate : RT LPAREN SuperExpr RPAREN'''

def p_circle(p):
    '''Circle : CIRCLE LPAREN SuperExpr RPAREN'''

def p_arc(p):
    '''Arc : ARC LPAREN SuperExpr COMMA SuperExpr RPAREN'''

def p_square(p):
    '''Square : SQUARE LPAREN SuperExpr RPAREN'''

def p_param(p):
    '''Param : Primitive ID Array1 Array1 Seen_Variable'''

def p_array_1(p):
    '''Array1 : LBRACKET RBRACKET
              | empty'''

def p_primitive(p):
    '''Primitive : INT
                 | FLOAT
                 | BOOL
                 | CHAR'''
    p[0] = p[1]

def p_paramlist(p):
    '''ParamList : ParamList1
                 | empty'''

def p_paramlist_1(p):
    '''ParamList1 : Param ParamList2'''

def p_paramlist_2(p):
    '''ParamList2 : COMMA ParamList1
                  | empty'''

def p_instruccion(p):
    '''Instruction : Loop SEMI Instruction
                   | Conditional SEMI Instruction
                   | Assign SEMI Instruction
                   | Call SEMI Instruction
                   | Brush SEMI Instruction
                   | Read SEMI Instruction
                   | Print SEMI Instruction
                   | PenDown SEMI Instruction
                   | PenUp  SEMI Instruction
                   | Home SEMI Instruction
                   | Forward SEMI Instruction
                   | Rotate SEMI Instruction
                   | Color SEMI Instruction
                   | Circle SEMI Instruction
                   | Arc SEMI Instruction
                   | Square SEMI Instruction
                   | empty'''

def p_constant(p):
    '''Constant : ID
                | FCONST
                | ICONST
                | FALSE
                | TRUE'''

# Update variable table
def p_seen_variable(p):
    '''Seen_Variable : '''
    var_table = sem.var_table
    scope = sem.scope
    if(var_table.get(scope) == None):
        var_table[scope] = {}
    if(p[-3] == scope or var_table[scope].get(p[-3]) != None):
        print("{0} already exists".format(p[-3]))
        #raise SyntaxError
    else:
        var_table[scope][p[-3]] = [p[-4]]
    #print("{0} {1} {2} {3} {4}".format(p[-4], p[-3], p[-2], p[-1], p[0]))

def p_change_scope(p):
    '''Change_Scope : '''
    sem.scope = p[-1]

def p_restore_scope(p):
    '''Restore_Scope : '''
    sem.scope = 'global'

# Empty production
def p_empty(p):
    '''empty : '''
    pass
    
# Error rules for productions
def p_program_err(p):
    '''Program : ASCII Program'''
def p_superexpr_error(p):
    '''SuperExpr : Expression error SuperExpr1'''
    print("Malformed expression")
    
def p_term_error(p):
    '''Term1 : DIVIDE error Term
             | TIMES error Term'''    
    
# Error rule for syntax errors
def p_error(p):
    try:
        print("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(input, p), p.value))
    except:
        print("Syntax error")
    lexer.push_state("err")
    while(True):
        tok = lexer.token()
        if(tok):
            if(tok.type != 'ASCII'):
                lexer.pop_state()
                yacc.errok()
                return(tok)
        else:
            print("Abrupt file termination")
            break    

# Build the parser
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    input = f.read()
    result = parser.parse(input,0,0)
    var_table = sem.var_table
    print result
    print "Scope\t|Id\t|Type"
    print "--------|-------|--------"
    for k in var_table:
        sys.stdout.write(k)
        for k1 in var_table[k]:
            print("\t|" + k1 + "\t|" + var_table[k][k1][0])
        print "--------|-------|--------"
    #print var_table