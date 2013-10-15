import oaf_global_quad as quad

# Temp pool
# TODO: Add a pool for each primitive


# ID found
def add_operand(id, type):
    #operand_stack.append([id, type])
    quad.quad.push_operand_stack([id, type])


def add_operator(operator):
    #global last_operator
    #operator_stack.append(operator) 
    quad.quad.push_operator_stack(operator)
    if(operator == '#'):
        #last_operator = None  
        quad.quad.set_last_operator(None)
    else:
        #last_operator = operator_stack[-1]  
         quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1)) 
         #print quad.quad.get_last_operator()

def push_expr():
    #global operator_stack, last_operator
    #operator_stack.append('#')
    quad.quad.push_operator_stack("#")
    quad.quad.set_last_operator(None)

def pop_expr():  
    #global operator_stack, last_operator
    #operator_stack.pop()
    #last_operator = operator_stack[-1]  
    op = quad.quad.pop_operator_stack()   

    
        
def generate_quad(level):
    #global last_operator, operand_stack, temp_counter, quads
    #quad = Quad()  
    if(level == 0):
        pass
    elif(level == 1):
        if(quad.quad.get_last_operator() == '*' or quad.quad.get_last_operator() == '/'):
            quad.quad.operator = quad.quad.pop_operator_stack()   
            quad.quad.operand2 = quad.quad.pop_operand_stack()[0]
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = "t" + str(quad.quad.get_temp_counter())
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad()) 
            if(len(quad.quad.operator_stack) > 0):
                quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
            quad.quad.set_temp_counter(quad.quad.get_temp_counter()+1)
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
    elif(level == 2): 
        print quad.quad.get_last_operator()
        if(quad.quad.get_last_operator() == '+' or quad.quad.get_last_operator() == '-'):   
            quad.quad.operator = quad.quad.pop_operator_stack()  
            quad.quad.operand2 = quad.quad.pop_operand_stack()[0]
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = "t" + str(quad.quad.get_temp_counter())
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad())
            if(len(quad.quad.operator_stack) > 0):
               quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
            quad.quad.set_temp_counter(quad.quad.get_temp_counter()+1)
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
    elif(level == 5):
        if(quad.quad.get_last_operator() == '='): 
            quad.quad.operator = quad.quad.pop_operator_stack() 
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = quad.quad.pop_operand_stack()[0]
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad())
            if(len(quad.quad.operator_stack) > 0):
                quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
            #print(quad.operator, quad.operand1, quad.operand2, quad.result)
            