import sys,os
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import tokens
from compilerProject.q1.lexicalAnaylzer import lexer

def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    saveTofile(p[1])

def p_var_assign(p):
    '''
    var_assign : VAR EQU expression
    '''
    p[0] = (p[1], '=', p[3])

def p_expression(p):
    '''
    expression : expression POW expression
               | expression MUL expression
               | expression DIV expression
               | expression SUB expression
               | expression ADD expression
               | expression GREATER expression
               | expression GREATEREQU expression
               | expression LESS expression
               | expression LESSEUQ expression
               | expression EQUEQU expression
               | expression NOTEQU expression
    '''
    p[0] = (p[1], p[2], p[3])

def p_expression_int_float_sci(p):
    '''
    expression : INT
                | FLOAT
                | SCI
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : VAR
    '''
    p[0] = (p[1])

def p_error(p):
    result = str(p.lexer.lineno)
    raise Exception(result)

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def saveTofile(p):
    outString = ""
    for item in range( len(p) ):
        outString += str(p[item])
    print( '(' + outString + ')')
# main
parser = yacc.yacc()
path = os.getcwd()

itemList = ["23+8", "25*0", "5NUM^ 3.0","x=5","10*x","x =y","x!=5"]

for line in range( len(itemList)):
    try:
        itemList[line].replace(" ", "")
        parser.parse( itemList[line] , lexer = lexer)
    except Exception as e:
        error = "Error in line " + str(line + 1) + ", pos " + str(e)
        print(error)
        continue
