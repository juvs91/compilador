import oaf_quad as quad
import oaf_state as state

def generate_length(var, dim):
    q = quad.Quad()
    q.set_quad("len", dim, var, "t" + str(state.temp_counter))
    state.temp_counter += 1
    state.quads.append(q)
    state.operand_stack.append(q.result)