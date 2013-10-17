import oaf_sem as sem
from oaf_quad import *
from oaf_state import *

# Temp pool
# TODO: Add a pool for each primitive

# ID found
def add_operand(operand):
    operand_stack.append(operand)

def add_operator(operator):
    global last_operator
    operator_stack.append(operator)
    if(operator == '#'):
        last_operator = None
    else:
        last_operator = operator_stack[-1]

def push_expr():
    global operator_stack, last_operator
    operator_stack.append('#')
    last_operator = None

def pop_expr():
    global operator_stack, last_operator
    operator_stack.pop()
    last_operator = operator_stack[-1]
        
def generate_quad(hierarchy):
    global last_operator, operand_stack, temp_counter, quads
    print operator_stack, operand_stack, hierarchy
    quad = Quad()
    if(hierarchy == 0):
        if(last_operator == 'u+' or last_operator == 'u-'):
            quad = create_quad(operator_stack.pop(), None, operand_stack.pop(), operand_stack.pop())
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
    elif(hierarchy == 1):
        if(last_operator == '*' or last_operator == '/'):
            quad = create_quad(operator_stack.pop(), operand_stack.pop(), operand_stack.pop(), "t" + str(temp_counter))
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
    elif(hierarchy == 2):
        if(last_operator == '+' or last_operator == '-'):
            quad = create_quad(operator_stack.pop(), operand_stack.pop(), operand_stack.pop(), "t" + str(temp_counter))
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
    elif(hierarchy == 3):
        if(last_operator == '==' or last_operator == '<=' or last_operator == '>=' or last_operator == '<>'  or last_operator == '<'  or last_operator == '>'):
            quad = create_quad(operator_stack.pop(), operand_stack.pop(), operand_stack.pop(), "t" + str(temp_counter))
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
    elif(hierarchy == 4):
        if(last_operator == '&&' or last_operator == '||'):
            quad = create_quad(operator_stack.pop(), operand_stack.pop(), operand_stack.pop(), "t" + str(temp_counter))
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
    elif(hierarchy == 5):
        if(last_operator == '='):
            quad = create_quad(operator_stack.pop(), None, operand_stack.pop(), operand_stack.pop())
            operand_stack.append(quad.result)
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            
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
    del(operator_stack[:])
    del(operand_stack[:])
    last_operator = None