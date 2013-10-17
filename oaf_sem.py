#import the funcTable to create a new one every time a scope is needed 
# import func_table as func_table                                          
#import the quad to maque the quadric more generic

global_str = "global"
scope = global_str
var_table = {scope:{}} 

operation = None
semantic_cube = {
"=":{
	"int":{
		"int":"int",
		"char":None,
		"float":None,
		"bool":None,
	},
	"char":{
		"int":None,
		"char":"char",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":None,
		"char":None,
		"float":"float",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":"bool",
	}
},
"*":{
	"int":{
		"int":"int",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"char":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"float",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	}
},
"+":{
	"int":{
		"int":"int",
		"char":"char",
		"float":"float",
		"bool":None,
	},
	"char":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"float",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
},
"-":{
	"int":{
		"int":"int",
		"char":"char",
		"float":"float",
		"bool":None,
	},
	"char":{
		"int":None,
		"char":"char",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"float",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
},
"/":{
	"int":{
		"int":"float",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"char":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"float",
		"char":None,
		"float":"float",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
},
">":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	 }, 
},
"<":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	}, 
},
">=":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
},
"<=":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
},
"<>":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":"bool",
	},
},
"==":{
	"int":{
		"int":"bool",
		"char":"bool",
		"float":"bool",
		"bool":None,
	},
	"char":{
		"int":"bool",
		"char":"bool",
		"float":None,
		"bool":None,
	},
	"float":{
		"int":"bool",
		"char":None,
		"float":"bool",
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":"bool",
	},
},
"||":{
	"int":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"char":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"float":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":"bool",
	},
},
"&&":{
	"int":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"char":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"float":{
		"int":None,
		"char":None,
		"float":None,
		"bool":None,
	},
	"bool":{
		"int":None,
		"char":None,
		"float":None,
		"bool":"bool",
	}	
}
}
                   

def fill_symbol_table_variable(symbol, type):
     #verifica si existe el scope dado
     if(var_table.get(scope) == None):
         var_table[scope] = {}

     if(symbol == scope or var_table[scope].get(symbol) != None):
         raise NameError("Variable redeclaration, '{0}' already exists".format(symbol))
     else:
         var_table[scope][symbol] = [type]  
    #print("{0} {1} {2} {3} {4}".format(p[-4], p[-3], p[-2], p[-1], p[0]))
	
	
	
def get_scope():
	return scope  
	
def validate_redeclaration_function(validate_scope):
	if(var_table.get(validate_scope) != None): raise NameError('se declaro varias veces una misma funcion')  

def validate_variable_is_declared(var):
	if(var_table[scope][var] == None): raise NameError('la variable {0} no se a declarado'.var)
    
def is_declared(var):
    if(var_table.get(scope) == None):
        raise NameError("Undeclared variable '{0}'".format(var))
    elif(var_table[scope].get(var) == None and var_table[global_str].get(var) == None):
        raise NameError("Undeclared variable '{0}'".format(var))
    else:
        return True

def get_variable(var):
    if(var_table[scope].get(var) != None):
        return [var, var_table[scope].get(var)]
    else:
        return [var, var_table[global_str].get(var)]
        
def get_type(op, op1, op2):
    #print op, op1, op2
    type = semantic_cube[op][op1[1][0]][op2[1][0]]
    if(type != None):
        return type
    else:
        raise NameError("Incompatible types '{0}' and '{1}'".format(op1[1][0], op2[1][0]))