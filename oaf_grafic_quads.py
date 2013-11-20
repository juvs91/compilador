import oaf_state as state
import oaf_quad as quad


def generate_draw_quad(type,exp):      
	q = quad.Quad()
	q.set_quad(type, None, exp, None) 
	state.quads.append(q)
	
def generate_pen_home_quad(type):
	q = quad.Quad()
	q.set_quad(type, None, None, None) 
	state.quads.append(q)     
	
	
def generate_color_quad(red,green,blue): 
	q = quad.Quad()
	q.set_quad("color", green, red, blue) 
	state.quads.append(q)
	                             
	
def generate_arc_quad(p1,p2):
	q = quad.Quad()
	q.set_quad("arc", p2, p1, None) 
	state.quads.append(q)        
	
	
	
