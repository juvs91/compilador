import oaf_state as state 
import oaf_quad as quad

# Functions quads module   
def generate_era(func_name, res):
    q = quad.Quad()
    q.set_quad("era", None, func_name, res)
    state.quads.append(q)
    
def generate_param(op1):
    q = quad.Quad()
    q.set_quad("param", None, op1, state.param_counter)
    state.quads.append(q)
    state.param_counter += 1
    
def generate_gosub(func_name, index):
    q = quad.Quad()
    q.set_quad("gosub", None, func_name, index)
    state.quads.append(q)

def generate_return(op1):
    q = quad.Quad()
    q.set_quad("return", None, op1, None)
    state.quads.append(q)

def generate_end(func_name):
    q = quad.Quad()
    q.set_quad("end", None, func_name, None)
    state.quads.append(q)