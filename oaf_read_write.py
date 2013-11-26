import oaf_state as state
import oaf_quad as quad
import oaf_sem as sem


def print_quad(printable):
    q = quad.Quad()
    q.set_quad("print", None, printable, None)
    state.quads.append(q)


def read_quad(type, var):
    if(type == var[1][0]):
        q = quad.Quad()
        q.set_quad("read", None, type, var)
        #state.operand_stack.append(q.result)
        state.quads.append(q)
    else:
        print "error tipos incompatiblee"
