import ply.lex as lex
import ply.yacc as yacc
import sys
import queue
from myTables import varTable, funTable
#Lexer
# Lista de Tokens para ForeverAlone
tokens = [
    #Literals (Identificador)
    'ID',     

    #Operators (+,-,*,/,&&,||,>,<,>=,<=,!=)
    'PLUS',
    'MINUS',
    'MULTIPLICATION',
    'DIVISION',
    'AND',
    'OR',
    'GTHAN',
    'LTHAN',
    'GTHANEQ',
    'LTHANEQ',
    'DIFFERENT',

    #Delimitators (;,',',:,{,},[,],(,),")
    'SEMICOLON',
    'COMMA',
    'LBRACKET', 
    'RBRACKET',
    'LSQRBRACKET',
    'RSQRBRACKET', 
    'LPARENTHESIS',
    'RPARENTHESIS',

    #Constants (Integer,  Float, Char, String)
    'CTEI',
    'CTEF',   
    'CTEC', 
    'CTESTRING',

    #Assignment (=)
    'EQUALS'
]

# Lista de Palabras reservadas
reserved = {
    #Strucutral and Functional
    'program': 'PROGRAM',
    'main': 'MAIN',
    'function': 'FUNCTION',
    'void': 'VOID',
    'return': 'RETURN',
    'end': 'END',

    #Conditional
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    
    #Variables
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'string': 'STRING',

    #Cyclic
    'for': 'FOR',
    'while': 'WHILE',
    'from': 'FROM',
    'to': 'TO', 

    #IO
    'print': 'PRINT', 
    'read': 'READ'
}

#Se agregan las reservadas a la lista de tokens para tener una sola lista
tokens += reserved.values()

#Lista de Expresiones regulares
#Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_AND = r'\&&'
t_OR = r'\|\|'
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LTHANEQ = r'<='
t_GTHANEQ = r'>='
t_DIFFERENT = r'!='

#Delimitators
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSQRBRACKET = r'\['
t_RSQRBRACKET = r'\]'

#Assignment
t_EQUALS = r'\='

#Espacios en Blanco
t_ignore = r' '

#Saltos de Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) #Cuenta mal pero se entiende

#Aceptar Indentacion
def t_tabspace(t):
    r'\t+'

