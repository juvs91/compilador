import ply.yacc as yacc 
import oaf_vm as vm

# Module to serialize objects
import cPickle as pickle

# Functions preparser
import oaf_yacc_func as func_parser

import oaf_state as state

import oaf_main as main      


#all the grafic quads
import oaf_grafic_quads as gq

# Expressions module
import oaf_expr as expr
# Functions module
import oaf_func as func
# Arrays module
import oaf_array as arr

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
    '''Declaration1 : Array Seen_Array Seen_Global_Variable SEMI Declaration
                    | Seen_Return_Function Push_Scope LPAREN ParamList RPAREN FBlock Seen_Return_Function_End Pop_Scope'''

def p_local_declaration(p):
    '''Local_Declaration : Primitive ID Array Seen_Array Seen_Local_Variable SEMI Local_Declaration
                         | empty'''

def p_array(p):
    '''Array : LBRACKET ICONST Seen_Int RBRACKET Seen_Dimension Array
             | empty'''

def p_seen_array(p):
    '''Seen_Array : '''
    for dim in state.arr_dim:
        mn = state.arr_r / dim
        state.arr_m_list.append(mn)
        state.arr_r = mn

def p_seen_dimension(p):
    '''Seen_Dimension : '''
    state.arr_dim.append(p[-3])
    state.arr_r *= p[-3]

def p_seen_dimension_1(p):
    '''Seen_Dimension1 : '''
    state.arr_dim.append(p[-2])

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
              | Constant Seen_Operand
              | Factor1'''
    p[0] = p[1]

#def p_factor_1(p):
#    '''Factor1 : Factor2
#               | Constant'''
#    p[0] = p[1]

def p_factor_1(p):
    '''Factor1 : MINUS Seen_Unary_Operator Constant Seen_Operand Gen_Quad0
               | PLUS Seen_Unary_Operator Constant Seen_Operand Gen_Quad0'''
    p[0] = p[3]

def p_constant(p):
    '''Constant : ID Constant1
                | FCONST Seen_Float
                | ICONST Seen_Int
                | CCONST Seen_Char
                | Constant2 Seen_Bool'''
    p[0] = p[1]

def p_constant_1(p):
    '''Constant1 : Array2
                 | Call'''
    p[0] = p[1]

def p_constant_2(p):
    '''Constant2 : TRUE
                 | FALSE'''
    p[0] = p[1]

def p_params(p):
    '''Params : Params1
              | empty'''

def p_params_1(p):
    '''Params1 : SuperExpr Seen_Param_Call Clear_Dimensions Params2'''
    p[0] = p[1]

def p_params_2(p):
    '''Params2 : COMMA Params1
               | empty'''

def p_params_3(p):
    '''Params3 : SuperExpr Seen_Param_Print Clear_Dimensions Params4
               | STRING Seen_Param_Print Clear_Dimensions Params4'''
    p[0] = p[1]

def p_params_4(p):
    '''Params4 : COMMA Params3
               | empty'''

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

def p_call_assign(p):
    '''Call_Assign : ID Call_Assign1'''
    p[0] = p[1]

def p_call_assign_1(p):
    '''Call_Assign1 : Assign
                    | Call'''
    p[0] = p[-1]

def p_assign(p):
    '''Assign : Clear_Assign Assign1 Check_Assign'''
    p[0] = p[-1]

def p_assign_1(p):
    '''Assign1 : Array2 Seen_Operand1 EQUAL Seen_Operator Assign2 Clear_Dimensions'''

def p_assign_2(p):
    '''Assign2 : SuperExpr Gen_Quad5
               | STRING Check_Char Seen_Char_Operand Gen_Quad5'''

def p_array_2(p):
    '''Array2 : Clear_Current_Dimension Array3 Update_Offset Generate_Dir
              | empty'''

def p_array_3(p):
    '''Array3 : LBRACKET SuperExpr RBRACKET Verify_Limit Array4'''
    p[0] = p[-1]

def p_array_4(p):
    '''Array4 : LBRACKET SuperExpr RBRACKET Verify_Limit Array4
              | empty'''

def p_clear_dimensions(p):
    '''Clear_Dimensions : '''
    state.arr_current_dim = 0
    state.arr_dim_stack = []

