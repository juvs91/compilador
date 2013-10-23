import oaf_sem as sem

class Quad:
    def __init__(self):
        self.operator = None
        self.operand1 = None
        self.operand2 = None
        self.result = None

    def set_quad(self, op, op2, op1, res):
        print op, op1, op2, res
        self.operator = op
        self.operand2 = op2
        self.operand1 = op1
        if(op2 == None):
            if(op != "read" and op != "print"):
                res[1][0] = sem.get_type(op, op1, res)
            self.result = res
        else:
            self.result = [res, [sem.get_type(op, op1, op2)]]