import oaf_quad as quad
import oaf_state as state
import oaf_sem as sem

def generate_verify(index, limit):
    q = quad.Quad()
    q.set_quad("ver", None, index, limit)
    state.quads.append(q)