def p_clear_current_dimension(p):
    '''Clear_Current_Dimension : '''
    expr.add_operator("#")
    state.arr_current_dim = 0
    p[0] = p[-1]

def p_clear_assign(p):
    '''Clear_Assign : '''
    state.assign_list = []
    state.arr_current_dim = 0
    state.arr_dim_stack = []
    p[0] = p[-1]

def p_check_assign(p):
    '''Check_Assign : '''
    if(not all(e == state.assign_list[0] for e in state.assign_list)):
        raise NameError("Incompatible assignment type.")
    state.assign_list = []

def p_update_offset(p):
    '''Update_Offset : '''
    var = sem.get_variable(p[-2])
    type = var[1][0]
    expr.add_operator("#")
    for x in range(state.arr_current_dim - 1):
        expr.add_operator("+")
        expr.generate_quad(2)  # Generates quads to sum all the indices
    if(type[0] == "i" or type[0] == "f"):
        sem.fill_symbol_table_constant(4, "int", 4)
        expr.add_operand(sem.get_variable(4))
        expr.add_operator("*")
        expr.generate_quad(1)
    expr.pop_operator()

def p_generate_dir(p):
    '''Generate_Dir : '''
    var = sem.get_variable(p[-3])
    # If size is zero variable is unresolved
    if(var[1][2][0] <= 0):
        state.unresolved_vars[sem.scope][var[0]].append(len(state.quads))
    arr.generate_dir(var[1][1], var[1][3])  # Starting address, scope
    state.assign_list.append(var[1][0][:-2 * state.arr_current_dim])
    state.arr_dim_stack.append(state.arr_current_dim)
    expr.pop_operator()

def p_verify_limit(p):
    '''Verify_Limit : '''
    state.arr_current_dim += 1  # First position holds the array size in bytes
    index = state.operand_stack.pop()
    var = sem.get_variable(p[-4])

    if(var[1][2][0] <= 0):
        if(state.unresolved_vars.get(sem.scope) == None):
            state.unresolved_vars[sem.scope] = {}
        if(state.unresolved_vars[sem.scope].get(var[0]) == None):
            state.unresolved_vars[sem.scope][var[0]] = []
        state.unresolved_vars[sem.scope][var[0]].append(len(state.quads))

    arr.generate_verify(index, var[1][2][state.arr_current_dim] - 1)  # Gets dimension limits
    arr.generate_multiply_m(index, var[1][4][state.arr_current_dim - 1])  # Gets mn

    p[0] = p[-4]

def p_check_char(p):
    '''Check_Char : '''
    sem.is_char(p[-1])


def p_call(p):
    '''Call : LPAREN Seen_Call Params RPAREN Check_Signature Seen_Call_End'''
    p[0] = p[1]

def p_read(p):
    '''Read : READ LPAREN Type COMMA ID Generate_Read RPAREN'''

def p_generate_read(p):
    '''Generate_Read : '''
    rw.read_quad(p[-3], sem.get_variable(p[-1]))

def p_type(p):
    '''Type : Primitive
            | STRING'''
    p[0] = p[1]

def p_print(p):
    '''Print : PRINT LPAREN Params3 RPAREN'''

def p_brush(p):
    '''Brush : BRUSH LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr'''


def p_color(p):
    '''Color : COLOR LPAREN SuperExpr COMMA SuperExpr COMMA SuperExpr RPAREN Seen_Color'''

def p_seen_color(p):
    '''Seen_Color : '''
    blue = state.operand_stack.pop()
    green = state.operand_stack.pop()
    red = state.operand_stack.pop()
    gq.generate_color_quad(red,green,blue)

def p_pendown(p):
    '''PenDown : PD LPAREN RPAREN Pen_Home'''

def p_penup(p):
    '''PenUp : PU LPAREN RPAREN Pen_Home'''  

def p_pen_home(p):
    '''Pen_Home : '''
    gq.generate_pen_home_quad(p[-3])

def p_home(p):
    '''Home : HOME LPAREN RPAREN Pen_Home'''

def p_forward(p):
    '''Forward : FD LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr'''

def p_seen_grafic_operation_requieres_name_expr(p):
    '''Seen_grafic_operation_requieres_name_expr :'''
    gq.generate_draw_quad(p[-4],state.operand_stack.pop())

