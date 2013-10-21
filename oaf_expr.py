import oaf_sem as sem  
import oaf_state as state 
from oaf_quad import *
from oaf_state import *

# Temp pool
# TODO: Add a pool for each primitive

# ID found
def add_operand(operand):
    state.operand_stack.append(operand)

def add_operator(operator):
    global last_operator
    state.operator_stack.append(operator)
    if(operator == '#'):
        state.last_operator = None
    else:
        state.last_operator = operator_stack[-1]

def push_expr():
    global operator_stack, last_operator
    state.operator_stack.append('#')
    state.last_operator = None

def pop_expr():
    global operator_stack, last_operator
    state.operator_stack.pop()
    state.last_operator = operator_stack[-1]
        
def generate_quad(hierarchy):
    global last_operator, operand_stack, temp_counter, quads
    quad = Quad()
    if(hierarchy == 0):
        if(state.last_operator == 'u+' or state.last_operator == 'u-'):
            quad = create_quad(state.operator_stack.pop(), None, state.operand_stack.pop(), state.operand_stack.pop())
            state.operand_stack.append(quad.result)
            state.quads.append(quad)
            if(len(state.operator_stack) > 0):
                lstate.ast_operator = state.operator_stack[-1]
    elif(hierarchy == 1):
        if(state.last_operator == '*' or state.last_operator == '/'):
            quad = create_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.operand_stack.append(quad.result)
            state.quads.append(quad)
            if(len(state.operator_stack) > 0):
                state.last_operator = state.operator_stack[-1]
            state.temp_counter += 1
    elif(hierarchy == 2):
        if(state.last_operator == '+' or state.last_operator == '-'):
            quad = create_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.operand_stack.append(quad.result)
            state.quads.append(quad)
            if(len(state.operator_stack) > 0):
                state.last_operator = state.operator_stack[-1]
            state.temp_counter += 1
    elif(hierarchy == 3):
        if(state.last_operator == '==' or state.last_operator == '<=' or state.last_operator == '>=' or state.last_operator == '<>'  or state.last_operator == '<'  or state.last_operator == '>'):
            state.quad = create_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.operand_stack.append(quad.result)
            state.quads.append(quad)
            if(len(state.operator_stack) > 0):
                state.last_operator = state.operator_stack[-1]
            state.temp_counter += 1
    elif(hierarchy == 4):
        if(state.last_operator == '&&' or state.last_operator == '||'):
            quad = create_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.operand_stack.append(quad.result)
            quads.append(quad)
            if(len(state.operator_stack) > 0):
                state.last_operator = state.operator_stack[-1]
            state.temp_counter += 1
    elif(hierarchy == 5):
        if(state.last_operator == '='):
            quad = create_quad(state.operator_stack.pop(), None, state.operand_stack.pop(), state.operand_stack.pop())
            state.operand_stack.append(quad.result)
            state.quads.append(quad)
            if(len(state.operator_stack) > 0):
                state.last_operator = state.operator_stack[-1]
            
def create_quad(op, op2, op1, res):
    quad = Quad()
    quad.operator = op
    quad.operand2 = op2
    quad.operand1 = op1
    if(op2 == None):
        res[1][0] = sem.get_type(op, op1, res)
        quad.result = res
    else:
        quad.result = [res, [sem.get_type(op, op1, op2)]]
    return quad
            
def clear_stacks():
    global operator_stack, operand_stack, last_operator
    del(state.operator_stack[:])
    del(state.operand_stack[:])
    state.last_operator = None