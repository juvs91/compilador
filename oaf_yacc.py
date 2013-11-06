import ply.yacc as yacc 

#he hash table to pass to the 
import oaf_data_to_vm as vm

# debug
import sys

import oaf_state as state

import oaf_main as main

# Expressions module
import oaf_expr as expr
# Functions module
import oaf_func as func

#read write module
import oaf_read_write as rw  

#if while module
import oaf_if_loop as il

# Get semantic variables
import oaf_sem as sem

# Get tokens from the lexer
from oaf_lex import tokens
# Get the lexer
from oaf_lex import lexer
from oaf_lex import find_column

def p_program(p):
    '''Program : Seen_Program Declaration Function Main Seen_Program_End'''

def p_main(p):
    '''Main : MAIN Push_Scope Seen_Main LPAREN RPAREN FBlock'''

def p_declaration(p):
    '''Declaration : Primitive ID Array Array Seen_Variable SEMI Declaration
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
    '''Function1 : VOID ID Push_Scope LPAREN ParamList RPAREN Seen_Function FBlock Seen_Function_End Pop_Scope Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID Push_Scope LPAREN ParamList RPAREN Seen_Function RFBlock Seen_Function_End Pop_Scope Function'''

def p_block(p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fblock(p):
    '''FBlock : LBRACE Declaration Instruction RBRACE'''

def p_rfblock(p):
    '''RFBlock : LBRACE Declaration Instruction RETURN SuperExpr SEMI RBRACE'''

def p_conditional(p):
    '''Conditional : IF LPAREN SuperExpr RPAREN Push_Label_Stack Block Else'''

def p_push_label_stack(p):
    '''Push_Label_Stack : '''
    state.label_stack.append(len(state.quads))
    il.generate_if_goto_F(state.operand_stack.pop())

def p_pop_label_stack(p):
    '''Pop_Label_Stack : '''
    il.put_label_to_goto_F(state.label_stack.pop())

def p_else(p):
    '''Else : ELSE Push_Else Pop_Label_Stack Block Pop_Label_Stack
            | Pop_Label_Stack empty'''  

def p_push_else(p):
    '''Push_Else : '''
    temp = state.label_stack.pop()
    state.label_stack.append(len(state.quads))
    state.label_stack.append(temp)
    il.generate_else_goto()

def p_superexpr(p):
    '''SuperExpr : Expression Gen_Quad4 SuperExpr1'''
    p[0] = p[1]

def p_superexpr_1(p):
    '''SuperExpr1 : AND Seen_Operator SuperExpr
                  | OR Seen_Operator SuperExpr
                  | empty'''

def p_expression(p):
    '''Expression : Expr Expression1 Gen_Quad3'''
    p[0] = p[1]

def p_expression_1(p):
    '''Expression1 : LESSTHAN Seen_Operator Expr
                   | GREATHAN Seen_Operator Expr
                   | DIFFERENT Seen_Operator Expr
                   | TWOEQUAL Seen_Operator Expr
                   | GREATEQUAL Seen_Operator Expr
                   | LESSEQUAL Seen_Operator Expr
                   | empty'''

def p_expr(p):
    '''Expr : Term Gen_Quad2 Expr1'''
    p[0] = p[1]

def p_expr_1(p):
    '''Expr1 : MINUS Seen_Operator Expr
             | PLUS Seen_Operator Expr
             | empty'''

def p_term(p):
    '''Term : Factor Gen_Quad1 Term1'''
    p[0] = p[1]

def p_term_1(p):
    '''Term1 : DIVIDE Seen_Operator Term
             | TIMES Seen_Operator Term
             | empty'''

def p_factor(p):
    '''Factor : LPAREN Push_Expr SuperExpr RPAREN Pop_Expr
              | Factor1 Seen_Operand'''
    p[0] = p[1]

def p_factor_1(p):
    '''Factor1 : Factor2
               | Factor3'''
    p[0] = p[1]

def p_factor_2(p):
    '''Factor2 : MINUS Factor3 Gen_Quad0
               | PLUS Factor3 Gen_Quad0'''
    p[0] = p[2]

def p_factor_3(p):
    '''Factor3 : Constant
               | Call'''
    p[0] = p[1]

# revisar este pedo
# Agregar tipo STRING para variables y funciones
def p_params(p):
    '''Params : Params1
              | empty'''

def p_params_1(p):
    '''Params1 : SuperExpr Seen_Param_Call Params2'''
    p[0] = p[1]

def p_params_2(p):
    '''Params2 : COMMA Params1
               | empty'''

def p_params_3(p):
    '''Params3 : SuperExpr Seen_Param_Print Params4
               | STRING Seen_Param_Print Params4'''
    p[0] = p[1]

def p_params_4(p):
    '''Params4 : COMMA Params3
               | empty'''

def p_push_param_list(p):
    '''Push_Param_List : '''
    state.params_list.append(p[-1])
#
# revisar este pedo


def p_loop(p):
    '''Loop : LOOP LPAREN Save_Label SuperExpr RPAREN Push_Label_Stack Block Go_Back_To_Validate Pop_Label_Stack'''

def p_save_label(p):
    '''Save_Label : '''
    state.label_stack.append(len(state.quads))

def p_go_back_to_validate(p):
    '''Go_Back_To_Validate :'''
    temp = state.label_stack.pop()
    il.generate_loop_goto(state.label_stack.pop())
    state.label_stack.append(temp)


def p_assign(p):
    '''Assign : ID Seen_Operand EQUAL Seen_Operator Assign1'''

def p_assign_1(p):
    '''Assign1 : SuperExpr Gen_Quad5
               | Call
               | STRING Check_Char Seen_Char_Operand Gen_Quad5'''

def p_check_char(p):
    '''Check_Char : '''
    sem.is_char(p[-1])


def p_call(p):
    '''Call : ID LPAREN Seen_Call Params RPAREN Check_Signature Seen_Call_End'''
    p[0] = p[1]

def p_read(p):
    '''Read : READ LPAREN Type COMMA ID Generate_Read RPAREN'''

def p_generate_read(p):
    '''Generate_Read : '''
    rw.read_quad(p[-3], p[-1], sem.scope)

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
    '''Param : Primitive ID Array1 Array1 Seen_Variable Update_Signature_Size'''

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
    '''Instruction : Instruction1 SEMI Seen_Semi Instruction
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
                | FCONST Seen_Float
                | ICONST Seen_Int
                | CCONST Seen_Char
                | FALSE
                | TRUE'''
    p[0] = p[1]

def p_seen_char_operand(p):
    '''Seen_Char_Operand :'''
    expr.add_operand(p[-2])
    print "CHAR"

def p_seen_call(p):
    '''Seen_Call : '''
    func.generate_era(p[-2])

def p_seen_call_end(p):
    '''Seen_Call_End : '''
    func.generate_gosub(p[-6])
    state.reset_call()

def p_seen_param_call(p):
    '''Seen_Param_Call : '''
    param = state.operand_stack.pop()
    func.generate_param(param)
    state.signature.append(param[1][0])

def p_seen_param_print(p):
    '''Seen_Param_Print : '''
    if(p[-1][0] == '"'):
        param = p[-1]
    else:
        param = state.operand_stack.pop()
    rw.print_quad(param)

# Function rules
def p_seen_function(p):
    '''Seen_Function : '''
    sem.fill_symbol_table_function(p[-5], [p[-6], state.signature, state.f_size])
    state.signature = []
    state.f_size = 0

def p_seen_function_end(p):
    '''Seen_Function_End : '''
    func.generate_end(p[-7])

def p_seen_program(p):
    '''Seen_Program : '''
    main.generate_main()

def p_seen_program_end(p):
    '''Seen_Program_End : '''
    func.generate_end("main")

def p_seen_main(p):
    '''Seen_Main : '''
    main.update_goto(len(state.quads) + 1)

def p_update_signature_size(p):
    '''Update_Signature_Size : '''
    state.signature.append(p[-1])
    if(p[-1][0] == "i" or p[-1][0] == "f"):
        state.f_size += 4
    else:
        state.f_size += 1

def p_check_signature(p):
    '''Check_Signature : '''
    sem.is_signature_valid(p[-5], state.signature)

# Math rules
def p_seen_operand(p):
    '''Seen_Operand : '''
    if(sem.is_declared(p[-1])):
        expr.add_operand(sem.get_variable(p[-1]))

def p_seen_operator(p):
    '''Seen_Operator : '''
    expr.add_operator(p[-1])
    p[0] = p[-1]

def p_push_expr(p):
    '''Push_Expr : '''
    expr.push_expr()

def p_pop_expr(p):
    '''Pop_Expr : '''
    expr.pop_expr()

# Unary operators
def p_gen_quad_0(p):
    '''Gen_Quad0 : '''

# *, /
def p_gen_quad_1(p):
    '''Gen_Quad1 : '''
    expr.generate_quad(1)

# +, -
def p_gen_quad_2(p):
    '''Gen_Quad2 : '''
    expr.generate_quad(2)

# Logical operators
def p_gen_quad_3(p):
    '''Gen_Quad3 : '''
    expr.generate_quad(3)

# &&, ||
def p_gen_quad_4(p):
    '''Gen_Quad4 : '''
    expr.generate_quad(4)

# Assign
def p_gen_quad_5(p):
    '''Gen_Quad5 : '''
    expr.generate_quad(5)

# Update variable table
def p_seen_variable(p):
    '''Seen_Variable : '''
    type = p[-4]
    if(p[-2] != None):
        type += "[]"
    if(p[-1] != None):
        type += "[]"
    sem.fill_symbol_table_variable(p[-3], type)
    p[0] = type

def p_seen_float(p):
    '''Seen_Float : '''
    sem.fill_symbol_table_constant(p[-1], "float")

def p_seen_int(p):
    '''Seen_Int : '''
    sem.fill_symbol_table_constant(p[-1], "int")

def p_seen_char(p):
    '''Seen_Char : '''
    sem.fill_symbol_table_constant(p[-1], "char")

def p_seen_semi(p):
    '''Seen_Semi : '''
    pass
    #state.clear_stacks()

def p_push_scope(p):
    '''Push_Scope : '''
    sem.scope = p[-1]
    sem.validate_redeclaration_function(p[-1])

def p_pop_scope(p):
    '''Pop_Scope : '''
    sem.scope = "global"

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
    '''FBlock : LBRACE Declaration error RBRACE'''

def p_rfblock_error(p):
    '''RFBlock : LBRACE Declaration error RETURN SuperExpr SEMI RBRACE'''

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
        print("Syntax error")
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
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    input = f.read()
    result = parser.parse(input,0,0)
    var_table = sem.var_table
    #print result
    #for idx, quad in enumerate(state.quads):
        #print idx + 1, (quad.operator, quad.operand1, quad.operand2, quad.result)
       # print "Scope\t|Id\t|Type"
       # print "--------|-------|--------"
       # for k in var_table:
       #     sys.stdout.write(k)
       #     for k1 in var_table[k]:
       #         print("\t|" + str(k1) + "\t|" + var_table[k][k1][0])
       #     print "--------|-------|--------"                          
i = 1        
for e in state.quads:
	vm.vm["quads"][i]=str(i) + "("+ str(e.operator) + " " +  str(e.operand1) + " " +str(e.operand2) + " " + str(e.result) + ")"
	i += 1  
#for e in sem.func_table
vm.vm["functions"] = sem.func_table 

vm.vm["constants"] = sem.var_table[sem.constant_str] 

target = open("object.txt", 'a+')

target.write(str(vm.vm))