def p_rotate(p):
    '''Rotate : RT LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr'''


def p_circle(p):
    '''Circle : CIRCLE LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr'''


def p_arc(p):
    '''Arc : ARC LPAREN SuperExpr COMMA SuperExpr RPAREN Seen_Arc'''  

def p_speed(p):
	'''Speed : SPEED LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr ''' 
	
def p_triangle(p):
	'''Triangle : TRIANGLE LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr ''' 
	print "en el triangulo"

def p_seen_arc(p):
    '''Seen_Arc : '''
    p2 = state.operand_stack.pop()
    p1 = state.operand_stack.pop()
    gq.generate_arc_quad(p1,p2)


def p_square(p):
    '''Square : SQUARE LPAREN SuperExpr RPAREN Seen_grafic_operation_requieres_name_expr'''

def p_param(p):
    '''Param : Primitive ID Array1 Seen_Local_Variable1'''

def p_array_1(p):
    '''Array1 : LBRACKET RBRACKET Seen_Dimension1 Array1
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
    p[0] = p[1]

def p_instruction_1(p):
    '''Instruction1 : Loop
                    | Conditional
                    | Call_Assign
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
                    | Triangle
                    | Speed
                    | Return'''
    p[0] = p[1] 

def p_return(p):
    '''Return : RETURN RType '''
    if(p[2] != None):
        return_var = state.operand_stack.pop()
        func.generate_return(return_var)
        sem.validate_return_funtion(return_var[1][0])
    else:
        func.generate_return(None)
        sem.validate_return_funtion("void")
    #if(p[2] != None):
    #    sem.validate_return_funtion(return_var[1][0])
    #else:
    #    sem.validate_return_funtion("void")

def p_rtype(p):
    '''RType : SuperExpr
             | empty'''
    p[0] = p[1]

def p_seen_char_operand(p):
    '''Seen_Char_Operand :'''
    expr.add_operand(p[-2])

def p_seen_call(p):
    '''Seen_Call : '''
    expr.add_operator("#")
    state.return_dir_stack.append(state.temp_dir)
    func_name = p[-2]
    state.current_call = func_name
    type = sem.func_table[func_name][0][0]  # [[primitive, dir, size, scope], dir, size]
    if(type != "void"):  # Function has a return value
        if(type[0] == "i" or type[0] == "f"):
            size = 4
        else:
            size = 1
        # Creates a temporal to save return value
        func.generate_era(func_name, [func_name, [type, state.temp_dir, [size, 1], 't']])
        state.temp_dir -= size
    else:
        func.generate_era(func_name, None)

def p_seen_call_end(p):
    '''Seen_Call_End : '''
    expr.pop_operator()
    func_name = p[-6]
    func.generate_gosub(func_name, sem.get_function(func_name)[3])
    state.reset_call()

def p_seen_param_call(p):
    '''Seen_Param_Call : '''
    param = state.operand_stack.pop()
    var = sem.get_variable(p[-1])
    type = var[1][0]
    # Check if it's a dimentional parameter
    if("[]" in type and "[]" in sem.func_table[state.current_call][1][state.param_counter]):  # Checks if the parameter is an array
        arg = sem.func_table[state.current_call][2][state.param_counter]  # Gets variable to replace
        dir = max(map(lambda x: x[1][1] + x[1][2][0], sem.var_table[state.current_call].items()))  # Gets the last available address
        sem.var_table[state.current_call][arg][1] = dir  # Updates the starting address
        sem.var_table[state.current_call][arg][2] = [var[1][2][0] / max(sum(var[1][2][1:state.arr_current_dim + 1]), 1)] + var[1][2][state.arr_current_dim + 1:]  # Updates the size and dimensions of the variable with the passed parameter
        sem.var_table[state.current_call][arg][4] = var[1][4][state.arr_current_dim:]  # Updates the m of each dimension
    func.generate_param(param)
    for x in range(0, state.arr_current_dim):
        type = type[:-2]
    state.signature.append(type)

def p_seen_param_print(p):
    '''Seen_Param_Print : '''
    if(isinstance(p[-1], str) and p[-1][0] == '"'):
        param = p[-1]
    else:
        param = state.operand_stack.pop()
    rw.print_quad(param)

# Function rules
def p_seen_function(p):
    '''Seen_Function : '''
    state.local_dir = 0
    # Appends the starting quad of the function
    sem.func_table[p[-1]].append([len(state.quads)])
    p[0] = p[-1]

def p_seen_function_end(p):
    '''Seen_Function_End : '''
    func_name = p[-7]
    # Appends the ending quad of the function
    sem.func_table[func_name][3].append(len(state.quads))
    func.generate_end(func_name)
    # Appends the function size (temporal value)
    sem.func_table[func_name].append(-1)

def p_seen_return_function(p):
    '''Seen_Return_Function : '''
    state.local_dir = 0
    # Appends the starting quad of the function
    sem.func_table[p[-1]].append([len(state.quads)])
    p[0] = p[-1]

def p_seen_return_function_end(p):
    '''Seen_Return_Function_End : '''
    func_name = p[-7]
    # Appends the ending quad of the function
    sem.func_table[func_name][3].append(len(state.quads))
    func.generate_end(func_name)
    # Appends the function size (temporal value)
    sem.func_table[func_name].append(-1)

def p_seen_program(p):
    '''Seen_Program : '''
    main.generate_main()

def p_seen_program_end(p):
    '''Seen_Program_End : '''
    # Set main ending quad
    sem.func_table["main"][3].append(len(state.quads))
    func.generate_end("main")

def p_seen_main(p):
    '''Seen_Main : '''
    state.local_dir = 0
    sem.func_table["main"][3].append(len(state.quads))
    main.update_goto(len(state.quads))

def p_check_signature(p):
    '''Check_Signature : '''
    sem.is_signature_valid(p[-5], state.signature)

# Math rules
def p_seen_operand(p):
    '''Seen_Operand : '''
    if(sem.is_declared(p[-1])):
        var = sem.get_variable(p[-1])
        if(state.arr_current_dim == 0 or "[]" not in var[1][0]):
            expr.add_operand(var)
            if(len(state.operator_stack) > 0 and state.operator_stack[-1] != "#"):
                state.assign_list.append(var[1][0])

def p_seen_operand_1(p):
    '''Seen_Operand1 : '''
    if(sem.is_declared(p[-2])):
        var = sem.get_variable(p[-2])
        if(state.arr_current_dim == 0 or "[]" not in var[1][0]):
            expr.add_operand(sem.get_variable(p[-2]))
            state.assign_list.append(var[1][0])

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
    if(type[0] == "i" or type[0] == "f"):
        size = 4
    else:
        size = 1
    # Check if variable has dimensions
    if(len(state.arr_dim) > 0):
        # Multiplies all the items in the dimensions list
        elements = reduce(lambda x, y: x * y, state.arr_dim)  # Number of elements in the array
        for dim in state.arr_dim:
            type += "[]"
        sem.fill_global_variables_table(p[-3], type, [elements * size] + state.arr_dim, state.arr_m_list)
        state.arr_dim = []
        state.arr_r = 1
        state.arr_m_list = []
    else:
        sem.fill_global_variables_table(p[-3], type, [size, 1], None)
    p[0] = type

# Variables declared inside the function body
def p_seen_local_variable(p):
    '''Seen_Local_Variable : '''
    type = p[-4]
    if(type[0] == "i" or type[0] == "f"):
        size = 4
    else:
        size = 1
    # Check if variable has dimensions
    if(len(state.arr_dim) > 0):
        # Multiplies all the items in the dimensions list
        elements = reduce(lambda x, y: x * y, state.arr_dim)  # Number of elements in the array
        for dim in state.arr_dim:
            type += "[]"
        sem.fill_local_variables_table(p[-3], type, [elements * size] + state.arr_dim, state.arr_m_list)
        state.arr_dim = []
        state.arr_r = 1
        state.arr_m_list = []
    else:
        sem.fill_local_variables_table(p[-3], type, [size, 1], None)
    p[0] = type

# Variables declared as parameters
def p_seen_local_variable_1(p):
    '''Seen_Local_Variable1 : '''
    type = p[-3]
    if(type[0] == "i" or type[0] == "f"):
        size = 4
    else:
        size = 1
    # Check if variable has dimensions
    if(len(state.arr_dim) > 0):
        dims = [0]  # List to hold temporal values of dimensions
        m_list = []  # List to hold temporal values of m
        # Appends brackets to type for each dimension
        for dim in state.arr_dim:
            type += "[]"
            dims.append(-1)
            m_list.append(-1)
        sem.fill_local_variables_table(p[-2], type, dims, m_list)  # Temporal values
        state.arr_dim = []
    else:
        sem.fill_local_variables_table(p[-2], type, [size, 1], None)
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

# Empty production
def p_empty(p):
    '''empty : '''
    pass

# Error rules for productions
#def p_program_error(p):
#    '''Program : ASCII Program'''
#
#def p_block_error(p):
#    '''Block : LBRACE error RBRACE'''
#
#def p_fblock_error(p):
#    '''FBlock : LBRACE Local_Declaration error RBRACE'''
#
#def p_circle_error(p):
#    '''Circle : CIRCLE LPAREN error RPAREN'''
#    print("Missing parameter(s)")
#
#def p_superexpr_error(p):
#    '''SuperExpr : Expression error SuperExpr1'''
#    print("Malformed expression")
#
#def p_term_error(p):
#    '''Term1 : DIVIDE error Term
#             | TIMES error Term'''
#    print("Malformed expression")

