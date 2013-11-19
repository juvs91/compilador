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
    #type = op1[1][0]
    #if(type[0] == "i" or type[0] == "f"):
    #    size = 4
    #else:
    #    size = 1
    #var = [func_name, [type, 0, size, 't']]
    # Revisar este pedo
    #state.return_var_stack.append(var)
    #q.set_quad("return", None, op1, var)
    q.set_quad("return", None, op1, None)
    state.quads.append(q)

def generate_end(func_name):
    q = quad.Quad()
    q.set_quad("end", None, func_name, None)
    state.quads.append(q)