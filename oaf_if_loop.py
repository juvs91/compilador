import oaf_state as state
import oaf_quad as quad

def generate_if_goto_f(exp):
    q = quad.Quad()
    q.set_quad("gotoFalse", None, exp, None)
    state.quads.append(q)

def put_label_to_goto_f(label):
    state.quads[label].result = len(state.quads)

def generate_else_goto():
    q = quad.Quad()
    q.set_quad("goto", None, None, None)
    state.quads.append(q)

def generate_loop_goto(label):
    q = quad.Quad()
    # revisar este pedo
    q.set_quad("goto", None, None, label + 1)
    state.quads.append(q)