# Error rule for syntax errors
def p_error(p):
    raise NameError("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(input, p), p.value))
    #try:
    #    raise NameError("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(input, p), p.value))
    #except:
    #    raise NameError("Syntax error")
    lexer.push_state("err")
    if(p):
        lexer.pop_state()
        if(p.type == 'SEMI'):
            while(True):
                tok = lexer.token()
                if(tok.type != 'ASCII'):
                    yacc.errok()
                    return(tok)
                else:
                    break
    else:
        raise NameError("Abrupt file termination")

# Build the parser
f_parser = func_parser.parser
parser = yacc.yacc()

with open(raw_input('filename > '), 'r') as f:
    input = f.read()
    preparsing = f_parser.parse(input, 0, 0)
    result = parser.parse(input, 0, 0)
    #for idx, quad in enumerate(state.quads):
    #    print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

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

# Appends memory map to functions
for func_name in sem.func_table:
    if(sem.var_table.get(func_name) != None and sem.var_table[func_name] != None):
        var_map = {}
        for var in sem.var_table[func_name].items():
            var_map[var[0]] = [var[1][0], var[1][1], var[1][2][0]]  # {id: [type, address, size (bytes)]}
        sem.func_table[func_name].append(var_map)
        sem.func_table[func_name][4] = sum(map(lambda x: x[1][2][0], sem.var_table[func_name].items()))
    else:
        sem.func_table[func_name].append({})
        sem.func_table[func_name][4] = 0

# Changes variables to memory addresses and adds temporal address offset
for idx, quad in enumerate(state.quads):
    quad.transform(state.t_offset, state.l_offset)
    #quad.add_offset(0, state.global_dir, 9000, 43000)
    print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

# Updates unresolved variables
for func_name in state.unresolved_vars:
    for var in state.unresolved_vars[func_name].items():
        arr.update_quads(var[1][0], var[1][-1], sem.var_table[func_name][var[0]])

# Pass the starting stack address to the VM as the biggest function size plus the global and constant variables
func_max_size = max(map(lambda x: x[1][4], sem.func_table.items()))
state.stack_dir += state.global_dir + state.constant_dir + func_max_size

# Sorting function
def swap(element):
    return element[1][1], element[0]

# Initializes main method variables and global variables
init_dict = {}
var_list = sem.var_table["global"].items()
if(sem.var_table.get("main") != None):
    var_list += sem.var_table["main"].items()
for var in var_list:
    start = var[1][1]
    end = start + var[1][2][0]
    if(var[1][0][0] == "i" or var[1][0][0] == "f"):
        step = 4
    else:
        step = 1
    for dir in range(start, end, step):
        init_dict[dir] = None

mem_dict = dict(map(swap, sem.var_table[sem.global_str].items()) + map(swap, sem.var_table[sem.constant_str].items()))
mem_dict.update(init_dict)

with open("o.af", "wb") as out:
    obj = {
        "quads": state.quads,
        "functions": sem.func_table,
        "mem": mem_dict
    }
    pickle.dump(obj, out, -1)

machine = vm.VirtualMachine("o.af", state.l_offset, state.stack_dir, state.t_offset)
machine.run()
