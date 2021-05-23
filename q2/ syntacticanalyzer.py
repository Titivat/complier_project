import sys
import ply.yacc as yacc
sys.path.append("..")
from compilerProject.q1.lexicalAnaylzer import lexer

def p_start(p):
    '''s : VAR ASSIGNMENT expr
         | expr'''

    if len(p) > 2:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_expr(p):
    '''expr : expr op1 term1
            | term1'''

    if len(p) > 2:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_term1(p):
    '''term1 : term1 op2 term2
             | term2'''

    if len(p) > 2:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_term2(p):
    '''term2 : term2 op3 term3
             | term3'''

    if len(p) > 2:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_term3(p):
    '''term3 : factor EXPONENT term3
             | factor'''

    if len(p) > 2:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]


def p_factor(p):
    '''factor : NUM
              | VAR
              | LPAREN expr RPAREN'''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_op1(p):
    '''op1 : EQUAL
           | NOT_EQUAL
           | GREATER_THAN
           | GREATER_THAN_EQUAL
           | LESS_THAN
           | LESS_THAN_EQUAL'''

    if p[1] == "==":
        p[0] = "=="
    elif p[1] == "!=":
        p[0] = "!="
    elif p[1] == ">":
        p[0] = ">"
    elif p[1] == ">=":
        p[0] = ">="
    elif p[1] == "<":
        p[0] = "<"
    elif p[1] == "<=":
        p[0] = "<="


def p_op2(p):
    '''op2 : ADDITION
           | SUBTRACTION'''

    if p[1] == "+":
        p[0] = "+"
    elif p[1] == "-":
        p[0] = "-"


def p_op3(p):
    '''op3 : MULTIPLICATION
           | DIVISION
           | I_DIVISION'''

    if p[1] == '*':
        p[0] = "*"
    elif p[1] == "/":
        p[0] = "/"
    elif p[1] == "//":
        p[0] = "//"


def p_error(p):
    result = "Error in line " + str(p.lexer.lineno) + ", pos " + str(p.lexer.lexpos)
    raise Exception(result)

def main():
    with open('inputFile2') as f:
        with open('61090017.bracket', 'a') as bracketFile:
            for line in f:
                line = line
                try:
                    string = "(" + line.rstrip() + ")"
                    print(string)
                    bracketFile.write(string + "\n")
                except Exception as e:
                    print(e)
                    bracketFile.write(str(e) + "\n")
                    continue

if __name__ == "__main__":
    main()