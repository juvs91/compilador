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
            self.result = [res, [type, state.temp_dir, size, 't']]
            state.temp_dir += size
        #if(op2 == None):
        #    if(op != "read" and op != "print" and op != "goto" and op != "era" and op != "param" and op != "gosub" and op != "end"):
        #        res[1][0] = sem.get_type(op, op1, res)
        #    self.result = res
        #else:
        #    if(op == "gotoFalse" or op == "gotoTrue" or op == "goto"):
        #        self.result = res
        #    else:
        #        type = sem.get_type(op, op1, op2)
        #        if(type[0] == "i" or type[0] == "f"):
        #            size = 4
        #        else:
        #            size = 1
        #        self.result = [res, [type, state.temp_dir, size, 't']]
        #        state.temp_dir += size

    def add_offset(self, g_offset, c_offset, l_offset, t_offset):
        if(isinstance(self.operand1, list)):
            if(self.operand1[1][3] == 'g'):
                self.operand1[1][1] += g_offset
            elif(self.operand1[1][3] == 'c'):
                self.operand1[1][1] += c_offset
            elif(self.operand1[1][3] == 'l'):
                self.operand1[1][1] += l_offset
            else:
                self.operand1[1][1] += t_offset

        if(isinstance(self.operand2, list)):
            if(self.operand2[1][3] == 'g'):
                self.operand2[1][1] += g_offset
            elif(self.operand2[1][3] == 'c'):
                self.operand2[1][1] += c_offset
            elif(self.operand2[1][3] == 'l'):
                self.operand2[1][1] += l_offset
            else:
                self.operand1[1][1] += t_offset

        if(isinstance(self.result, list)):
            if(self.result[1][3] == 'g'):
                self.result[1][1] += g_offset
            elif(self.result[1][3] == 'c'):
                self.result[1][1] += c_offset
            elif(self.result[1][3] == 'l'):
                self.result[1][1] += l_offset
            else:
                self.result[1][1] += t_offset

    def transform(self, g_offset, c_offset, l_offset, t_offset):
        if(isinstance(self.operand1, list)):
            if(self.operand1[1][3] == 'g'):
                self.operand1 = self.operand1[1][1] + g_offset
            elif(self.operand1[1][3] == 'c'):
                self.operand1 = self.operand1[1][1] + c_offset
            elif(self.operand1[1][3] == 'l'):
                self.operand1 = self.operand1[1][1] + l_offset
            else:
                self.operand1 = self.operand1[1][1] + t_offset

        if(isinstance(self.operand2, list)):
            if(self.operand2[1][3] == 'g'):
                self.operand2 = self.operand2[1][1] + g_offset
            elif(self.operand2[1][3] == 'c'):
                self.operand2 = self.operand2[1][1] + c_offset
            elif(self.operand2[1][3] == 'l'):
                self.operand2 = self.operand2[1][1] + l_offset
            else:
                self.operand2 = self.operand2[1][1] + t_offset

        if(isinstance(self.result, list)):
            if(self.result[1][3] == 'g'):
                self.result = self.result[1][1] + g_offset
            elif(self.result[1][3] == 'c'):
                self.result = self.result[1][1] + c_offset
            elif(self.result[1][3] == 'l'):
                self.result = self.result[1][1] + l_offset
            else:
                self.result = self.result[1][1] + t_offset