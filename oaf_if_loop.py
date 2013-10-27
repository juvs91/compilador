import oaf_state as state
import oaf_quad as quad

def generate_if_goto_F(exp):
	q = quad.Quad()
	q.set_quad("gotoFalse", exp, None, None)
	#state.operand_stack.append(q.result)
	state.quads.append(q)
	state.label += 1



def put_label_to_goto_F(label):
	state.quads[label].result = state.label+1
	
def generate_else_goto():
	q = quad.Quad()
	q.set_quad("goto", None, None, None)
	#state.operand_stack.append(q.result)
	state.quads.append(q)
	state.label += 1
	
def generate_loop_goto(label):
	q = quad.Quad()
	q.set_quad("goto", None, None, label+1)
	#state.operand_stack.append(q.result)
	state.quads.append(q)
	state.label += 1