import oaf_sem as sem
import oaf_state as state

class Quad:
    def __init__(self):
        self.operator = None
        self.operand1 = None
        self.operand2 = None
        self.result = None

    def set_quad(self, op, op2, op1, res):
        self.operator = op
        self.operand2 = op2
        self.operand1 = op1
        if(op2 == None):
            if(op == "="):
                res[1][0] = sem.get_type(op, res, op1)
            elif(op == "u+" or op == "u-"):
                if(op1[1][0][0] != "i" and op1[1][0][0] != "f"):
                    raise NameError("Number expected, '{0}' received".format(op1[1][0]))
                size = 4
                res = [res, [op1[1][0], state.temp_dir, [size, 1], 't']]
                state.temp_dir -= size
            elif(op == "u!"):
                if(op1[1][0][0] != "b"):
                    raise NameError("Boolean expected, '{0}' received".format(op1[1][0]))
                size = 1
                res = [res, [op1[1][0], state.temp_dir, [size, 1], 't']]
                state.temp_dir -= size
            self.result = res
        else:
            if(op == "len"):
                size = 4
                res = [res, ["int", state.temp_dir, [size, 1], 't']]
            else:
                type = sem.get_type(op, op1, op2)
                if(type[0] == "i" or type[0] == "f"):
                    size = 4
                else:
                    size = 1
                res = [res, [type, state.temp_dir, [size, 1], 't']]
            state.temp_dir -= size
            self.result = res

    # Transforms variables to memory addresses
    def transform(self, t_offset, l_offset):
        if(self.operator == "add" and self.operand2[1][3][1] == "l"):
            self.operand2[0] += l_offset
        if(self.operator == "gosub"):  # Sets the starting quad
            self.result = self.result[0]

        if(isinstance(self.operand1, list)):
            if(self.operand1[1][3][0] == 'g'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3][0] == 'c'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3][0] == 'l'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3][0] == 't'):
                self.operand1 = self.operand1[1][1] + t_offset
            elif(self.operand1[1][3][0] == 's'):
                self.operand1 = self.operand1[0]

        if(isinstance(self.operand2, list)):
            if(self.operand2[1][3][0] == 'g'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3][0] == 'c'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3][0] == 'l'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3][0] == 't'):
                self.operand2 = self.operand2[1][1] + t_offset
            elif(self.operand2[1][3][0] == 's'):
                self.operand2 = self.operand2[0]

        if(isinstance(self.result, list)):
            if(self.result[1][3][0] == 'g'):
                self.result = self.result[1][1]
            elif(self.result[1][3][0] == 'c'):
                self.result = self.result[1][1]
            elif(self.result[1][3][0] == 'l'):
                self.result = self.result[1][1]
            elif(self.result[1][3][0] == 't'):
                self.result = self.result[1][1] + t_offset
            elif(self.result[1][3][0] == 's'):
                self.result = self.result[0]
