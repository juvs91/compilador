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
                res[1][0] = sem.get_type(op, op1, res)
            self.result = res
        else:
            type = sem.get_type(op, op1, op2)
            if(type[0] == "i" or type[0] == "f"):
                size = 4
            else:
                size = 1
            # Check if result is of pointer type
            if(res[0] == "p"):
                self.result = [res, [type, state.temp_dir, [size, 1], 's']]
            else:
                self.result = [res, [type, state.temp_dir, [size, 1], 't']]
            state.temp_dir -= size

    #def add_offset(self, g_offset, c_offset, l_offset, t_offset):
    #    if(isinstance(self.operand1, list)):
    #        if(self.operand1[1][3] == 'g'):
    #            self.operand1[1][1] += g_offset
    #        elif(self.operand1[1][3] == 'c'):
    #            self.operand1[1][1] += c_offset
    #        elif(self.operand1[1][3] == 'l'):
    #            self.operand1[1][1] += l_offset
    #        else:
    #            self.operand1[1][1] += t_offset
    #
    #    if(isinstance(self.operand2, list)):
    #        if(self.operand2[1][3] == 'g'):
    #            self.operand2[1][1] += g_offset
    #        elif(self.operand2[1][3] == 'c'):
    #            self.operand2[1][1] += c_offset
    #        elif(self.operand2[1][3] == 'l'):
    #            self.operand2[1][1] += l_offset
    #        else:
    #            self.operand1[1][1] += t_offset
    #
    #    if(isinstance(self.result, list)):
    #        if(self.result[1][3] == 'g'):
    #            self.result[1][1] += g_offset
    #        elif(self.result[1][3] == 'c'):
    #            self.result[1][1] += c_offset
    #        elif(self.result[1][3] == 'l'):
    #            self.result[1][1] += l_offset
    #        else:
    #            self.result[1][1] += t_offset

    # Transforms variables to memory addresses
    def transform(self, t_offset):
        if(isinstance(self.operand1, list)):
            if(self.operand1[1][3] == 'g'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3] == 'c'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3] == 'l'):
                self.operand1 = self.operand1[1][1]
            elif(self.operand1[1][3] == 't'):
                self.operand1 = self.operand1[1][1] + t_offset
            elif(self.operand1[1][3] == 's'):
                self.operand1 = self.operand1[0]

        if(isinstance(self.operand2, list)):
            if(self.operand2[1][3] == 'g'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3] == 'c'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3] == 'l'):
                self.operand2 = self.operand2[1][1]
            elif(self.operand2[1][3] == 't'):
                self.operand2 = self.operand2[1][1] + t_offset
            elif(self.operand2[1][3] == 's'):
                self.operand2 = self.operand2[0]

        if(isinstance(self.result, list)):
            if(self.result[1][3] == 'g'):
                self.result = self.result[1][1]
            elif(self.result[1][3] == 'c'):
                self.result = self.result[1][1]
            elif(self.result[1][3] == 'l'):
                self.result = self.result[1][1]
            elif(self.result[1][3] == 't'):
                self.result = self.result[1][1] + t_offset
            elif(self.result[1][3] == 's'):
                self.result = self.result[0]