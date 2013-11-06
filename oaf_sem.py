#import the funcTable to create a new one every time a scope is needed
# import func_table as func_table
#import the quad to maque the quadric more generic

global_str = "global"
constant_str = "constant"
scope = global_str
var_table = {scope: {}, constant_str: {}}

func_table = {}

operation = None

semantic_cube = {
"=": {
    "int": {
        "int": "int",
        "char": None,
        "float": None,
        "bool": None,
    },
    "char": {
        "int": "char",
        "char": "char",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": "bool",
    }
},
"*": {
    "int": {
        "int": "int",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "char": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    }
},
"+": {
    "int": {
        "int": "int",
        "char": "char",
        "float": "float",
        "bool": None,
    },
    "char": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
"-": {
    "int": {
        "int": "int",
        "char": "char",
        "float": "float",
        "bool": None,
    },
    "char": {
        "int": None,
        "char": "char",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
"/": {
    "int": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "char": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "float",
        "char": None,
        "float": "float",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
">": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
     },
},
"<": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
">=": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
"<=": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
},
"<>": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": "bool",
    },
},
"==": {
    "int": {
        "int": "bool",
        "char": "bool",
        "float": "bool",
        "bool": None,
    },
    "char": {
        "int": "bool",
        "char": "bool",
        "float": None,
        "bool": None,
    },
    "float": {
        "int": "bool",
        "char": None,
        "float": "bool",
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": "bool",
    },
},
"||": {
    "int": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "char": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "float": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": "bool",
    },
},
"&&": {
    "int": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "char": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "float": {
        "int": None,
        "char": None,
        "float": None,
        "bool": None,
    },
    "bool": {
        "int": None,
        "char": None,
        "float": None,
        "bool": "bool",
    }
}
}


def fill_symbol_table_function(symbol, attributes): 
    if(func_table.get(symbol) == None): 
        func_table[symbol] = attributes
    else: 
        raise NameError("Function redeclaration, '{0}' already exists".format(symbol))

def fill_symbol_table_variable(symbol, type): 
    #verifica si existe el scope dado
    if(var_table.get(scope) == None): 
        var_table[scope] = {}
    if(symbol == scope or var_table[scope].get(symbol) != None): 
        raise NameError("Variable redeclaration, '{0}' already exists".format(symbol))
    else: 
        var_table[scope][symbol] = [type]
    #print("{0} {1} {2} {3} {4}".format(p[-4], p[-3], p[-2], p[-1], p[0]))

def fill_symbol_table_constant(symbol, type): 
    if(var_table[constant_str].get(symbol) != None): 
        return
    else: 
        var_table[constant_str][symbol] = [type]
    #print var_table


def get_function(func_name):
    function = func_table.get(func_name)
    if(function != None):
        return function
    else:
        raise NameError("Undeclared function '{0}'".format(func_name))

def get_scope(): 
    return scope


def validate_redeclaration_function(validate_scope): 
    if(var_table.get(validate_scope) != None):  raise NameError('se declaro varias veces una misma funcion')

def validate_variable_is_declared(var): 
    if(var_table[scope][var] == None):  raise NameError('la variable {0} no se a declarado'.var)

# revisar este pedo
def is_declared(var):
    if(var_table[constant_str].get(var) != None):
        return True
    elif(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return True
    elif(var_table[global_str].get(var) != None):
        return True
    else: 
        raise NameError("Undeclared variable '{0}'".format(var))

def get_variable(var):
    if(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return [var, var_table[scope].get(var)]
    elif(var_table[constant_str].get(var) != None):
        return [var, var_table[constant_str].get(var)]
    else:
        return [var, var_table[global_str].get(var)]

def get_type(op, op1, op2): 
    #print op, op1, op2 
    if(isinstance(op1,str)): 
        type = semantic_cube[op]["char"][op2[1][0]]
    else: 
        type = semantic_cube[op][op1[1][0]][op2[1][0]]
    if(type != None): 
        return type
    else: 
        raise NameError("Incompatible types '{0}' and '{1}'".format(op1[1][0], op2[1][0]))


def is_char(char): 
    if(len(char) != 3): 
        print len(char)
        raise NameError("its not a char ")

def is_signature_valid(func_name, signature):
    if(cmp(func_table.get(func_name)[1], signature) == 0):
        return True
    else:
        raise NameError("Wrong signature")
