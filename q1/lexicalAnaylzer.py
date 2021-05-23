import ply.lex as lex
import os

tokens = [
    'INT',
    'FLOAT',
    'SCI',
    'VAR',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'INTDIV',
    'POW',
    'GREATER',
    'GREATEREQU',
    'LESS',
    'LESSEUQ',
    'EQUEQU',
    'EQU',
    'NOTEQU',
    'LPAREN',
    'RPAREN'
]


t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_INTDIV = r'\/\/'
t_POW = r'\^'
t_GREATER = r'\>'
t_GREATEREQU = r'\>\='
t_LESS = r'\<'
t_LESSEUQ = r'\<\='
t_NOTEQU = r'\!\='
t_EQUEQU = r'\=\='
t_EQU = r'\='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore = ' \t'

def t_SCI(t):
    r'[\s=]+([+-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+))$'
    t.value = float( t.value )
    t.value = round( t.value , 6)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float( t.value )
    return t

def t_INT(t):
    r'\d+'
    t.value = int( t.value )
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t

def t_error( t ):
    t.type = 'ERR'
    t.lexer.skip(1)
    return t

#not related to pharser
def getType( tok ):
    operation = ["ADD", "SUB","MUL","DIV","INTDIV","GREATER","GREATEREQU","LESS","LESSEUQ","NOTEQU","EQU","LPAREN","RPAREN"]
    if( tok.type == 'INT' or tok.type == 'FLOAT' or tok.type == 'SCI'):
        tok.type = 'NUM'
        return tok

    elif( tok.type == "POW"):
        tok.type = 'pow'
        return tok

    elif( tok.type in operation ):
        tok.type = tok.value
        return tok

    return tok

#check for error
def checkForEror( toks ):
    toksRange = len( toks )-1
    for tok in range( toksRange ):
        if( toks[tok].type == 'ERR' and tok != 0):
            prvTok = toks[ tok-1 ]
            curVal = toks[tok].value[0]
            if( prvTok.type == "VAR" ):
                toks[tok].value =  prvTok.value + curVal
                toks.pop(tok-1)
            else:
                toks[tok].value = curVal

def getOutString( toks ):
    outString = ""
    for tok in toks:
        outString += str(tok.value) + "/" + str(tok.type) + " "
    return outString

#main
fin = open(os.getcwd() + "/input.txt", 'r')
body = fin.read().split("\n")
fin.close()

fin = open(os.getcwd() + "/q1/61090041.tok", 'w')

inputList = body

lexer = lex.lex()
for item in inputList:
    item = item.replace(" ","")
    lexer.input(item)

    outString = ""
    toks = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tok = getType( tok )
        toks.append( tok )

    checkForEror( toks )
    outString = getOutString( toks )
    fin.write(outString + "\n")
fin.close()

print("\n+++++end of lexicalAnaylzer++++\n")