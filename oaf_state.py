# Module that keeps the state of the parser

# Current calling function
current_call = ""

#label stack 
label_stack = []

# Return values of functions
return_dir_stack = []
return_var_stack = []

# Array information, used when parsing arrays
arr_dim = []  # Used to get dimension size
arr_dim_str = ""  # Used to update function signature in preparser
arr_current_dim = 0  # Used to access array and verify limits
arr_m_list = []  # M values for each dimension
arr_r = 1  # R value
arr_indices = []  # List that holds the calculates indices

# Operands stack
operand_stack = []
# Operator stack
operator_stack = []
last_operator = None

# Pointer counter
ptr_counter = 0

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
# List of al the parameters
f_param_list = []
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