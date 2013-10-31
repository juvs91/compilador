# Module that keeps the state of the parser
# Temp pool
# TODO: Add a pool for each primitive
            
#list of al the params
params_list = []

#label stack 
label_stack = []


# Operands stack
operand_stack = []

# Operator stack
operator_stack = []  

last_operator = None


#label
label = 0
# Temp counter
temp_counter = 0   

# Function signature
signature = []

# Function size(bytes)
f_size = 0

# Param counter
param_counter = 0
# Param types of function call
param_types = []

# Quad list
quads = []

def clear_stacks():
    global operator_stack, operand_stack, last_operator
    del(operator_stack[:])
    del(operand_stack[:])
    last_operator = None

def reset_param_counter():
    global param_counter
    param_counter = 0

def reset_param_types():
    global param_types
    param_types = []

def reset_call():
    reset_param_counter()
    reset_param_types()

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