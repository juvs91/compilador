from oaf_quad import *
import oaf_sem as sem

# checar esta funcion para ver si se pone en quad
def create_quad(op, op2, op1, res):
	quad = Quad()
	quad.operator = op
	quad.operand2 = op2
	quad.operand1 = op1
	if(op2 == None):
		if(op =="read" or op =="print"):
			#quad.result = op2 
			quad.result = res 
		else:
			res[1][0] = sem.get_type(op, op1, res)
			quad.result = res
	else:
		quad.result = [res, [sem.get_type(op, op1, op2)]]

	return quad