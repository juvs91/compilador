import oaf_quad as quad
import oaf_state as state
import oaf_sem as sem

def generate_verify(index, limit):
    q = quad.Quad()
    q.set_quad("ver", None, index, limit)
    state.quads.append(q)

def generate_multiply_m(index, m):
    q = quad.Quad()
    # Adds the remaining information to the m variable
    mn = [m, ["int", 0, [4, 1], "s"]]  # "s" special type
    q.set_quad("*", mn, index, "t" + str(state.temp_counter))
    state.temp_counter += 1
    state.quads.append(q)
    state.operand_stack.append(q.result)

def generate_dir(d):
    q = quad.Quad()
    dir = [d, ["int", 0, [4, 1], "s"]]
    q.set_quad("+", dir, state.operand_stack.pop(), "p" + str(state.ptr_counter))
    state.ptr_counter += 1
    state.quads.append(q)
    state.operand_stack.append(q.result)