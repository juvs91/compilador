#import the funcTable to create a new one every time a scope is needed 
import func_table as func_table                                          
#import the quad to maque the quadric more generic
import quad as quad


var_table = {"global":{}}
scope = "global"

class semantic():
	def __init__(self): 
		#always creat it befor the sintax start
		var_table = []                      
			
	
	def fill_symbol_table_variable(self,symbol,type,scope):
		#create a new array everytime you found a new symbol, it goning to be the row of the symbos and its 
		#always in this order type symbol and scope  
		new_symbol = []    
		#fill the row                           
		new_symbol.append(type)#insert the type in the row
		new_symbol.append(symbol)#insert the symbol in the row 
		
		#check if the symbol is global or local 
		if scope == "global"  
			newSymbol.append("global")#the scope the name of the function or the word global    
			
		else:
			#create a new table to set the scope of the variable on the table 
			function_table = func_table()
			
			function_table.fill_table(newSymbol) 
			
			#put the new object in the table,it has the local scope of the function
			newSymbol.append(function_table) 
			
			
		self.var_table.append(newSymbol)#insert the row in the matrix 
		
			
	
			   