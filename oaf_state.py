# Module that keeps the state of the parser

#list of al the params
params_list = []

#label stack 
label_stack = []

# Maintains the addresses references when changing scopes
#address_stack = []  # [global, constant, local, temp]

# Return values of functions
return_dir_stack = []
return_var_stack = []

# Operands stack
operand_stack = []
# Operator stack
operator_stack = []
last_operator = None

# Temp counter
temp_counter = 0

# Memory address (bytes)
global_dir = 0
constant_dir = 0
local_dir = 0
temp_dir = 0
stack_dir = 0

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

# Offsets
g_offset = 0      # Global
c_offset = 0      # Constant
l_offset = 0      # Local
t_offset = 56000  # Temporal

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