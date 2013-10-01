import ply.yacc as yacc

# Get tokens from the lexer
from oaf_lex import tokens

# Variables table
var_table = {"global":{}}

def p_program(p):
    '''Program : Declaration Function Main'''
    
def p_main(p):
    '''Main : MAIN LPAREN RPAREN FBlock'''

def p_declaration(p):
    '''Declaration : Primitive ID Array Array SEMI Declaration
                   | empty'''

def p_array(p):
    '''Array : LBRACKET ICONST RBRACKET
             | empty'''

def p_function(p):
    '''Function : Function1
                | RFunction
                | empty'''

def p_function_1(p):
    '''Function1 : VOID ID LPAREN ParamList RPAREN FBlock Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID LPAREN ParamList RPAREN RFBlock Function'''

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
    '''Param : Primitive Array1 Array1 ID'''

def p_array_1(p):
    '''Array1 : LBRACKET RBRACKET
              | empty'''

def p_primitive(p):
    '''Primitive : INT
                 | FLOAT
                 | BOOL
                 | CHAR'''

def p_paramlist(p):
    '''ParamList : Param ParamList1'''

def p_paramlist_1(p):
    '''ParamList1 : COMMA ParamList
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

# Empty production
def p_empty(p):
    '''empty : '''
    pass
    
# Error rule for syntax errors
def p_error(p):
    try:
        print "Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, p.lexpos, p.value)
    except:
        pass
        
# Build the parser
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    result = parser.parse(f.read())
    print result