import oaf_state as state
import oaf_quad as quad

def generate_main():
    q = quad.Quad()
    q.set_quad("goto", None, "main", None)
    state.quads.append(q)   
    #state.label +=1

def update_goto(index):
    state.quads[0].result = index