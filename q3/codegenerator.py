import sys
import os
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import lexer
from compilerProject.q1.lexicalAnaylzer import tokens

variable = {}
undifineVar = ""
writeFile = open("./q3/61090041.asm", 'w')

precedence = (
    ('left', 'GREATER', 'GREATEREQU', 'LESS', 'LESSEUQ', 'EQUEQU', 'NOTEQU'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV', 'INTDIV'),
    ('left', 'POW')
)

def getOperation( operation ):
    if( operation == "*" ):
        return "MUL."
    elif( operation == "+"):
        return "ADD."
    elif( operation == "-"):
        return "SUB."
    elif( operation == "/" ):
        return "DIV."
    elif( operation == "//" ):
        return "DIV."
    elif( operation == "==" ):
        return "EQ.f"
    elif( operation == "!=" ):
        return "NE.f"
    elif( operation == ">"):
        return "GT.f"
    elif( operation == ">="):
        return "GE.f"
    elif( operation == "<"):
        return "LT.f"
    elif( operation == "<="):
        return "LE.f"
    elif( operation ==  "=="):
        return "EQ.f"
    elif( operation == "!=" ):
        return "NE.f"

def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''

def p_var_assign(p):
    '''
    var_assign : VAR EQU expression
    '''
    p[0] = (p[1], '=', p[3])
    global variable
    variable[p[1]] = 1

    new_varable = str(p[3])
    if(not new_varable.isdigit()):
        if(new_varable not in variable):
            global undifineVar
            undifineVar = new_varable
            result = str(abs(p.lexer.lexpos-2))
            raise Exception(result)

    print("p_var_assign")
    print(p[1], p[3])
    print(variable)


def p_expression(p):
    '''
    expression : expression POW expression
               | expression MUL expression
               | expression DIV expression
               | expression INTDIV expression
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
    ##
    print('p_expression:')
    if( p[2] in [""]):
        pass
    elif( isinstance(p[1], int) and isinstance(p[3], int)):
        print(f"{'1'}")
    print( p[1], p[2], p[3])

def p_expression_int_float_sci(p):
    '''
    expression : INT
               | FLOAT
               | SCI
               | parentheses
    '''
    p[0] = p[1]
    print('p_expression_int_float_sci:')
    var = "1"
    print(f"LD R{var} #{p[1]}")


def p_parentheses(p):
    '''
    parentheses : LPAREN expression RPAREN
    '''
    p[0] = (p[1], p[2], p[3])


def p_expression_var(p):
    '''
    expression : VAR
    '''
    p[0] = (p[1])
    print('p_expression_var:')
    print( p[1])


def p_error(p):
    result = str(p.lexer.lineno)
    global error_status
    error_status = "error"
    raise Exception(result)


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

# main
parser = yacc.yacc()
path = os.getcwd()

openFile = open("./input.txt", 'r')
body = openFile.read().split("\n")
openFile.close()

itemList = body

for line in range(len(itemList)):
    try:
        itemList[line].replace(" ", "")
        print( itemList[line] + "\n")
        parser.parse(itemList[line], lexer=lexer)
        print("++++++++++++++++++++++++++++")
    except Exception as e:
        error = "ERROR\n"
        writeFile.write(error)
        print("++++++++++++Error+++++++++++++")
        continue

print("\n+++++end of condegenerator++++\n")
