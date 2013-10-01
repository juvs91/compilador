import ply.yacc as yacc

from lexer import MyLexer


def p_program(self,p):
    '''Program : Declaration FunctionTotal Main'''

def p_functionTotal(self,p):
    '''FunctionTotal : Function
                     | RFunction'''

def p_main(self,p):
    '''Main : MAIN LPAREN RPAREN FBlock'''

def p_declaration(self,p):
    '''Declaration : Primitive Identifier List SEMI
                   | empty'''

def p_list(self,p):
    '''List : Array
            | empty'''

def p_array(self,p):
    '''Array : LBRACKET INTEGER RBRACKET Matrix'''

def p_matrix(self, p):
    '''Matrix : LBRACKET INTEGER RBRACKET
              | empty'''

def p_function(self,p):
    '''Function : VOID Identifier LPAREN ParamList RPAREN FBLock'''

def p_rFunction(self,p):
    '''RFunction : Primitive Identifier LPAREN ParamList RPAREN RFBLock'''

def p_block(self,p):
    '''Block : LBRACE Instruction RBRACE'''

def p_fBlock(self,p):
    '''FBlock : LBRACE Declaration Instruction  RBRACE'''

def p_rFBlock(self,p):
    '''RFBlock : LBRACE Declaration Instruction RETURN SuperExpr SEMI RBRACE'''

def p_loop(self,p):
    '''Loop : LOOP LPAREN SuperExpr RPAREN Block'''

def p_conditional(self,p):
    '''Conditional : IF LPAREN SuperExpr RPAREN Block Else'''

def p_else(self,p):
    '''Else : ELSE Block
            | empty'''

def p_superExpr(self,p):
    '''SuperExpr : Expression LogicalOp'''

def p_logicalOp(self,p):
    '''LogicalOp : OR SuperExpr
                 | AND SuperExpr
                 | empty'''

def p_expression(self,p):
    '''Expression : Expr Comparison'''

def p_comparison(self,p):
    '''Comparison : GREATHAN Expr
                  | LESSTHAN Expr
                  | DIFFERENT Expr
                  | TWOEQUAL Expr
                  | GREATEQUAL Expr
                  | LESSEQUAL Expr
                  | empty'''

def p_expr(self,p):
    '''Expr : Term Op1'''

def p_op1(self,p):
    '''Op1 : PLUS Expr
           | MINUS Expr
           | empty'''

def p_term(self,p):
    '''Term : Factor Op2'''

def p_op2(self,p):
    '''Op2 : TIMES Term
           | DIVIDE Term
           | empty'''

def p_factor(self,p):
    '''Factor : LPAREN SuperExpr RPAREN
              | Op3 Constant'''

def p_op3(self,p):
    '''Op3 : PLUS
           | MINUS
           | empty'''

def p_instruccion(self,p):
    '''Instruction : Loop SEMI
                   | Assign SEMI
                   | Call SEMI
                   | Brush SEMI
                   | Read SEMI
                   | Print SEMI
                   | PenDown SEMI
                   | PenUp  SEMI
                   | Home SEMI
                   | Forward SEMI
                   | Rotate SEMI
                   | Color SEMI
                   | Cirlce SEMI
                   | Arc SEMI
                   | Square SEMI'''

def p_assign(self,p):
    '''Assign : Identifier EQUAL Assignation'''

def p_assignation(self,p):
    '''Assignation : SuperExpr
                   | STRING
                   | Call'''

def p_call(self,p):
    '''Call : Identifier LPAREN Parameters RPAREN'''

def p_read(self,p):
    '''Read : READ LPAREN Type COMMA Identifier RPAREN'''

def p_type(selfmp):
    '''Type : Primitive
            | STRING'''

def p_print(self,p):
    '''Print : PRINT LPAREN Parameters RPAREN'''

def p_parameters(self,p):
    '''Parameters : Params
                  | empty'''

def p_params(self, p):
    '''Params : SuperExpr Params1
              | STRING Params1'''

def p_params_1(self, p):
    '''Params1 : COMMA Params
               | empty'''

def p_brush(self,p):
    '''Brush : BRUSH LPAREN Color COMMA SuperExpr RPAREN'''

def p_color(self,p):
    '''Color : COLOR LPAREN SuperExpr COMMA SuperExpr COMMA SuperExpr RPAREN'''

def p_penDown(self,p):
    '''PendDown : PD LPAREN RPAREN'''

def p_penUp(self,p):
    '''PenUp : PU LPAREN RPAREN'''

def p_home(self,p):
    '''Home : HOME LPAREN RPAREN'''

def p_forward(self,p):
   '''ForWard : FD LPAREN SuperExpr RPAREN'''

def p_rotate(self,p):
   '''Rotate : RT LPAREN SuperExpr RPAREN'''

def p_circle(self,p):
    '''Circle : CIRCLE LPAREN SuperExpr RPAREN'''

def p_arc(self,p):
    '''Arc : ARC LPAREN SuperExpr COMMA SuperExpr RPAREN'''

def p_square(self,p):
    '''Square : SQUARE LPAREN SuperExpr RPAREN'''

def p_paramList(self,p):
    '''ParamList : Param ParamList1'''

def p_paramList_1(self,p):
    '''ParamList1 : COMMA ParamList
                  | empty'''

def p_param(self,p):
    '''Param : Primitive ListP Identifier'''

def p_ListP(self,p):
    '''ListP : ArrayP ArrayP'''

def p_arrayp(self,p):
    '''ArrayP : LBRACE RBRACE
              | empty'''

def p_primitive(self,p):
    '''Primitive : INT
                 | FLOAT
                 | BOOL
                 | CHAR'''

def p_identifier(self,p):
    '''Identifier : ID'''

def p_constant(self,p):
    '''Constant : INTEGER
                | FLOAT
                | Identifier'''  
def p_empty(p):
    'empty :'
    pass 

def p_error(p):
    try:
        print "Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, p.lexpos, p.value)
    except:
        pass


yacc.tokenList = MyLexer.listOfTokens  

parser = yacc.yacc(start = 'Program')

while True:
   try:
       s = raw_input('file > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print result


print MyLexer.listOfTokens
