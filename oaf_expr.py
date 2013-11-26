import oaf_state as state 
import oaf_quad as quad

# Temp pool
# TODO: Add a pool for each primitive

# ID found
def add_operand(operand):
    state.operand_stack.append(operand)

def add_operator(operator):
    state.operator_stack.append(operator)
    if(operator == '#'):
        state.last_operator = None
    else:
        state.last_operator = state.operator_stack[-1]

def pop_operator():
    state.operator_stack.pop()
    if(len(state.operator_stack) > 0):
        state.last_operator = state.operator_stack[-1]
    else:
        state.last_operator = None

def push_expr():
    state.operator_stack.append('#')
    state.last_operator = None

def pop_expr():
    state.operator_stack.pop()
    if(len(state.operator_stack) > 0):
        state.last_operator = state.operator_stack[-1]
    else:
        state.last_operator = None

def generate_quad(hierarchy):
    q = quad.Quad()
    if(hierarchy == 0):
        if(state.last_operator == 'u+' or state.last_operator == 'u-'):
            q.set_quad(state.operator_stack.pop(), None, state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.temp_counter += 1
    elif(hierarchy == 1):
        if(state.last_operator == '*' or state.last_operator == '/'):
            # id, [type, address, size]
            q.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.temp_counter += 1
    elif(hierarchy == 2):
        if(state.last_operator == '+' or state.last_operator == '-'):
            q.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.temp_counter += 1
    elif(hierarchy == 3):
        if(state.last_operator == '==' or state.last_operator == '<=' or state.last_operator == '>=' or state.last_operator == '<>' or state.last_operator == '<' or state.last_operator == '>'):
            q.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.temp_counter += 1
    elif(hierarchy == 4):
        if(state.last_operator == '&&' or state.last_operator == '||'):
            q.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
            state.temp_counter += 1
    elif(hierarchy == 5):
        if(state.last_operator == '='):
            q.set_quad(state.operator_stack.pop(), None, state.operand_stack.pop(), state.operand_stack.pop())
    if(q.operator != None):
        state.quads.append(q)
        if(q.operator != "="):
            state.operand_stack.append(q.result)
            if(len(state.assign_list) > 1):
                state.assign_list.pop()
                state.assign_list.pop()
                state.assign_list.append(q.result[1][0])
    else:
        del(q)
    if(len(state.operator_stack) > 0):
        state.last_operator = state.operator_stack[-1]
        if(state.last_operator == '#'):
            state.last_operator = None
    else:
        state.last_operator = None