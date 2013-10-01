import ply.yacc as yacc

from lexer import MyLexer

class Sintax():

    tokens = MyLexer.tokens

    def __init__(self):
        l =[]

    def p_program(p):
        '''Program : Declaration FunctionTotal Main'''

    def p_functionTotal(p):
        '''FunctionTotal : Function
                         | RFunction'''

    def p_main(p):
        '''Main : MAIN LPAREN RPAREN FBlock'''

    def p_declaration(p):
        '''Declaration : Primitive Identifier List SEMI
                       | empty'''

    def p_list(p):
        '''List : Array
                | empty'''

    def p_array(p):
        '''Array : LBRACKET INTEGER RBRACKET Matrix'''

    def p_matrix(p):
        '''Matrix : LBRACKET INTEGER RBRACKET
                  | empty'''

    def p_function(p):
        '''Function : VOID Identifier LPAREN ParamList RPAREN FBlock'''

    def p_rFunction(p):
        '''RFunction : Primitive Identifier LPAREN ParamList RPAREN RFBlock'''

    def p_block(p):
        '''Block : LBRACE Instruction RBRACE'''

    def p_fBlock(p):
        '''FBlock : LBRACE Declaration Instruction  RBRACE'''

    def p_rFBlock(p):
        '''RFBlock : LBRACE Declaration Instruction RETURN SuperExpr SEMI RBRACE'''

    def p_loop(p):
        '''Loop : LOOP LPAREN SuperExpr RPAREN Block'''

    def p_conditional(p):
        '''Conditional : IF LPAREN SuperExpr RPAREN Block Else'''

    def p_else(p):
        '''Else : ELSE Block
                | empty'''

    def p_superExpr(p):
        '''SuperExpr : Expression LogicalOp'''

    def p_logicalOp(p):
        '''LogicalOp : OR SuperExpr
                     | AND SuperExpr
                     | empty'''

    def p_expression(p):
        '''Expression : Expr Comparison'''

    def p_comparison(p):
        '''Comparison : GREATHAN Expr
                      | LESSTHAN Expr
                      | DIFFERENT Expr
                      | TWOEQUAL Expr
                      | GREATEQUAL Expr
                      | LESSEQUAL Expr
                      | empty'''

    def p_expr(p):
        '''Expr : Term Op1'''

    def p_op1(p):
        '''Op1 : PLUS Expr
               | MINUS Expr
               | empty'''

    def p_term(p):
        '''Term : Factor Op2'''

    def p_op2(p):
        '''Op2 : TIMES Term
               | DIVIDE Term
               | empty'''

    def p_factor(p):
        '''Factor : LPAREN SuperExpr RPAREN
                  | Op3 Constant'''

    def p_op3(p):
        '''Op3 : PLUS
               | MINUS
               | empty'''

    def p_instruccion(p):
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
                       | Circle SEMI
                       | Arc SEMI
                       | Square SEMI'''

    def p_assign(p):
        '''Assign : Identifier EQUAL Assignation'''

    def p_assignation(p):
        '''Assignation : SuperExpr
                       | STRING
                       | Call'''

    def p_call(p):
        '''Call : Identifier LPAREN Parameters RPAREN'''

    def p_read(p):
        '''Read : READ LPAREN Type COMMA Identifier RPAREN'''

    def p_type(p):
        '''Type : Primitive
                | STRING'''

    def p_print(p):
        '''Print : PRINT LPAREN Parameters RPAREN'''

    def p_parameters(p):
        '''Parameters : Params
                      | empty'''

    def p_params(p):
        '''Params : SuperExpr Params1
                  | STRING Params1'''

    def p_params_1(p):
        '''Params1 : COMMA Params
                   | empty'''

    def p_brush(p):
        '''Brush : BRUSH LPAREN Color COMMA SuperExpr RPAREN'''

    def p_color(p):
        '''Color : COLOR LPAREN SuperExpr COMMA SuperExpr COMMA SuperExpr RPAREN'''

    def p_penDown(p):
        '''PenDown : PD LPAREN RPAREN'''

    def p_penUp(p):
        '''PenUp : PU LPAREN RPAREN'''

    def p_home(p):
        '''Home : HOME LPAREN RPAREN'''

    def p_forward(p):
       '''Forward : FD LPAREN SuperExpr RPAREN'''

    def p_rotate(p):
       '''Rotate : RT LPAREN SuperExpr RPAREN'''

    def p_circle(p):
        '''Circle : CIRCLE LPAREN SuperExpr RPAREN'''

    def p_arc(p):
        '''Arc : ARC LPAREN SuperExpr COMMA SuperExpr RPAREN'''

    def p_square(p):
        '''Square : SQUARE LPAREN SuperExpr RPAREN'''

    def p_paramList(p):
        '''ParamList : Param ParamList1'''

    def p_paramList_1(p):
        '''ParamList1 : COMMA ParamList
                      | empty'''

    def p_param(p):
        '''Param : Primitive ListP Identifier'''

    def p_ListP(p):
        '''ListP : ArrayP ArrayP'''

    def p_arrayp(p):
        '''ArrayP : LBRACE RBRACE
                  | empty'''

    def p_primitive(p):
        '''Primitive : INT
                     | FLOAT
                     | BOOL
                     | CHAR'''

    def p_identifier(p):
        '''Identifier : ID'''

    def p_constant(p):
        '''Constant : INTEGER
                    | FLOAT
                    | Identifier'''
                    
    def p_empty(p):
        '''empty : '''
        pass
        
    # Error rule for syntax errors
    def p_error(p):
        try:
            print "Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, p.lexpos, p.value)
        except:
            pass
                    
    # Build the parser
    parser = yacc.yacc()

    with open(raw_input('filename > '), 'r') as f:
        result = parser.parse(f.read())
        print result

#print MyLexer.listOfTokens
