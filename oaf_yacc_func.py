import ply.yacc as yacc

# Get semantic variables
import oaf_sem as sem

# Parsing state module
import oaf_state as state

# Get tokens from the lexer
from oaf_lex import tokens
# Get the lexer
from oaf_lex import lexer
from oaf_lex import find_column

def p_program(p):
    '''Program : Declaration Function Main'''

def p_main(p):
    '''Main : MAIN LPAREN RPAREN FBlock'''
    
def p_declaration(p):
    '''Declaration : Primitive ID Declaration1
                   | empty'''
    
def p_declaration_1(p):
    '''Declaration1 : Array Array Seen_Variable SEMI Declaration
                    | LPAREN ParamList RPAREN Seen_Function RFBlock'''

def p_local_declaration(p):
    '''Local_Declaration : Primitive ID Array Array Seen_Variable SEMI Local_Declaration
                   | empty'''

def p_array(p):
    '''Array : LBRACKET ICONST RBRACKET
             | empty'''
    p[0] = p[1]

def p_function(p):
    '''Function : Function1
                | RFunction
                | empty'''

def p_function_1(p):
    '''Function1 : VOID ID LPAREN ParamList RPAREN Seen_Function FBlock Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID LPAREN ParamList RPAREN Seen_Function RFBlock Function'''

def p_block(p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fblock(p):
    '''FBlock : LBRACE Local_Declaration Instruction RBRACE'''

def p_rfblock(p):
    '''RFBlock : LBRACE Local_Declaration Instruction RETURN SuperExpr SEMI RBRACE'''

def p_conditional(p):
    '''Conditional : IF LPAREN SuperExpr RPAREN Block Else'''

def p_else(p):
    '''Else : ELSE Block
            | empty'''

def p_superexpr(p):
    '''SuperExpr : Expression SuperExpr1'''
    p[0] = p[1]

def p_superexpr_1(p):
    '''SuperExpr1 : AND SuperExpr
                  | OR SuperExpr
                  | empty'''

def p_expression(p):
    '''Expression : Expr Expression1'''
    p[0] = p[1]

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
    p[0] = p[1]

def p_expr_1(p):
    '''Expr1 : MINUS Expr
             | PLUS Expr
             | empty'''

def p_term(p):
    '''Term : Factor Term1'''
    p[0] = p[1]

def p_term_1(p):
    '''Term1 : DIVIDE Term
             | TIMES Term
             | empty'''

def p_factor(p):
    '''Factor : LPAREN SuperExpr RPAREN
              | Factor1'''
    p[0] = p[1]

def p_factor_1(p):
    '''Factor1 : Factor2
               | Factor3'''
    p[0] = p[1]

def p_factor_2(p):
    '''Factor2 : MINUS Factor3
               | PLUS Factor3'''
    p[0] = p[2]

def p_factor_3(p):
    '''Factor3 : Constant
               | Call'''
    p[0] = p[1]

# Agregar tipo STRING para variables y funciones
def p_params(p):
    '''Params : Params1
              | empty'''

def p_params_1(p):
    '''Params1 : SuperExpr Params2'''
    p[0] = p[1]

def p_params_2(p):
    '''Params2 : COMMA Params1
               | empty'''

def p_params_3(p):
    '''Params3 : SuperExpr Params4
               | STRING Params4'''
    p[0] = p[1]

def p_params_4(p):
    '''Params4 : COMMA Params3
               | empty'''

def p_loop(p):
    '''Loop : LOOP LPAREN SuperExpr RPAREN Block'''

def p_assign(p):
    '''Assign : ID EQUAL Assign1'''

def p_assign_1(p):
    '''Assign1 : SuperExpr
               | Call
               | STRING'''

def p_call(p):
    '''Call : ID LPAREN Params RPAREN'''
    p[0] = p[1]

def p_read(p):
    '''Read : READ LPAREN Type COMMA ID RPAREN'''

def p_type(p):
    '''Type : Primitive
            | STRING'''
    p[0] = p[1]

def p_print(p):
    '''Print : PRINT LPAREN Params3 RPAREN'''

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
    '''Param : Primitive ID Array1 Array1 Seen_Variable Update_Signature'''

def p_array_1(p):
    '''Array1 : LBRACKET RBRACKET
              | empty'''
    p[0] = p[1]

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

def p_instruction(p):
    '''Instruction : Instruction1 SEMI Instruction
                   | empty'''

def p_instruction_1(p):
    '''Instruction1 : Loop
                    | Conditional
                    | Assign
                    | Call
                    | Brush
                    | Read
                    | Print
                    | PenDown
                    | PenUp
                    | Home
                    | Forward
                    | Rotate
                    | Color
                    | Circle
                    | Arc
                    | Square'''

def p_constant(p):
    '''Constant : ID
                | FCONST
                | ICONST
                | CCONST
                | FALSE
                | TRUE'''
    p[0] = p[1]

# Function rules
def p_seen_function(p):
    '''Seen_Function : '''
    sem.fill_symbol_table_function(p[-4], [[p[-5]], state.signature])
    state.signature = []

def p_update_signature_size(p):
    '''Update_Signature : '''
    state.signature.append(p[-1])

# Update variable table
def p_seen_variable(p):
    '''Seen_Variable : '''
    type = p[-4]
    if(p[-2] != None):
        type += "[]"
    if(p[-1] != None):
        type += "[]"
    p[0] = type

# Empty production
def p_empty(p):
    '''empty : '''
    pass

# Error rules for productions
def p_program_error(p):
    '''Program : ASCII Program'''

def p_block_error(p):
    '''Block : LBRACE error RBRACE'''

def p_fblock_error(p):
    '''FBlock : LBRACE Local_Declaration error RBRACE'''

def p_rfblock_error(p):
    '''RFBlock : LBRACE Local_Declaration error RETURN SuperExpr SEMI RBRACE'''

def p_circle_error(p):
    '''Circle : CIRCLE LPAREN error RPAREN'''
    print("Missing parameter(s)")

def p_superexpr_error(p):
    '''SuperExpr : Expression error SuperExpr1'''
    print("Malformed expression")

def p_term_error(p):
    '''Term1 : DIVIDE error Term 
             | TIMES error Term'''
    print("Malformed expression")

# Error rule for syntax errors
def p_error(p):
    try:
        print("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(input, p), p.value))
    except:
        print("Preparser syntax error")
    lexer.push_state("err")
    #print(tok, p.type)
    #print(p)
    if(p):
        lexer.pop_state()
        if(p.type == 'SEMI'):
            print("in$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            while(True):
                tok = lexer.token()
                if(tok.type != 'ASCII'):
                    yacc.errok()
                    return(tok)
                else:
                    break
    else:
        print("Abrupt file termination")

# Build the parser
parser = yacc.yacc(tabmodule="preparser")