# Crear IDs
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# FLOATS
def t_CTEF(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

# INTEGERS
def t_CTEI(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

# CHARS
def t_CTEC(t):
    r"\'[^']\'"
    t.value = t.value[1]
    return t

# STRINGS
def t_CTESTRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    t.value = str(t.value)
    return t

# Verificador de Errores
def t_error(t):
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1)


# Cosas a guardar y pilas
currentVarType = ''
currentVarId = ''
currentFunType = ''
currentFunId = ''

OperandStack = []
TypeStack = []
OperatorsStack = []
#Intancear las clases
funTable = funTable()
varTable = varTable()
#PARSER
#Estrucura del Programa
def p_programa(p):
    '''
    programa : PROGRAM ID addProgram SEMICOLON programa1 END
    '''
    p[0] = 'PROGRAM COMPILED'
def p_addProgram(p):
	''' addProgram : '''
	global currentFunId, currentFunType
	currentFunId = p[-1]
	currentFunType = 'global'
	funTable.addFun(currentFunType, currentFunId, 0, [], [], 0)
def p_programa1(p):
    '''
    programa1 : vars funcion principal 
    '''
def p_principal(p):
    '''
    principal : MAIN addMain LPARENTHESIS parameters RPARENTHESIS vars LBRACKET estatuto RBRACKET
    '''
def p_addMain(p):
	''' addMain : '''
	global currentFunId, currentFunType
	currentFunId = 'main'
	currentFunType = 'void'
	funTable.addFun(currentFunType, currentFunId, 0, [], [], 0)	
#Variables
def p_vars(p):
    '''
    vars : VAR vars1
        | empty
    '''
def p_vars1(p):
    '''
    vars1 : tipo vars2 SEMICOLON varsadd
    '''
def p_vars2(p):
    '''
    vars2 : ID addVariable arr vars3
    '''
def p_vars3(p):
    '''
    vars3 : COMMA vars2
        | empty
    '''
def p_varsadd(p):
    '''
    varsadd : vars1
        | empty
    '''
def p_tipo(p):
    '''
    tipo : INT 
        | FLOAT
        | CHAR 
        | STRING
    '''
    global currentVarType
    currentVarType = p[1]
    global currentFunType
    currentFunType = p[1]

def p_arr(p):
	'''
	arr : LSQRBRACKET CTEI RSQRBRACKET
        | empty
	'''
#Parametros
def p_parameters(p):
    '''
    parameters : parameters2
    	| empty
    '''
def p_parameters2(p):
	'''
	parameters2 : tipo ID addVariable
		| tipo ID addVariable parameters3 
	'''
def p_parameters3(p):
	'''
	parameters3 : COMMA ID addVariable parameters3
		| COMMA tipo ID addVariable parameters3
		| COMMA ID addVariable
		| COMMA tipo ID addVariable
	'''
#Funciones
def p_funcion(p):
	'''
	funcion : FUNCTION tipo ID addFunction LPARENTHESIS parameters RPARENTHESIS vars LBRACKET estatuto retorno RBRACKET funcion
		| FUNCTION VOID ID addFunction LPARENTHESIS parameters RPARENTHESIS vars LBRACKET estatuto RBRACKET funcion
        | empty
	'''
def p_addFunction(p):
	'''addFunction : '''
	global currentFunId
	currentFunId = p[-1]
	global currentFunType
	if p[-2] == 'void':
		currentFunType = 'void'
	funTable.addFun(currentFunType, currentFunId, 0, [], [], 0)
def p_retorno(p):
	'''
	retorno : RETURN ID SEMICOLON
	'''
#Estatutos
def p_estatuto(p):
    '''
    estatuto : estatuto2 estatuto
        | empty
    '''
def p_estatuto2(p):
    '''
    estatuto2 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    ''' 
def p_asignacion(p):
    '''
    asignacion : ID arr EQUALS expresion 
    '''
def p_llamada(p):
    '''
    llamada : ID LPARENTHESIS expresion RPARENTHESIS 
    '''
def p_lectura(p):
    '''
    lectura : READ LPARENTHESIS vars2 RPARENTHESIS
    '''
def p_escritura(p):
    '''
    escritura : PRINT LPARENTHESIS escritura1 RPARENTHESIS
    '''
def p_escritura1(p):
    '''
    escritura1 : expresion escritura2 
    '''
def p_escritura2(p):
    '''
    escritura2 : COMMA escritura1
        | empty 
    '''
def p_for(p):
    '''
    for : FOR LPARENTHESIS FROM asignacion COMMA TO expresion RPARENTHESIS LBRACKET estatuto RBRACKET
    '''
def p_if(p):
    '''
    if : IF LPARENTHESIS expresion RPARENTHESIS THEN LBRACKET estatuto RBRACKET else 
    '''
def p_else(p):
    '''
    else : ELSE LBRACKET estatuto RBRACKET
        | empty
    '''
def p_while(p):
    '''
    while : WHILE LPARENTHESIS expresion RPARENTHESIS LBRACKET estatuto RBRACKET
    '''
#Expresiones
def p_expresion(p):
    '''
    expresion : nexp expresion1
    '''
def p_expresion1(p):
	'''
	expresion1 : OR expresion
		| empty
	'''
def p_nexp(p):
	'''
	nexp : comexp nexp1
	'''
def p_nexp1(p):
	'''
	nexp1 : AND nexp
		| empty
	'''
def p_comexp(p):
	'''
	comexp : sumexp compex1
	'''
def p_compex1(p):
	'''
	compex1 : GTHAN sumexp
		| LTHAN sumexp
		| GTHANEQ sumexp
		| LTHANEQ sumexp
		| DIFFERENT sumexp
		| empty
	'''
def p_sumexp(p):
	'''
	sumexp : mulexp sumexp1
	'''
def p_sumexp1(p):
	'''
	sumexp1 : PLUS sumexp
		| MINUS sumexp
		| empty
	'''
def p_mulexp(p):
	'''
	mulexp : pexp mulexp1
	'''
def p_mulexp1(p):
	'''
	mulexp1 : MULTIPLICATION mulexp
		| DIVISION mulexp
		| empty
	'''
def p_pexp(p):
	'''
	pexp : CTEI
		| CTEF
		| CTEC
		| CTESTRING
		| llamada
		| ID
		| LPARENTHESIS expresion RPARENTHESIS
	'''
def p_addVariable(p):
	'''addVariable : '''
	global currentVarId
	currentVarId = p[-1]
	if(funTable.searchFun(currentFunId)==True):
		funTable.addVartoFun(currentFunId, currentVarType, currentVarId)
	else:
		print("Funcion no enconttrada")
def p_empty(p):
    '''
    empty : 
    '''

    p[0] = None
def p_error(t):
    if t is not None:
        print ("Illegal token at %s, unexpected %s" % (lexer.lineno, t.value))
        parser.errok()
    else:
        print('Unexpected end of file')

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION'),
    ('right', 'EQUALS'),
    ('left', 'AND', 'OR'),
)

#Contruir Lex y Parser
lexer = lex.lex()
parser = yacc.yacc()


def main():
    try:
        filename = 'testFacil.txt'
        file = open(filename, 'r')
        print("Compilando: " + filename)
        content = file.read()
        file.close()
        lexer.input(content)
        while True:
            tok = lexer.token()
            if not tok:
                break
            #print(tok)
        if (parser.parse(content, tracking = True) == 'PROGRAM COMPILED'):
            print ("Compiled")

    except EOFError:
        print(EOFError)
main()