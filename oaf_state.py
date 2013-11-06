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

def reset_call():
    global param_counter, param_types, signature
    param_counter = 0
    param_types = []
    signature = []