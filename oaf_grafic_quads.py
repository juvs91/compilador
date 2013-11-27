import oaf_state as state
import oaf_quad as quad


def generate_draw_quad(type, exp):
    q = quad.Quad()
    q.set_quad(type, None, exp, None)
    state.quads.append(q)


def generate_pen_home_quad(type):
    q = quad.Quad()
    q.set_quad(type, None, None, None)
    state.quads.append(q)


def generate_color_quad(red, green, blue):
    q1 = quad.Quad()
    q1.set_quad("color", red, None, None)
    q2 = quad.Quad()
    q2.set_quad("color", green, None, None)
    q3 = quad.Quad()
    q3.set_quad("color", blue, None, None)
    state.quads.append(q1)
    state.quads.append(q2)
    state.quads.append(q3)


def generate_arc_quad(type,p1, p2):
    q = quad.Quad()
    q.set_quad(type, p2, p1, None)
    state.quads.append(q)