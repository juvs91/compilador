#import the funcTable to create a new one every time a scope is needed 
# import func_table as func_table                                          
#import the quad to maque the quadric more generic


scope = "global"
var_table = {scope:{}}
                   

def fill_symbol_table_variable(symbol,type,scope):
	#create a new array everytime you found a new symbol, it goning to be the row of the symbos and its 
	#always in this order type symbol and scope dirScope in scope send de function or global and the dir Scope send null if its global  
	#new_symbol = []    
	#fill the row                           
	#new_symbol.append(type)#insert the type in the row
	#new_symbol.append(symbol)#insert the symbol in the row  
	#newSymbol.append(scope)#the scope the name of the function or the word global    
	
	
	#check if the symbol is global or local 
	#if scope == "global"  
	#	newSymbol.append("global")#the scope the name of the function or the word global    
	#	
	#else:
		#create a new table to set the scope of the variable on the table 
	#	function_table = func_table()
		
	#	function_table.fill_table(newSymbol) 
		
		#put the new object in the table,it has the local scope of the function
	#	newSymbol.append(function_table) 

		
		
	#self.var_table.append(newSymbol)#insert the row in the matrix 
	
	new_dictionary_symbol = {}
	
	##fill the diccionary
	new_dictionary_symbol["type"] = type
	new_dictionary_symbol["symbol"] = symbol
	scope = scope
	var_table[scope]=new_dictionary_symbol
	
def get_scope():
	return scope

	   

	
