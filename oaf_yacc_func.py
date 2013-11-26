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
    '''Main : MAIN LPAREN RPAREN Seen_Main FBlock'''

def p_declaration(p):
    '''Declaration : Primitive ID Declaration1
                   | empty'''

def p_declaration_1(p):
    '''Declaration1 : Array SEMI Declaration
                    | LPAREN ParamList RPAREN Seen_Function FBlock'''

def p_local_declaration(p):
    '''Local_Declaration : Primitive ID Array SEMI Local_Declaration
                   | empty'''

def p_array(p):
    '''Array : LBRACKET ICONST RBRACKET Array
             | empty'''

def p_function(p):
    '''Function : Function1
                | RFunction
                | empty'''

def p_function_1(p):
    '''Function1 : VOID ID LPAREN ParamList RPAREN Seen_Function FBlock Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID LPAREN ParamList RPAREN Seen_Function FBlock Function'''

def p_block(p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fblock(p):
    '''FBlock : LBRACE Local_Declaration Instruction RBRACE'''

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
    '''Assign : ID Array2 EQUAL Assign1'''

def p_assign_1(p):
    '''Assign1 : SuperExpr
               | STRING'''

def p_array_2(p):
    '''Array2 : LBRACKET SuperExpr RBRACKET Array2
              | empty'''

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
    '''Brush : BRUSH LPAREN SuperExpr RPAREN'''

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
	'''Square : SQUARE LPAREN SuperExpr RPAREN '''

def p_param(p):
    '''Param : Primitive ID Array1 Update_Signature'''

def p_array_1(p):
    '''Array1 : LBRACKET RBRACKET Add_Dimension Array1
              | empty'''

def p_add_dimension(p):
    '''Add_Dimension : '''
    state.arr_dim_str += "[]"

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
                    | Square
                    | Return'''

def p_return(p):
    '''Return : RETURN RType'''

def p_rtype(p):
    '''RType : SuperExpr
             | empty'''

def p_constant(p):
    '''Constant : ID Array2
                | FCONST
                | ICONST
                | CCONST
                | FALSE
                | TRUE'''
    p[0] = p[1]

# Function rules
def p_seen_function(p):
    '''Seen_Function : '''
    sem.fill_symbol_table_function(p[-4], [[p[-5]], state.signature, state.f_param_list])
    state.f_param_list = []
    state.signature = []

def p_seen_main(p):
    '''Seen_Main : '''
    # Main has no signature, parameters, or return type
    sem.fill_symbol_table_function(p[-3], [[], [], [], [], 0])

def p_update_signature_size(p):
    '''Update_Signature : '''
    state.signature.append(p[-3] + state.arr_dim_str)
    state.f_param_list.append(p[-2])
    state.arr_dim_str = ""

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
    if(p):
        raise NameError("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(lexer.lexdata, p), p.value))
    else:
        raise NameError("Abrupt file termination")

# Build the parser
parser = yacc.yacc(tabmodule="preparser")