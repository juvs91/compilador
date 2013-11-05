import oaf_state as state
import oaf_quad as quad
import oaf_sem as sem


def print_quad(printable):
    if(isinstance(printable,list)):
       printable = printable[0]
    q = quad.Quad()
    q.set_quad("print", None, printable, None)
    #state.operand_stack.append(q.result)
    state.quads.append(q)
    #state.temp_counter += 1

def read_quad(type, var, scope):
    print type, var, scope
    if(type == sem.var_table[scope][var][0]):
        q = quad.Quad()
        q.set_quad("read", None, "t" + str(state.temp_counter), var)
        #state.operand_stack.append(q.result)
        state.quads.append(q)
        state.temp_counter += 1
    else:
        print "error tipos incompatiblee"
