import ply.yacc as yacc 
import oaf_vm as vm

# Module to serialize objects
import cPickle as pickle

# Funcions preparser
import oaf_yacc_func as func_parser

#he hash table to pass to the 
#import oaf_data_to_vm as vm

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
    '''Main : MAIN Seen_Main Push_Scope LPAREN RPAREN FBlock'''

def p_declaration(p):
    '''Declaration : Primitive ID Declaration1
                   | empty'''

def p_declaration_1(p):
    '''Declaration1 : Array Array Seen_Global_Variable SEMI Declaration
                    | Seen_Return_Function Push_Scope LPAREN ParamList RPAREN FBlock Seen_Return_Function_End Pop_Scope'''

def p_local_declaration(p):
    '''Local_Declaration : Primitive ID Array Array Seen_Local_Variable Update_Signature_Size SEMI Local_Declaration
                         | empty'''

def p_array(p):
    '''Array : Array1
             | empty'''
    p[0] = p[1]

def p_array_1(p):
    '''Array1 : LBRACKET ICONST RBRACKET'''
    p[0] = p[2]

def p_function(p):
    '''Function : Function1
                | RFunction
                | empty'''

def p_function_1(p):
    '''Function1 : VOID ID Seen_Function Push_Scope LPAREN ParamList RPAREN FBlock Seen_Function_End Pop_Scope Function'''

def p_rfunction(p):
    '''RFunction : Primitive ID Seen_Return_Function Push_Scope LPAREN ParamList RPAREN FBlock Seen_Return_Function_End Pop_Scope Function'''

