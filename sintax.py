import ply.yacc as yacc 

from lexer import MyLexer

class Sintax():
	def __init__(self):
		l =[]
	def p_program(self,p):
		'''Program : Declaration FunctionTotal Main '''
	def p_functionTotal(self,p):
		'''FunctionTotal : Function
						 | RFunction'''
	
	def p_main(self,p):
		'''Main :  MAIN LPAREN RPAREN FBlock'''  
		
	def p_declaration(self,p):
		'''Declaration : Primitive Identifier List SEMI
					   | empty'''
	
	def List(self,p):
		'''List : Array Array2'''
		
	def p_array2(self,p):
		'''Array2 : Array
				  | empty'''
	def Array(self,p):
		'''Array : LBRACKET Integer RBRACKET'''
	
	def p_function(self,p):
		'''Function : VOID Identifier LPAREN ParamList RPAREN FBLock'''  
		
	def p_rFunction(self,p):
		'''RFunction : Primitive Identifier LPAREN ParamList RPAREN RFBLock'''  
		
	def p_block(self,p):
		'''Block : LBRACKET Instruction  RBRACKET''' 
		
	def p_fBlock(self,p):
		'''FBlock : LBRACKET Declaration Instruction  RBRACKET''' 
		
	def p_rFBlock(self,p):
		'''RFBlock : LBRACKET Declaration Instruction RETURN SuperExp SEMI RBRACKET'''  
		
	def p_loop(self,p):
		'''Loop : LOOP  LPAREN  SuperExp RPAREN Block'''
		
	def p_conditional(self,p):
		'''Conditional : IF LPAREN SuperExp RPAREN Block Else'''  
		
	def p_else(self,p):
		'''Else : ELSE Block
				| empty''' 
				
	def p_superExpr(self,p):
		'''SuperExp : Expression LogicalOp'''
		
	def p_logicalOp(self,p):
		'''LogicalOp : OR  SuperExp
					 |  AND SuperExp
					 | empty'''

	def p_expr(self,p):
		'''Expr : Term Op1'''
		
	def p_op1(self,p):
		'''Op1 : PLUS  Expr
			   | MINUS  Expr
			   | empty'''    
			
	def p_expression(self,p):
		'''Expression : Expr Comparison''' 
		
	def p_comparison(self,p):
		'''Comparison : GREATHAN Expr
					  | LESSTHAN Expr
					  | DIFERENT Expr
					  | TWOEQUAL Expr
					  | GREATHANOREQUAL Expr
					  | LESSTHANOREQUAL Expr
					  | empty
					  '''
		
	def p_term(self,p):
		'''Term : Factor Op2'''  
				            
	def p_op2(self,p):
		'''Op2 : TIMES  Term
			   | DIVIDE Term
			   | empty'''  
			
	def p_factor(self,p):
		'''Factor : LPAREN SuperExp RPAREN   
				  | Op3 Constant'''
	def p_op3(self,p):
		'''Op3 : PLUS
			   | MINUES
			   | empty'''
	def p_instruccion(self,p):
		'''Instruction : Loop SEMI
					   | Assign SEMI
					   | Call SEMI
					   | Brush SEMI
					   | Read SEMI
					   | Print SEMI
					   | PenDown SEMI
					   | PenUp  SEMI
					   | Home SEMI
					   | Forward SEMI
					   | Rotate SEMI
					   | Color SEMI
					   | Cirlce SEMI
					   | Arc SEMI
					   | Square SEMI '''   
					
	def p_assign(self,p):
		''' Assign : Identifier EQUAL Assignation '''   
		
	def p_assignation(self,p):
		'''Assignation : SuperExp 
					   | String 
					   | Call'''
					
	def p_call(self,p):
		''''''
	def p_read(self,p):
		l =[]
	def p_print(self,p):
		l =[]
	def p_brush(self,p):
		l =[]
	def p_color(self,p):
		l =[]
	def p_penDown(self,p):
		l =[]
	def p_penUp(self,p):
		l =[]
	def p_home(self,p):
		l =[]
	def p_forward(self,p):
		l =[]
	def p_rotate(self,p):
		l =[]
	def p_circle(self,p):
		l =[]
	def p_arc(self,p):
		l =[]
	def p_square(self,p):
		l =[]
	def p_paramList(self,p):
		l =[]
	def p_param(self,p):
		l =[]
	def p_primitive(self,p):
		l =[]
	def p_identifier(self,p):
		l =[]
	def p_constant(self,p):
		l =[]
	def p_integer(self,p):
		l =[]
	def p_float(self,p):
		l =[]
	def p_string(self,p):
		l =[]
	def p_printable(self,p):
		l =[]
	def p_lower(self,p):
		l =[]
	def p_upper(self,p):
		l =[]
	def p_digit(self,p):
		l =[]
	
print MyLexer.listOfTokens
	