import sys
import os
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import lexer
from compilerProject.q1.lexicalAnaylzer import tokens

variable = {}
register = {}
stringToFile = ""
writeFile = open("./q3/61090041.asm", 'w')
writeFile.close()

writeFile = open("./q3/61090041.asm", 'a')

precedence = (
    ('left', 'GREATER', 'GREATEREQU', 'LESS', 'LESSEUQ', 'EQUEQU', 'NOTEQU'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV', 'INTDIV'),
    ('left', 'POW')
)


def addString(string):
    global stringToFile
    stringToFile += string + '\n'


def addTofile():
    global stringToFile
    global stringToFile
    writeFile.write(stringToFile + '\n')


def addRegister(value):
    global register
    register[value] = len(register)


def getReister(value):
    global register
    return register[value]


def calculateValue(trub):
    for item in trub:
        if(type(item) == float):
            return 1.0
        if(item == "/"):
            return 1.0
    return 1


def getOperation(operation):
    if(operation == "*"):
        return "MUL."
    elif(operation == "+"):
        return "ADD."
    elif(operation == "-"):
        return "SUB."
    elif(operation == "/"):
        return "DIV."
    elif(operation == "//"):
        return "DIV."
    elif(operation == "=="):
        return "EQ.f"
    elif(operation == "!="):
        return "NE.f"
    elif(operation == ">"):
        return "GT.f"
    elif(operation == ">="):
        return "GE.f"
    elif(operation == "<"):
        return "LT.f"
    elif(operation == "<="):
        return "LE.f"
    elif(operation == "=="):
        return "EQ.f"
    elif(operation == "!="):
        return "NE.f"


def p_calc(p):
    '''
    calc : expression
         | var_assign
         | empty
    '''
    global register
    global variable
    global stringToFile
    if(len(p[1]) <= 1):
        addString(f"ST @print R{len(register)-1}")
        addTofile()
        stringToFile = ""

    elif((p[1][1]) != "="):
        addString(f"ST @print R{len(register)-1}")
        addTofile()
        stringToFile = ""

    register = {}


def p_var_assign(p):
    '''
    var_assign : VAR EQU expression
    '''
    p[0] = (p[1], '=', p[3])
    global variable

    new_varable = str(p[3])
    if(not new_varable.isdigit()):
        if(new_varable not in variable):
            result = str(abs(p.lexer.lexpos-2))
            raise Exception(result)

    variable[p[1]] = p[3]

    addString(f"ST @{p[1]} R{getReister(p[3])}" + '\n')
    variable[p[1]] = p[3]


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
    temp = p[1]
    if(type(p[1]) == tuple):
        p[1] = calculateValue(p[1])

    operation = getOperation(p[2])
    global variable
    global register
    exp1 = p[1]
    exp2 = p[3]
    reg1 = getReister(p[1])
    reg2 = getReister(p[3])
    addRegister((temp, p[3]))
    newReg = getReister((temp, p[3]))
    newReg = len(register) - 1

    if((type(exp1) == str)):
        exp1 = variable[exp1]

    if(type(exp2) == str):
        exp2 = variable[exp2]

    if(p[2] in ["==", '!=', '<', '<=', '>', '>=']):
        if(isinstance(exp1, int)):
            addString(f"FL.i R{reg1} R{reg1}")

        if(isinstance(exp2, int)):
            addString(f"FL.i R{reg2} R{reg2}")

        addString(f"{operation} R{newReg} R{reg1} R{reg2}")

    elif(isinstance(exp1, int) and isinstance(exp2, int)):
        addString(f"{operation}i R{newReg} R{reg1} R{reg2}")

    elif(isinstance(exp1, int)):
        addString(f"FL.i R{reg1} R{reg1}")
        addString(f"{operation}f R{newReg} R{reg1} R{reg2}")

    elif(isinstance(exp2, int)):
        addString(f"FL.i R{'1'} R{'1'}")
        addString(f"{operation}f R{newReg} R{reg1} R{reg2}")

    else:
        addString(f"{operation}f R{newReg} R{reg1} R{reg2}")


def p_expression_int_float_sci(p):
    '''
    expression : INT
               | FLOAT
               | SCI
               | parentheses
    '''
    p[0] = p[1]

    if(type(p[1]) != tuple):
        addRegister(p[1])
        addString(f"LD R{getReister(p[1])} #{p[1]}")


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
    pValue = p[1]
    global variable
    if(p[1] in variable):
        addRegister(pValue)
        addString(f"LD R{getReister(pValue)} @{pValue}")


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
        parser.parse(itemList[line], lexer=lexer)
    except Exception as e:
        register = {}
        error = "ERROR\n\n"
        writeFile.write(error)
        continue

writeFile.close()
print("\n+++++end of condegenerator++++\n")
