class Quad:
	def __init__(self):
		self.operator = None
		self.operand1 = None
		self.operand2 = None
		self.result = None 
		# Operands stack
		self.operand_stack = []
		# Operator stack
		self.operator_stack = [] 
		#jump stack 
		self.jump_stack = [] 
		
		#label that need to jump the gotoV,gotoF,goto
		self.label = 0
		
		self.last_operator = None
		
		# Temp counter
		self.temp_counter = 0
		
		# Quad list
		self.quads = []  
		
	def push_operand_stack(self,n):
		self.operand_stack.append(n) 
		
	def pop_operand_stack(self):
		return self.operand_stack.pop()
	
	def get_operand_stack_index(self,i):
		return self.operand_stack[i]
		
	def push_operator_stack(self,n):
		self.operator_stack.append(n)
		
	def pop_operator_stack(self):
		return self.operator_stack.pop()

	def get_operator_stack_index(self,i):
		return self.operator_stack[i]
		
	def push_jump_stack(self,n):
		self.jump_stack.append(n)  
		
	def pop_jump_stack(self):
		return self.jump_stack.pop()  
		
	def get_jump_stack_index(self,i):
		return self.jump_stack[i] 
		
	def get_labe(self):
		return self.label	
	
	def set_label(self,l):
		self.label = l
		
		
	def get_last_operator(self):
		return self.last_operator
		
		
	def set_last_operator(self,operator):
		self.last_operator = operator
		
		
	def get_temp_counter(self):
		return self.temp_counter
		
	def set_temp_counter(self,counter):
		self.temp_counter = counter
		
		
	def push_quad(self,n):
		self.quad.append(n)   
		
	def pop_quad(self):
		return self.quad.pop()     

	def get_quad_index(self,i):
		return self.quad[i]  
		
		
	def generate_quad(self):
		return [ self.operator,self.operand1,self.operand2,self.result]