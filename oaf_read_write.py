from oaf_quad import *
import oaf_state as state 
import create_quad as cq
import oaf_sem as sem


def print_quad(printable):    
	quad = Quad()
	quad = cq.create_quad("print",None,printable,"t" + str(temp_counter))
	state.operand_stack.append(quad.result)
	state.quads.append(quad)
	state.temp_counter += 1 
	
	
	
def read_quad(type,var,scope): 
	if(type == sem.var_table[scope][var][0]):
		quad = Quad()
		quad = cq.create_quad("read",None,"t" + str(state.temp_counter),var)
		state.operand_stack.append(quad.result)
		state.quads.append(quad)
		state.temp_counter += 1
	else:
		print "error tipos incompatiblee"
