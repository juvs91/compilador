#import the funcTable to create a new one every time a scope is needed 
# import func_table as func_table                                          
#import the quad to maque the quadric more generic


scope = "global"
var_table = {scope:{}}
                   

def fill_symbol_table_variable(symbol,type):
     
     #verifica si existe el scope dado
     if(var_table.get(scope) == None):
         var_table[scope] = {}

     if(symbol == scope or var_table[scope].get(symbol) != None):
         raise NameError("Variable redeclaration, {0} already exists".format(symbol))
     else:
         var_table[scope][symbol] = [type]  
    #print("{0} {1} {2} {3} {4}".format(p[-4], p[-3], p[-2], p[-1], p[0]))
	
	
	
def get_scope():
	return scope  
	
def validate_redeclaration_function(validate_scope):
	if(var_table.get(validate_scope) != None): raise NameError('se declaro varias veces una misma funcion')
	
	



	
