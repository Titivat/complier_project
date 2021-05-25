import sys,os
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import tokens
from compilerProject.q1.lexicalAnaylzer import lexer

error_status = ""
variable = {}
undifineVar = ""
writeFile = open( "./q3/61090041.asm", 'w')

precedence = (
    ('left','GREATER','GREATEREQU','LESS','LESSEUQ','EQUEQU','NOTEQU'),
    ('left', 'ADD','SUB'),
    ('left', 'MUL','DIV','INTDIV'),
    ('left', 'POW')
)

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

    if( not str(p[3]).isdigit() ):
        if( str(p[3]) not in variable ):
            global undifineVar
            undifineVar = str(p[3])
            global error_status
            error_status = "undefine"
            result = str( abs(p.lexer.lexpos-2) )
            raise Exception(result)


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

def p_expression_int_float_sci(p):
    '''
    expression : INT
               | FLOAT
               | SCI
               | parentheses
    '''
    p[0] = p[1]

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

openFile = open( "./input.txt", 'r')
body = openFile.read().split("\n")
openFile.close()

itemList = body

for line in range( len(itemList)):
    try:
        itemList[line].replace(" ", "")
        parser.parse( itemList[line] , lexer = lexer)
        writeFile.write( '(' + itemList[line] + ')' + '\n')
    except Exception as e:
        if( error_status == "error" ):
            error = "Error in line " + str(line + 1) + ", pos " + str(e) + '\n'
        else:
            error = "Undefined variable " + undifineVar +" at line "+ str(line + 1) + ", pos " + str(e) + "\n"
        writeFile.write( error )
        continue

print("\n+++++end of syntacticanalyzer++++\n")
