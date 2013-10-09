from oaf_quad import *

# Temp pool
# TODO: Add a pool for each primitive

# Operands stack
operand_stack = []
# Operator stack
operator_stack = []
last_operator = None

# Temp counter
temp_counter = 0

# Quad list
quads = []

# ID found
def add_operand(id, type):
    operand_stack.append([id, type])

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
        
def generate_quad(level):
    global last_operator, operand_stack, temp_counter, quads
    quad = Quad()
    if(level == 0):
        pass
    elif(level == 1):
        if(last_operator == '*' or last_operator == '/'):
            quad.operator = operator_stack.pop()
            quad.operand2 = operand_stack.pop()[0]
            quad.operand1 = operand_stack.pop()[0]
            quad.result = "t" + str(temp_counter)
            operand_stack.append([quad.result, 0])
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
    elif(level == 2):
        if(last_operator == '+' or last_operator == '-'):
            quad.operator = operator_stack.pop()
            quad.operand2 = operand_stack.pop()[0]
            quad.operand1 = operand_stack.pop()[0]
            quad.result = "t" + str(temp_counter)
            operand_stack.append([quad.result, 0])
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            temp_counter += 1
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
    elif(level == 5):
        if(last_operator == '='):
            quad.operator = operator_stack.pop()
            quad.operand1 = operand_stack.pop()[0]
            quad.result = operand_stack.pop()[0]
            operand_stack.append([quad.result, 0])
            quads.append(quad)
            if(len(operator_stack) > 0):
                last_operator = operator_stack[-1]
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
            