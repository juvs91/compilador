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
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        self.functions = self.obj["functions"]
        self.mem = self.obj["mem"]

        self.max_mem = []

    def load_obj(self, filename):
        f = open(filename, "rb")
        return pickle.load(f)

    # Adds current function variables to stack before calling another one
    # and saves the local variables to the stack
    # If the functions returns a value that value is also stored in the stack
    def save_state(self, *ret_dir):
        copy_dir = self.stack_dir
        for item in self.mem.items()[:]:
            # revisar este pedo
            if(self.local_dir_start <= item[0] < self.stack_dir_start or item[1] != None):
                self.mem[copy_dir] = item[0]  # Copies the memory address
                self.mem[copy_dir + 4] = item[1]  # Copies the value stored in that address
                copy_dir += 8
        self.max_mem.append(len(self.mem))
        return copy_dir

    def restore_state(self):
        dirs = self.function_call_stack.pop()
        if(dirs[1][0] >= 0):  # Restore the local variables
            for i in range(dirs[1][0], dirs[1][1], 8):
                self.mem[self.mem[i]] = self.mem[i + 4]
                del(self.mem[i], self.mem[i + 4])
            # Restore the temporal variables
        return dirs[1][0]

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

            # Function operations
            if(op == "era"):
                # Checks if function returns a value
                # if it returns assigns a memory address
                if(res):
                    self.mem[res] = None
                    self.return_dir_stack.append(res)
                copy_dir = self.save_state(res)  # Saves memory state and returns next free address
                prev_state = [op1, [], []]       # Previous state [function name, [stack begin, stack end], [temporals addresses]]
                if(copy_dir == self.stack_dir):  # Function didn't save any variables
                    prev_state[1] = [-1, -1]     # [stack begin, stack end]
                else:  # Function saved variables in the stack
                    prev_state[1] = [self.stack_dir, copy_dir - 4]
                if(self.mem[res] != None):  # There's a temporal with a result
                    prev_state[2].append(res)
                self.function_call_stack.append(prev_state)
                self.stack_dir = copy_dir
            if(op == "param"):
                func_name = self.function_call_stack[-1][0]
                dir = self.functions[func_name][4][res][0]
                self.mem[dir] = self.mem[op1]

            # Printing functions
            if(op == "print"):
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
                # Map function's memory address to VM
                #for var in self.functions[op1][4]:
                #    self.mem[var[0]] = var[1]
                self.instr_ptr_stack.append(self.instr_ptr + 1)
                self.instr_ptr = res
            elif(op == "end"):
                self.stack_dir = self.restore_state()  # Reloads previous values and returns next free address
                self.mem[self.return_dir_stack.pop()] = self.return_value_stack.pop()  # Saves value returned by function
                self.instr_ptr = self.instr_ptr_stack.pop()
            else:
                self.instr_ptr += 1
            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        print "Program finished", len(self.max_mem), max(self.max_mem)