def p_block(p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fblock(p):
    '''FBlock : LBRACE Local_Declaration Instruction RBRACE'''

def p_conditional(p):
    '''Conditional : IF LPAREN SuperExpr RPAREN Push_Label_Stack Block Else'''

def p_push_label_stack(p):
    '''Push_Label_Stack : '''
    state.label_stack.append(len(state.quads))
    il.generate_if_goto_f(state.operand_stack.pop())

def p_pop_label_stack(p):
    '''Pop_Label_Stack : '''
    il.put_label_to_goto_f(state.label_stack.pop())

def p_else(p):
    '''Else : ELSE Push_Else Pop_Label_Stack Block Pop_Label_Stack
            | Pop_Label_Stack empty'''  

def p_push_else(p):
    '''Push_Else : '''
    temp = state.label_stack.pop()
    il.generate_else_goto()
    state.label_stack.append(len(state.quads) - 1)
    state.label_stack.append(temp)

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
    '''Factor2 : MINUS Seen_Unary_Operator Factor3 Gen_Quad0
               | PLUS Seen_Unary_Operator Factor3 Gen_Quad0'''
    p[0] = p[3]

def p_factor_3(p):
    '''Factor3 : Constant
               | Call'''
    p[0] = p[1]
    if(p[0] == "uno"):
        pass
    if(p[0] == 7):
        pass

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
#
# revisar este pedo


def p_loop(p):
    '''Loop : LOOP LPAREN Save_Label SuperExpr RPAREN Push_Label_Stack Block Go_Back_To_Validate Pop_Label_Stack'''

def p_save_label(p):
    '''Save_Label : '''
    state.label_stack.append(len(state.quads) - 1)

def p_go_back_to_validate(p):
    '''Go_Back_To_Validate :'''
    temp = state.label_stack.pop()
    il.generate_loop_goto(state.label_stack.pop())
    state.label_stack.append(temp)


def p_assign(p):
    '''Assign : ID Seen_Operand EQUAL Seen_Operator Assign1'''

def p_assign_1(p):
    '''Assign1 : SuperExpr Gen_Quad5
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
    '''Param : Primitive ID Array2 Array2 Seen_Local_Variable Update_Signature_Size'''

def p_array_2(p):
    '''Array2 : LBRACKET RBRACKET
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
    p[0] = p[1]

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
    p[0] = p[1] 

def p_return(p):
    '''Return : RETURN RType '''
    #print state.operand_stack[-1][1][0]
    return_var = state.operand_stack.pop()
    func.generate_return(return_var)
    if(p[2] != None):
        sem.validate_return_funtion(return_var[1][0])
    else:
        sem.validate_return_funtion("void")
def p_rtype(p):
    '''RType : SuperExpr
             | empty'''
    p[0] = p[1]


def p_constant(p):
    '''Constant : ID
                | FCONST Seen_Float
                | ICONST Seen_Int
                | CCONST Seen_Char
                | Constant1 Seen_Bool'''
    p[0] = p[1]

def p_constant_1(p):
    '''Constant1 : TRUE
                 | FALSE'''
    p[0] = p[1]

def p_seen_char_operand(p):
    '''Seen_Char_Operand :'''
    expr.add_operand(p[-2])


def p_seen_call(p):
    '''Seen_Call : '''
    expr.add_operator("#")
    state.return_dir_stack.append(state.temp_dir)
    func_name = p[-2]
    type = sem.func_table[func_name][0][0]  # [[primitive, dir, size, scope], dir, size]
    if(type != "void"):  # Function has a return value
        if(type[0] == "i" or type[0] == "f"):
            size = 4
        else:
            size = 1
        # Creates a temporal to save return value
        func.generate_era(func_name, [func_name, [type, state.temp_dir, size, 't']])
        state.temp_dir -= size
    else:
        func.generate_era(func_name, None)

def p_seen_call_end(p):
    '''Seen_Call_End : '''
    expr.pop_operator()
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
    state.local_dir = 0
    sem.func_table[p[-1]].append(len(state.quads))

def p_seen_function_end(p):
    '''Seen_Function_End : '''
    func_name = p[-7]
    func.generate_end(func_name)
    sem.func_table[func_name].append(state.f_size)
    state.f_size = 0

def p_seen_return_function(p):
    '''Seen_Return_Function : '''
    state.local_dir = 0
    #state.return_dir_stack.append(state.temp_dir)
    sem.func_table[p[-1]].append(len(state.quads))

def p_seen_return_function_end(p):
    '''Seen_Return_Function_End : '''
    func_name = p[-7]
    #return_var = state.operand_stack.pop()
    #func.generate_return(func_name, return_var)
    func.generate_end(func_name)
    sem.func_table[func_name].append(state.f_size)
    #sem.func_table[func_name][0] = return_var[1]
    #state.return_dir_stack.pop()
    #state.return_var_stack.pop()
    state.f_size = 0

def p_seen_program(p):
    '''Seen_Program : '''
    main.generate_main()

def p_seen_program_end(p):
    '''Seen_Program_End : '''
    func.generate_end("main")

def p_seen_main(p):
    '''Seen_Main : '''
    state.local_dir = 0
    main.update_goto(len(state.quads))

def p_update_signature_size(p):
    '''Update_Signature_Size : '''
    d1 = 1
    d2 = 1
    if(p[-3] != None):
        d1 = p[-3]
    if(p[-2] != None):
        d2 = p[-2]
    type = p[-1]
    if(type[0] == "i" or type[0] == "f"):
        state.f_size += 4 * d1 * d2
    else:
        state.f_size += 1 * d1 * d2

def p_check_signature(p):
    '''Check_Signature : '''
    sem.is_signature_valid(p[-5], state.signature)

# Math rules
def p_seen_operand(p):
    '''Seen_Operand : '''
    if(sem.is_declared(p[-1])):
        expr.add_operand(sem.get_variable(p[-1]))

def p_seen_unary_operator(p):
    '''Seen_Unary_Operator : '''
    expr.add_operator("u" + str(p[-1]))
    p[0] = p[-1]

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
    expr.generate_quad(0)

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
def p_seen_global_variable(p):
    '''Seen_Global_Variable : '''
    type = p[-4]
    d1 = 1
    d2 = 1
    if(p[-2] != None):
        type += "[]"
        d1 = p[-2]
    if(p[-1] != None):
        type += "[]"
        d2 = p[-2]
    if(type[0] == "i" or type[0] == "f"):
        size = 4
    else:
        size = 1
    sem.fill_global_variables_table(p[-3], type, d1 * d2 * size)
    p[0] = type

def p_seen_local_variable(p):
    '''Seen_Local_Variable : '''
    type = p[-4]
    d1 = 1
    d2 = 1
    if(p[-2] != None):
        type += "[]"
        d1 = p[-2]
    if(p[-1] != None):
        type += "[]"
        d2 = p[-2]
    if(type[0] == "i" or type[0] == "f"):
        size = 4
    else:
        size = 1
    sem.fill_local_variables_table(p[-3], type, d1 * d2 * size)
    p[0] = type

def p_seen_float(p):
    '''Seen_Float : '''
    sem.fill_symbol_table_constant(p[-1], "float", 4)

def p_seen_int(p):
    '''Seen_Int : '''
    sem.fill_symbol_table_constant(p[-1], "int", 4)

def p_seen_char(p):
    '''Seen_Char : '''
    sem.fill_symbol_table_constant(p[-1], "char", 1)

def p_seen_bool(p):
    '''Seen_Bool : '''
    sem.fill_symbol_table_constant(p[-1], "bool", 1)

def p_seen_semi(p):
    '''Seen_Semi : '''
    pass
    #state.clear_stacks()

def p_push_scope(p):
    '''Push_Scope : '''
    sem.scope = p[-2]
    sem.validate_redeclaration_function(p[-2])
    #state.address_stack.append([state.global_dir, state.constant_dir, state.local_dir, state.temp_dir])
    state.temp_counter = 0
    state.temp_dir = 0

def p_pop_scope(p):
    '''Pop_Scope : '''
    sem.scope = "global"
    #addresses = state.address_stack.pop()
    #state.global_dir = addresses[0]
    #state.constant_dir = addresses[1]
    #state.local_dir = addresses[2]
    #state.temp_dir = addresses[3]

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
f_parser = func_parser.parser
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    input = f.read()
    preparsing = f_parser.parse(input, 0, 0)
    result = parser.parse(input, 0, 0)
    var_table = sem.var_table
    for idx, quad in enumerate(state.quads):
        print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

def add_offset(lst, g_offset, c_offset, l_offset):
    if(lst[3] == 'g'):
        lst[1] += g_offset
    elif(lst[3] == 'c'):
        lst[1] += c_offset
    else:
        lst[1] += l_offset

# Adds offset to global, local and constant variables
state.c_offset += state.global_dir  # Adds the count of global variables to constants
state.l_offset += state.global_dir + state.constant_dir  # Adds the count of global and constant variables to locals
for okey in sem.var_table:
    for ikey in sem.var_table[okey].items():
        add_offset(ikey[1], state.g_offset, state.c_offset, state.l_offset)

# Pass the starting stack address to the VM as the biggest function size plus the global and constant variables
func_max_size = max(map(lambda x: x[1][3], sem.func_table.items()))
main_size = sum(map(lambda x: x[1][2], var_table["main"].items()))
state.stack_dir += state.global_dir + state.constant_dir + max(func_max_size, main_size)
#stack_dir = 0
#for var in sem.var_table[sem.global_str].items():
#    stack_dir += var[1][2]
#for var in sem.var_table[sem.constant_str].items():
#    stack_dir += var[1][2]

# Appends memory map to functions
for func_name in sem.func_table:
    if(sem.var_table.get(func_name) != None and sem.var_table[func_name] != None):
        sem.func_table[func_name].append(sorted(map(lambda x: [x[1][1], x[0]], sem.var_table[func_name].items())))

# Changes variables to memory addresses and adds temporal address offset
for idx, quad in enumerate(state.quads):
    quad.transform(state.t_offset)
    #quad.add_offset(0, state.global_dir, 9000, 43000)
    print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

#for e in sem.var_table[sem.constant_str].items():
#    e[1][1] += state.global_dir
#    for idx, quad in enumerate(state.quads):
#        quad.transform()
#        #quad.add_offset(0, state.global_dir, 9000, 43000)
#        print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

# Sorting function
def swap(element):
    return element[1][1], element[0]

with open("o.af", "wb") as out:
    obj = {
        "quads": state.quads,
        "functions": sem.func_table,
        "mem": dict(map(swap, sem.var_table[sem.constant_str].items()) + map(swap, sem.var_table[sem.global_str].items()))
    }
    pickle.dump(obj, out, -1)

machine = vm.VirtualMachine("o.af", state.l_offset, state.stack_dir)
machine.run()

#target.write(str(vm.vm))