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
    q.set_quad("mul", mn, index, "t" + str(state.temp_counter))
    state.temp_counter += 1
    state.quads.append(q)
    state.operand_stack.append(q.result)

def generate_dir(d):
    q = quad.Quad()
    dir = [d, ["int", 0, [4, 1], "s"]]
    q.set_quad("add", dir, state.operand_stack.pop(), "t" + str(state.temp_counter))
    state.temp_counter += 1
    state.quads.append(q)
    state.operand_stack.append(q.result)

def update_quads(start, end, var):
    v_dim = 1
    m_dim = 0
    for index in range(start, end + 1):
        q = state.quads[index]
        if(q.operator == "ver"):
            q.result = var[2][v_dim] - 1
            v_dim += 1
        elif(q.operator == "mul"):
            q.operand2 = var[4][m_dim]
            m_dim += 1
        elif(q.operator == "add"):
            q.operand2 = var[1]