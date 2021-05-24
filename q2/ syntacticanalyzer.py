import sys,os
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import tokens
from compilerProject.q1.lexicalAnaylzer import lexer

def p_calc(p):
    '''
    calc : expression
        | empty
    '''
    print(p[1])

def p_expression(p):
    '''
    expression : INT
                | FLOAT
    '''
    p[0] = p[1]

def p_empty( p ):
    '''
    empty :
    '''
    p[0] = None

# main
parser = yacc.yacc()
path = os.getcwd()

itemList = ['1', '10','10H']

for item in itemList:
    try:
        item.replace(" ", "")
    except Exception as e:
        print(e)
        continue
    parser.parse( item )
