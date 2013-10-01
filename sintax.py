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
		'''List : Array Array
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
		'''Call : Identifier LPAREN Parameters RPAREN'''
	def p_parameters(self,p):
		'''Parameters : SuperExp Coma
					  | String Coma
					  | empty'''
	def p_coma(self,p):
		'''Coma : COMMA Parameters
				| empty'''
				
	def p_read(self,p):
		'''Read : READ LPAREN Type COMMA Identifier RPAREN '''   
		
	def p_type(selfmp):
		'''Type : Primitive
				| String'''   
				
	def p_print(self,p):
		'''Print : PRINT LPAREN Printing RPAREN'''
		
	def p_printing(self,p):
		'''Printing : SuperExp ComaP
					| String ComaP''' 
					
	def p_comap(self):
		'''ComaP : COMMA Printing
				| empty'''
	 
	def p_brush(self,p):
		'''Brush : BRUSH LPAREN Color COMMA SuperExp RPAREN'''   
		
	def p_color(self,p):
		'''Color : COLOR LPAREN SuperExp COMMA SuperExp COMMA SuperExp RPAREN ''' 
		
	def p_penDown(self,p):
		'''PendDown : pd LPAREN RPAREN'''      
		
	def p_penUp(self,p):
		'''PenUp : pu LPAREN RPAREN''' 
		   
		
	def p_home(self,p):
		'''Home : HOME LPAREN RPAREN'''   
		
	def p_forward(self,p):
	   '''ForWard : FD LPAREN RPAREN'''    
	
	def p_rotate(self,p):
	   '''Rotate : RT LPAREN RPAREN'''   
	
	def p_circle(self,p):
		'''Circle : CIRCLE LPAREN SuperExp RPAREN'''     
		
	def p_arc(self,p):
		'''Arc : ARC LPAREN SuperExp COMMA SuperExp RPAREN ''' 
		
	def p_square(self,p):
		'''Square : SQUARE LPAREN SuperExp RPAREN'''       
		
	def p_paramList(self,p):
		'''ParamList : Param ComaParam'''
		
	def p_comaParam(self,p):
		'''ComaParam : COMMA ParamList
					 | empty'''
					
	def p_param(self,p):
		'''Param : Primitive ListP Identifier'''
	def p_ListP(self,p):
		'''ListP : ArrayP ArrayP'''
		
	def p_arrayp(self,p):
		'''ArrayP : LBRACE RBRACE
				  | empty'''
				
	def p_primitive(self,p):
		'''Primitive : INT
					 | FLOAT
					 | BOOL
					 | CHAR''' 
					
	def p_identifier(self,p):
		'''Identifier : Lower NextChar''' 
		
	def p_nextChar(self,p):
		'''NextChar : Lower NextChar
					| Upper NextChar
					| Digit NextChar
					| empty'''
	def p_constant(self,p):
		'''Constant : Integer
					| Float
					|Identifier'''
	def p_integer(self,p):
		'''Integer : INTEGER''' 
		
	def p_float(self,p):
		'''Float : FLOAT'''   
		
	def p_string(self,p):
		'''String : COMMILLAS Printable COMMILLAS'''    
		
	def p_printable(self,p):
		l =[]
	def p_lower(self,p):
		l =[]
	def p_upper(self,p):
		l =[]
	def p_digit(self,p):
		l =[]
	
print MyLexer.listOfTokens
	