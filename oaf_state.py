# Module that keeps the state of the parser
# Temp pool
# TODO: Add a pool for each primitive

import oaf_math as math

# Operands stack
operand_stack = []

# Operator stack
operator_stack = []
last_operator = None

# Temp counter
temp_counter = 0

# Quad list
quads = []

# def push_expr():
    # global operator_stack, last_operator
    # operator_stack.append('#')
    # last_operator = None

# # Pops the expression and appends the generated quads
# def pop_expr():
    # global operator_stack, last_operator, operand_stack, quads
    # while(last_operator != '#'):
        # quad, operator_stack, operand_stack = math.generate_quad(operator_stack, operand_stack, 2)
        # quads.append(quad)
        # if(len(operator_stack) > 0):
            # last_operator = operator_stack[-1]
    # #operator_stack.pop()
    # #last_operator = operator_stack[-1]
    
# def add_operand(operand):
    # operand_stack.append(operand)

# def add_operator(operator):
    # global last_operator
    # operator_stack.append(operator)
    # last_operator = operator_stack[-1]

# def generate_quad(type):
    # global operator_stack, last_operator, operand_stack, quads
    # if(type == "math"):
        # quad, operator_stack, operand_stack = math.generate_quad(operator_stack, operand_stack)
        # quads.append(quad)
        # if(len(operator_stack) > 0):
            # last_operator = operator_stack[-1]