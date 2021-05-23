import logging
from compilerProject.q1.lexicalAnaylzer import tokens
from compilerProject.q1.lexicalAnaylzer import lexer
from compilerProject.ply.yacc import yacc
import sys
import os
import ply.lex as lex
sys.path.append("..")

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()


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
               | STRING
    '''
    p[0] = p[1]


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


# main
parser = yacc.yacc()
path = os.getcwd()

itemList = ['1', '10', '10h']

for item in itemList:
    try:
        item.replace(" ", "")
    except Exception as e:
        print(e)
        continue
    print(item)
