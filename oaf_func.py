import oaf_state as state 
import oaf_quad as quad
import oaf_sem as sem

# Functions quads module   
def generate_quad(func_name):
    pass
    
def generate_era(func_name):
    q = quad.Quad()
    q.set_quad("era", None, func_name, sem.get_function(func_name)[2])
    state.quads.append(q)
    
def generate_param(op1):
    q = quad.Quad()
    q.set_quad("param", None, op1, "param" + str(state.param_counter))
    state.quads.append(q)
    state.param_counter += 1
    
def generate_gosub(func_name):
    q = quad.Quad()
    q.set_quad("gosub", None, func_name, None)
    state.quads.append(q)

def generate_end(func_name):
    q = quad.Quad()
    q.set_quad("end", None, func_name, None)
    state.quads.append(q)