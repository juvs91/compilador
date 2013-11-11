import cPickle as pickle

class VirtualMachine:
    def __init__(self, filename, stack_address):
        self.instr_ptr = 0  # Current quad
        self.instr_ptr_stack = []  # Stack used when returning to previous instruction
        self.function_call_stack = []  # Stack of function calls
        self.return_dir = -1  # Address to save value to
        self.return_stack = []  # Hold values returned by functions
        self.stack_dir = stack_address  # Address to start the stack
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        self.functions = self.obj["functions"]
        #self.heap = {}
        self.mem = self.obj["mem"]

    def load_obj(self, filename):
        f = open(filename, "rb")
        return pickle.load(f)

    # Adds current function variables to stack before calling another one
    def save_state(self):
        copy_dir = self.stack_dir
        for item in self.mem.items()[:]:
            if(item[0] >= self.stack_dir):
                self.mem[copy_dir] = item[0]  # Copies the memory address
                self.mem[copy_dir + 4] = item[1]  # Copies the value stored in that address
                copy_dir += 8
        return copy_dir

    def restore_state(self):
        dirs = self.function_call_stack.pop()
        if(dirs[1] >= 0):  # There's something to restore
            for i in range(dirs[1], dirs[2], 8):
                self.mem[self.mem[i]] = self.mem[i + 4]
                del(self.mem[i], self.mem[i + 4])

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
            elif(op == "return"):
                #self.mem[self.return_dir] = self.mem[op1]
                self.return_stack.append([self.return_dir, self.mem[op1]])

            # Function operations
            if(op == "era"):
                copy_dir = self.save_state()  # Returns next free address
                if(copy_dir == self.stack_dir):  # Function didn't save any variables
                    self.function_call_stack.append([op1, -1, -1])  # [function name, stack begin, stack end]
                else:  # Fimction saved variables in the stack
                    self.function_call_stack.append([op1, self.stack_dir, copy_dir - 4])
                self.stack_dir = copy_dir
                if(res):  # Checks if function returns a value
                    self.mem[res] = 'ret'
                    self.return_dir = res
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
                ## Map function memory address to VM
                #for var in self.functions[op1][4]:
                #    self.mem[var[0]] = var[1]
                self.instr_ptr_stack.append(self.instr_ptr + 1)
                self.instr_ptr = res
            elif(op == "end"):
                self.restore_state()  # Reloads previous values
                ret = self.return_stack.pop()
                self.mem[ret[0]] = ret[1]  # Saves value returned by function
                self.instr_ptr = self.instr_ptr_stack.pop()
            else:
                self.instr_ptr += 1
            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        print "Program finished"