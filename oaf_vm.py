import cPickle as pickle
import turtle

class VirtualMachine:
    def __init__(self, filename, local_address, stack_address, heap_address):
        self.color_list = []#the list of colors
        self.instr_ptr = 0  # Current quad
        self.instr_ptr_stack = []  # Stack used when returning to previous instruction
        self.function_call_stack = []  # Stack of function calls
        self.return_dir_stack = []  # Address to save value to
        self.return_value_stack = []  # Value to save at address
        self.local_dir_start = local_address  # Address to start the local variables
        self.stack_dir_start = stack_address  # Address to start the stack
        self.stack_dir = stack_address  # Next free address to start continue stack
        self.heap_dir = heap_address  # Last used temporal address
        self.context = ["main", [], []]  # [function name, [stack begin, stack end], [{temporals list}]]
        # Loads the object code and initializes the virtual machine
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        self.functions = self.obj["functions"]
        self.mem = self.obj["mem"]

        # List of memory addresses
        self.mem_map = {}
        self.grafic_used = False  # variable to seet main loop if any grafic comands are used

        # Operators list
        self.op_list = ["u+", "u-", "=", "+", "-", "*", "/", "<", ">", "<=", ">=", "<>", "==", "||", "&&", "print", "param", "return"]

    def square(self, size):
        for i in range(4):
            turtle.fd(size)
            turtle.rt(90)

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
            if (self.local_dir_start <= item[0] < self.stack_dir_start):
                self.mem[copy_dir] = item[0]  # Copies the memory address
                self.mem[copy_dir + 4] = item[1]  # Copies the value stored in that address
                copy_dir += 8
        for item in temporals:
            if (self.mem[item] != None):
                self.mem[copy_dir] = item  # Copies the memory address
                self.mem[copy_dir + 4] = self.mem[item]  # Copies the value stored in that address
                copy_dir += 8
        if (copy_dir > self.heap_dir):  # If addresses collide
            raise NameError("Stack buffer overflow")
        return copy_dir

    def restore_state(self):
        self.context = self.function_call_stack.pop()
        dirs = self.context[1]
        if (dirs[0] >= 0):  # There's something to restore
            for i in range(dirs[0], dirs[1], 8):
                self.mem[self.mem[i]] = self.mem[i + 4]
                del (self.mem[i], self.mem[i + 4])
            return dirs[0]  # Something was restored
        else:
            return self.stack_dir  # Nothing was restored

    def init_func(self, func_name):
        # Initializes local variables
        self.mem_map = {}
        # Adds all the used addresses to the dictionary
        for var in self.functions[func_name][5].items():
            # Check if variable is an array
            if ("[]" in var[1][0]):
                if (var[1][0][0] == "i" or var[1][0][0] == "f"):
                    step = 4
                else:
                    step = 1
                for x in range(0, var[1][2], step):
                    self.mem_map[var[1][1] + x] = None
            else:
                self.mem_map[var[1][1]] = None

    def copy_mem(self):
        # Clears the local memory
        for dir in range(self.local_dir_start, self.stack_dir_start):
            if (dir in self.mem):
                del (self.mem[dir])
        # Adds the variables to memory
        self.mem.update(self.mem_map)

    def run(self):
        quad = self.quads[self.instr_ptr]
        op = quad.operator
        op1 = quad.operand1
        op2 = quad.operand2
        res = quad.result
        while (op != "end" or op1 != "main"):
            if(op in self.op_list):
                if (self.mem.get(op1) != None and isinstance(self.mem[op1], str) and self.mem[op1][0] == "*"):
                    op1 = int(self.mem[op1][1:])
                if (self.mem.get(op2) != None and isinstance(self.mem[op2], str) and self.mem[op2][0] == "*"):
                    op2 = int(self.mem[op2][1:])
                if (self.mem.get(res) != None and isinstance(self.mem[res], str) and self.mem[res][0] == "*"):
                    res = int(self.mem[res][1:])
            if(op == "u+"):
                self.mem[res] = self.mem[op1]
            elif(op == "u-"):
                self.mem[res] = -self.mem[op1]
            elif (op == "+"):
                self.mem[res] = self.mem[op1] + self.mem[op2]
            elif (op == "-"):
                self.mem[res] = self.mem[op1] - self.mem[op2]
            elif (op == "*"):
                self.mem[res] = self.mem[op1] * self.mem[op2]
            elif (op == "/"):
                self.mem[res] = self.mem[op1] / self.mem[op2]
            elif (op == "="):
                self.mem[res] = self.mem[op1]
            elif (op == ">"):
                if (self.mem[op1] > self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "<"):
                if (self.mem[op1] < self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "=="):
                if (self.mem[op1] == self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "<>"):
                if (self.mem[op1] != self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == ">="):
                if (self.mem[op1] >= self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "<="):
                if (self.mem[op1] <= self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "&&"):
                if (self.mem[op1] and self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "||"):
                if (self.mem[op1] or self.mem[op2]):
                    self.mem[res] = "true"
                else:
                    self.mem[res] = "false"
            elif (op == "return"):
                self.return_value_stack.append(self.mem[op1])

            # Array operations
            if (op == "ver"):
                if (self.mem[op1] > res or self.mem[op1] < 0):
                    raise NameError("Array limits out of bounds")
            elif (op == "add"):
                self.mem[res] = "*" + str(self.mem[op1] + op2)
            elif (op == "mul"):
                self.mem[res] = self.mem[op1] * op2

            # Function operations
            if (op == "era"):
                self.context[0] = op1
                self.init_func(op1)
                # Checks if function returns a value
                # if it returns assigns a memory address
                if (res):
                    self.mem[res] = None
                    self.return_dir_stack.append(res)
                    self.context[2].append(res)
                copy_dir = self.save_state(self.context[2])  # Saves memory state and returns next free address
                if (copy_dir == self.stack_dir):  # Function didn't save any variables
                    self.context[1] = [-1, -1]
                else:  # Function saved variables in the stack
                    self.context[1] = [self.stack_dir, copy_dir - 4]
                self.function_call_stack.append(self.context)
                self.stack_dir = copy_dir
            if (op == "param"):
                func_name = self.function_call_stack[-1][0]
                var = self.functions[func_name][2][res]
                type = self.functions[func_name][5][var][0]
                dir = self.functions[func_name][5][var][1]
                size = self.functions[func_name][5][var][2]
                if (type[0] == "i" or type[0] == "f"):
                    bytes = 4
                else:
                    bytes = 1
                    # Copies the variables to local memory
                for x in range(0, size, bytes):
                    #self.mem[dir + x] = self.mem[op1 + x]
                    self.mem_map[dir + x] = self.mem[op1 + x]
                    # Removes already initialized variables
                    #self.mem_map.remove(dir + x)

            # Printing functions
            if (op == "print"):
                print self.mem[op1]
                #read a variable in a memory addres
            if (op == "read"):
            #if(op1 == "int"):
                response = input("data:")
                if (isinstance(response, int) and op1 != "int" ):
                    raise NameError("Incompatible types '{0}' and '{1}'".format("int", op1))
                if (isinstance(response, float) and op1 != "float"):
                    raise NameError("Incompatible types '{0}' and '{1}'".format("float", op1))
                if (isinstance(response, bool) and op1 != "bool"):
                    raise NameError("Incompatible types '{0}' and '{1}'".format("bool", op1))
                if (isinstance(response, str) and op1 != "char"):
                    raise NameError("Incompatible types '{0}' and '{1}'".format("char", op1))
                self.mem[res] = response

                #all the grafic quads traductions
            if (op == "circle"):
                turtle.circle(self.mem[op1])
                self.grafic_used = True
            if (op == "fd"):
                turtle.forward(self.mem[op1])
                self.grafic_used = True
            if (op == "rt"):
                print "rt"
                turtle.rt(self.mem[op1])
                self.grafic_used = True
            if (op == "square"):
                print "square"
                self.square(self.mem[op1])

                self.grafic_used = True
            if (op == "brush"):
                print "brush"
                turtle.pensize(self.mem[op1])
                self.grafic_used = True
            if (op == "arc"):
                print "arc"

                self.grafic_used = True
            if (op == "pd"):
                print "pd"
                turtle.pd()
                self.grafic_used = True
            if (op == "pu"):
                print "pu"
                turtle.pu()
                self.grafic_used = True
            if (op == "color"):
                self.color_list.append(self.mem[op2])
                if (len(self.color_list) == 3):
                    turtle.pencolor(self.color_list[0], self.color_list[1], self.color_list[2])
                    self.grafic_used = True
            if (op == "home"):
                turtle.home()

            # Operators that change the instruction pointer
            if (op == "goto"):
                self.instr_ptr = res
            elif (op == "gotoFalse"):
                if (self.mem[op1] == "false"):
                    self.instr_ptr = res
                else:
                    self.instr_ptr += 1
            elif (op == "gosub"):
                self.context = [op1, [], []]
                self.instr_ptr_stack.append(self.instr_ptr + 1)
                self.instr_ptr = res
                self.copy_mem()
            elif (op == "end"):
                self.stack_dir = self.restore_state()  # Reloads previous values and returns next free address
                if (self.functions[op1][0][0] != "void"):  # Function returns a value
                    self.mem[
                        self.return_dir_stack.pop()] = self.return_value_stack.pop()  # Saves value returned by function
                self.instr_ptr = self.instr_ptr_stack.pop()
            else:
                self.instr_ptr += 1

            # Updates last temporal variable
            self.heap_dir = min(filter(lambda x: x > self.stack_dir, self.mem.keys()) + [self.heap_dir])
            # Check if heap and stack buffers collided
            if (self.heap_dir < self.stack_dir):
                raise NameError("Heap buffer overflow")
                # Check if memory is full
            if (min(self.mem.keys()) < 0 or self.heap_dir < self.stack_dir):
                raise NameError("Not enough memory")

            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        if (self.grafic_used):
            turtle.mainloop()
        print "Program finished"