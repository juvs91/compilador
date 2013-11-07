import cPickle as pickle

class VirtualMachine:
    def __init__(self, filename):
        self.instr_ptr = 0
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        #self.globals = self.obj["globals"]
        self.functions = self.obj["functions"]
        #self.heap = {}
        self.mem = self.obj["mem"]

    def load_obj(self, filename):
        f = open(filename, "rb")
        return pickle.load(f)

    def run(self):
        quad = self.quads[self.instr_ptr]
        op = quad.operator
        op1 = quad.operand1
        op2 = quad.operand2
        res = quad.result
        while(op != "end" or op1 != "main"):
            if(op == "+"):
                self.mem[res] = str(self.mem[op1]) + "+" + str(self.mem[op2])
            elif(op == "-"):
                self.mem[res] = str(self.mem[op1]) + "-" + str(self.mem[op2])
            elif(op == "*"):
                self.mem[res] = str(self.mem[op1]) + "*" + str(self.mem[op2])
            elif(op == "/"):
                self.mem[res] = str(self.mem[op1]) + "/" + str(self.mem[op2])

            # Function operations
            if(op == "era")

            # Operators that change the instruction pointer
            if(op == "goto"):
                self.instr_ptr = res
            elif(op == "gosub"):
                self.instr_ptr = self.functions[op1][3]
            else:
                self.instr_ptr += 1
            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        print "Program finished"