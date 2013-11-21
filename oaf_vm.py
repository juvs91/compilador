import cPickle as pickle

class VirtualMachine:
    def __init__(self, filename, local_address, stack_address):
        self.instr_ptr = 0  # Current quad
        self.instr_ptr_stack = []  # Stack used when returning to previous instruction
        self.function_call_stack = []  # Stack of function calls
        self.return_dir_stack = []  # Address to save value to
        self.return_value_stack = []  # Value to save at address
        self.local_dir_start = local_address  # Address to start the local variables
        self.stack_dir_start = stack_address  # Address to start the stack
        self.stack_dir = stack_address  # Next free address to start continue stack
        self.context = ["main", [], []]  # [function name, [stack begin, stack end], [{temporals list}]]
        # Loads the object code and initializes the virtual machine
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        self.functions = self.obj["functions"]
        self.vars = self.obj["vars"]
        self.mem = self.obj["mem"]

    def load_obj(self, filename):
        f = open(filename, "rb")
        return pickle.load(f)

    # Adds current function variables to stack before calling another one
    # and saves the local variables to the stack
    # If the functions returns a value that value is also stored in the stack
    def save_state(self, temporals):
        copy_dir = self.stack_dir
        for item in self.mem.items()[:]:
            # revisar este pedo
            if(self.local_dir_start <= item[0] < self.stack_dir_start):
                self.mem[copy_dir] = item[0]  # Copies the memory address
                self.mem[copy_dir + 4] = item[1]  # Copies the value stored in that address
                copy_dir += 8
        for item in temporals:
            if(self.mem[item] != None):
                self.mem[copy_dir] = item  # Copies the memory address
                self.mem[copy_dir + 4] = self.mem[item]  # Copies the value stored in that address
                copy_dir += 8
        return copy_dir

    def restore_state(self):
        self.context = self.function_call_stack.pop()
        dirs = self.context[1]
        if(dirs[0] >= 0):  # There's something to restore
            for i in range(dirs[0], dirs[1], 8):
                self.mem[self.mem[i]] = self.mem[i + 4]
                del(self.mem[i], self.mem[i + 4])
            return dirs[0]  # Something was restored
        else:
            return self.stack_dir  # Nothing was restored

    def run(self):
        quad = self.quads[self.instr_ptr]
        op = quad.operator
        op1 = quad.operand1
        op2 = quad.operand2
        res = quad.result
        while(op != "end" or op1 != "main"):
            if(op == "+"):
                self.mem[res] = self.mem[op1] + self.mem[op2]
            elif(op == "-"):
                self.mem[res] = self.mem[op1] - self.mem[op2]
            elif(op == "*"):
                self.mem[res] = self.mem[op1] * self.mem[op2]
            elif(op == "/"):
                self.mem[res] = self.mem[op1] / self.mem[op2]
            elif(op == "="):
                # Check if result is a pointer
                if(self.mem.get(res) != None and isinstance(self.mem[res], str) and self.mem[res][0] == "*"):
                    res = int(self.mem[res][1:])
                # Check if operand is a pointer
                if(isinstance(self.mem[op1], str) and self.mem[op1][0] == "*"):
                    op1 = int(self.mem[op1][1:])
                self.mem[res] = self.mem[op1]
            elif(op == ">"):
                if(self.mem[op1] > self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == "<"):
                if(self.mem[op1] < self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == "=="):
                if(self.mem[op1] == self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == ">="):
                if(self.mem[op1] >= self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == "<="):
                if(self.mem[op1] <= self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == "return"):
                self.return_value_stack.append(self.mem[op1])

            # Array operations
            if(op == "ver"):
                if(self.mem[op1] > res or self.mem[op1] < 0):
                    raise NameError("Array limits out of bounds")
            elif(op == "add"):
                self.mem[res] = "*" + str(self.mem[op1] + op2)
            elif(op == "mul"):
                self.mem[res] = self.mem[op1] * op2

            # Function operations
            if(op == "era"):
                self.context[0] = op1
                # Checks if function returns a value
                # if it returns assigns a memory address
                if(res):
                    self.mem[res] = None
                    self.return_dir_stack.append(res)
                    self.context[2].append(res)
                copy_dir = self.save_state(self.context[2])  # Saves memory state and returns next free address
                if(copy_dir == self.stack_dir):  # Function didn't save any variables
                    self.context[1] = [-1, -1]
                else:  # Function saved variables in the stack
                    self.context[1] = [self.stack_dir, copy_dir - 4]
                self.function_call_stack.append(self.context)
                self.stack_dir = copy_dir
            if(op == "param"):
                func_name = self.function_call_stack[-1][0]
                # revisar este pedo
                type = self.functions[func_name][5][res][1]
                dir = self.functions[func_name][5][res][2]
                size = self.functions[func_name][5][res][3]
                if(type[0] == "i" or type[0] == "f"):
                    bytes = 4
                else:
                    bytes = 1
                # Check if operand is a pointer
                if(isinstance(self.mem[op1], str) and self.mem[op1][0] == "*"):
                    op1 = int(self.mem[op1][1:])
                # Copies the whole array to local memory
                for x in range(0, size, bytes):
                    self.mem[dir + x] = self.mem[op1 + x]

            # Printing functions
            if(op == "print"):
                # Check if operand is a pointer
                if(isinstance(self.mem[op1], str) and self.mem[op1][0] == "*"):
                    op1 = int(self.mem[op1][1:])
                print self.mem[op1]

            # Operators that change the instruction pointer
            if(op == "goto"):
                self.instr_ptr = res
            elif(op == "gotoFalse"):
                if(self.mem[op1] == 0):
                    self.instr_ptr = res
                else:
                    self.instr_ptr += 1
            elif(op == "gosub"):
                self.context = [op1, [], []]
                self.instr_ptr_stack.append(self.instr_ptr + 1)
                self.instr_ptr = res
            elif(op == "end"):
                self.stack_dir = self.restore_state()  # Reloads previous values and returns next free address
                if(self.functions[op1][0][0] != "void"):  # Function returns a value
                    self.mem[self.return_dir_stack.pop()] = self.return_value_stack.pop()  # Saves value returned by function
                self.instr_ptr = self.instr_ptr_stack.pop()
            else:
                self.instr_ptr += 1
            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        print "Program finished"