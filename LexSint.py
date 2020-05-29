import ply.lex as lex
import ply.yacc as yacc
import sys
import queue
from myTables import *
from semanticCube import *
from avail import *
#Lexer
# Lista de Tokens para ForeverAlone
tokens = [
    #Literals (Identificador)
    'ID',     

    #Operators (+,-,*,/,&&,||,>,<,>=,<=,!=,==)
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
    'EQUALS',

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
    'EQUAL'
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
t_EQUALS = r'=='

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
t_EQUAL = r'\='

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

#Pilas para los quads
operandStack = []
typeStack = []
operatorsStack = []
jumpStack = []
quadruples = []
quadruplesMem = []
#Intancear las clases
funTable = funTable()
varTable = varTable()
avail = avail()
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
	currentFunId = 'global'
	currentFunType = 'global'
	funTable.addFun(currentFunType, currentFunId, 0, [], [], 0)
	quad = ('Goto', None, None, 'main')
	quadruples.append(quad)
	operator = operators['Goto']
	quad = (operator, None, None, 'main')
	quadruplesMem.append(quad)
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
	funcion : FUNCTION tipo ID addFunction LPARENTHESIS parameters RPARENTHESIS vars LBRACKET estatuto retorno RBRACKET endFunc funcion
		| FUNCTION VOID ID addFunction LPARENTHESIS parameters RPARENTHESIS vars LBRACKET estatuto RBRACKET endFunc funcion
        | empty
	'''
def p_addFunction(p):
	'''addFunction : '''
	global currentFunId
	currentFunId = p[-1]
	global currentFunType
	if p[-2] != 'void':
		funTable.addVartoFun('global', currentFunType, currentFunId)
	else:
		currentFunType = 'void'
	funTable.addFun(currentFunType, currentFunId, 0, [], [], 0)

def p_endFunc(p):
	''' endFunc : '''
	quad = ('endproc', None, None, None)
	quadruples.append(quad)
	operator = operators['endproc']
	quad = (operator, None, None, None)
	quadruplesMem.append(quad)

def p_retorno(p):
	'''
	retorno : RETURN expresion quadReturn SEMICOLON
	'''
def p_quadReturn(p):
	''' quadReturn : '''
	value = operandStack.pop()
	valueType = typeStack.pop()
	quad = ('return', None, None, value)
	quadruples.append(quad)
	operator = operators['return']
	value = funTable.getVarAddress(currentFunId, value)
	quad = (operator, None, None, value)
	quadruplesMem.append(quad)

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
    asignacion : ID addId arr EQUAL addOperator expresion quadEqual
    '''
def p_llamada(p):
    '''
    llamada : ID requestCallMemory LPARENTHESIS enviarAgrs RPARENTHESIS callQuad
    '''
def p_enviarAgrs(p):
	'''
	enviarAgrs : expresion quadArg enviarAgrs2
		| empty
	'''
def p_enviarAgrs2(p):
	'''
	enviarAgrs2 : COMMA enviarAgrs
		| empty
	'''
def p_requestCallMemory(p):
	''' requestCallMemory : '''
	quad = ('ERA', None, None, p[-1])
	quadruples.append(quad)
	operator = operators['ERA']
	quad = (operator, None, None, p[-1])
	quadruplesMem.append(quad)

def p_quadArg(p):
	''' quadArg : '''
	value = operandStack.pop()
	valueType = typeStack.pop()
	quad = ('param', value, None, -1)
	quadruples.append(quad)
	operator = operators['param']
	value = funTable.getVarAddress(currentFunId, value)
	quad = (operator, value, None, -1)
	quadruplesMem.append(quad)

def p_callQuad(p):
	''' callQuad : '''
	quad = ('Gosub', None, None, p[-5])
	quadruples.append(quad)
	operator = operators['Gosub']

	quad = (operator, None, None, p[-5])
	quadruplesMem.append(quad)

def p_lectura(p):
    '''
    lectura : READ readOperator LPARENTHESIS expresion readQuad RPARENTHESIS
    '''
def p_escritura(p):
    '''
    escritura : PRINT LPARENTHESIS escritura1 RPARENTHESIS
    '''
def p_escritura1(p):
    '''
    escritura1 : printOperator expresion printQuad escritura2 
    '''
def p_escritura2(p):
    '''
    escritura2 : COMMA escritura1
        | empty 
    '''
def p_for(p):
    '''
    for : FOR forOperator asignacion COMMA TO expresion forQuad LBRACKET estatuto RBRACKET endFor
    '''
def p_if(p):
    '''
    if : IF LPARENTHESIS expresion RPARENTHESIS ifQuad THEN LBRACKET estatuto RBRACKET else endIf
    '''
def p_else(p):
    '''
    else : ELSE elseQuad LBRACKET estatuto RBRACKET
        | empty
    '''
def p_while(p):
    '''
    while : WHILE whileOperator LPARENTHESIS expresion RPARENTHESIS whileQuad LBRACKET estatuto RBRACKET endWhile
    '''
#Expresiones
def p_expresion(p):
    '''
    expresion : nexp orQuad expresion1
    '''
def p_expresion1(p):
	'''
	expresion1 : OR addOperator expresion
		| empty
	'''
def p_nexp(p):
	'''
	nexp : comexp andQuad nexp1
	'''
def p_nexp1(p):
	'''
	nexp1 : AND addOperator nexp
		| empty
	'''
def p_comexp(p):
	'''
	comexp : sumexp compQuad compex1 compQuad
	'''
def p_compex1(p):
	'''
	compex1 : GTHAN addOperator sumexp
		| LTHAN addOperator sumexp
		| GTHANEQ addOperator sumexp
		| LTHANEQ addOperator sumexp
		| DIFFERENT addOperator sumexp
		| EQUALS addOperator sumexp
		| empty
	'''
def p_sumexp(p):
	'''
	sumexp : mulexp plusQuad sumexp1
	'''
def p_sumexp1(p):
	'''
	sumexp1 : PLUS addOperator sumexp
		| MINUS addOperator sumexp
		| empty
	'''
def p_mulexp(p):
	'''
	mulexp : pexp multQuad mulexp1
	'''
def p_mulexp1(p):
	'''
	mulexp1 : MULTIPLICATION addOperator mulexp
		| DIVISION addOperator mulexp
		| empty
	'''
def p_pexp(p):
	'''
	pexp : CTEI addOperandCte
		| CTEF addOperandCte
		| CTEC addOperandCte
		| CTESTRING addOperandCte
		| llamada
		| ID addOperandVar
		| LPARENTHESIS expresion RPARENTHESIS
	'''
#########################################################################
#			 	SEMANTICA Y GENERACION DE CODIGO INTERMEDIO			   	#
#########################################################################

############################################
# GENERACION DE CUADRUPLOS CON PRECEDENCIA #
############################################
#AND Y OR
def p_orQuad(p):
	''' orQuad : '''
	global operatorsStack
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == '||'):
			genQuad()
def p_andQuad(p):
	''' andQuad : '''
	global operatorsStack
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == '&&'):
			genQuad()

#COMPARACIONES
def p_compQuad(p):
	''' compQuad : '''
	global operatorsStack
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == '>' or operatorsStack[-1] == '<'  or operatorsStack[-1] == '>=' or operatorsStack[-1] == '<=' or operatorsStack[-1] == '==' or operatorsStack[-1] == '!='):
			genQuad()

#MULTIPLICACION Y DIVISION
def p_multQuad(p):
    '''multQuad : '''
    global operatorsStack
    if(len(operatorsStack) > 0):
    	if(operatorsStack[-1] == '*' or operatorsStack[-1] == '/'):
    		genQuad()

#SUMA Y RESTA
def p_plusQuad(p):
    '''plusQuad : '''
    global operatorsStack
    if(len(operatorsStack) > 0):
    	if(operatorsStack[-1] == '+' or operatorsStack[-1] == '-'):
    		genQuad()

#IGUAL
def p_quadEqual(p):
	''' quadEqual : '''
	global operatorsStack, operatorsStack, typeStack, quadruples
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == '='):
			operator = operatorsStack.pop()
			rightVal = operandStack.pop()
			rightType = typeStack.pop()
			leftVal = operandStack.pop()
			leftType = typeStack.pop()
			resType = getType(leftType,rightType,operator)
			if resType != 'error':
				quad = (operator, leftVal, None, rightVal)
				#print('quad equal: ' + str(quad))
				quadruples.append(quad)
				leftVal = funTable.getVarAddress(currentFunId, leftVal)
				rightVal = funTable.getVarAddress(currentFunId, rightVal)
				operator = operators[operator]
				quad = (operator, leftVal, None, rightVal)
				quadruplesMem.append(quad)
			else:
				print("Type missmatch")
				sys.exit()     

############################################
#    CUADRUPLOS LINEALES DE 2 ARGUMENTOS   #
############################################
#PRINT
def p_printOperator(p):
	''' printOperator : '''
	global operatorsStack
	operatorsStack.append('print')
def p_printQuad(p):
	''' printQuad : '''
	global operatorsStack
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == 'print'):
			operator = operatorsStack.pop()
			value = operandStack.pop()
			typeStack.pop()
			quad = (operator, None, None, value)
			quadruples.append(quad)
			operator = operators[operator]
			value = funTable.getVarAddress(currentFunId, value)
			quad = (operator, None, None, value)
			quadruplesMem.append(quad)

#READ
def p_readOperator(p):
	''' readOperator : '''
	global operatorsStack
	operatorsStack.append('read')
def p_readQuad(p):
	''' readQuad : '''
	global operatorsStack
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == 'read'):
			operator = operatorsStack.pop()
			value = operandStack.pop()
			typeStack.pop()
			quad = (operator, None, None, value)
			quadruples.append(quad)
			value = funTable.getVarAddress(currentFunId, value)
			operator = operators[operator]
			quad = (operator, None, None, value)
			#print('print quad: ' + str(quad))
			quadruplesMem.append(quad)

############################################
#   		CUADRUPLOS NO LINEALES		   #
############################################
#IF & IFELSE
def p_ifQuad(p):
	''' ifQuad : '''
	global typeStack, quadruples, jumpStack, funTable
	resType	= typeStack.pop()
	if resType == 'bool':
		value = operandStack.pop()
		quad = ('GotoF', value, None, -1)
		quadruples.append(quad)

		value = funTable.getVarAddress(currentFunId, value)
		operator = operators['GotoF']
		quad = (operator, value, None, -1)
		quadruplesMem.append(quad)
		jumpStack.append(len(quadruples)-1)
	else:
		print("type mismatch")
		sys.exit()

def p_elseQuad(p):
	''' elseQuad : '''
	global quadruples, jumpStack
	quad = ('Goto', None, None, -1)
	quadruples.append(quad)
	operator = operators['Goto']
	quad = (operator, None, None, -1)
	quadruplesMem.append(quad)
	false = jumpStack.pop()
	jumpStack.append(len(quadruples)-1)
	fillQuad(false, -1)

def p_endIf(p):
	''' endIf : '''
	global jumpStack
	end = jumpStack.pop()
	fillQuad(end, -1)

#WHILE
def p_whileOperator(p):
	''' whileOperator : '''
	global operatorsStack, jumpStack
	operatorsStack.append('while')
	jumpStack.append(len(quadruples))

def p_whileQuad(p):
	''' whileQuad : '''
	global typeStack, quadruples, jumpStack
	resType = typeStack.pop()
	if(resType == 'bool'):
		operatorsStack.pop()
		value = operandStack.pop()
		quad = ('GotoF', value, None, -1)
		quadruples.append(quad)

		value = funTable.getVarAddress(currentFunId, value)
		operator = operators['GotoF']
		quad = (operator, value, None, -1)
		quadruplesMem.append(quad)
		jumpStack.append(len(quadruples)-1)
	else: 
		print("type mismatch")
		sys.exit()

def p_endWhile(p):
	''' endWhile : '''
	end = jumpStack.pop()
	ret = jumpStack.pop()
	quad = ('Goto', None, None, ret)
	quadruples.append(quad)
	operator = operators['Goto']
	quad = (operator, None, None, ret)
	quadruplesMem.append(quad)
	fillQuad(end, -1)

#FOR
def p_forOperator(p):
	''' forOperator : '''
	global operatorsStack, jumpStack
	operatorsStack.append('for')
	jumpStack.append(len(quadruples))

def p_forQuad(p):
	''' forQuad : '''
	global typeStack, quadruples, jumpStack
	resType = typeStack.pop()
	if(resType == 'bool'):
		operatorsStack.pop()
		value = operandStack.pop()
		quad = ('GotoF', value, None, -1)
		quadruples.append(quad)
		jumpStack.append(len(quadruples)-1)
	else: 
		print("type mismatch")
		sys.exit()

def p_endFor(p):
	''' endFor : '''
	end = jumpStack.pop()
	ret = jumpStack.pop()
	quad = ('Goto', None, None, -1)
	quadruples.append(quad)
	fillQuad(end, -1)

############################################
#   	  CUADRUPLOS DE FUNCIONES		   #
############################################




#FUNCIONES GENERALES
def genQuad(): 
	global operatorsStack, operandStack, typeStack, quadruples, funTable
	if(len(operatorsStack) > 0):
		if(operatorsStack[-1] == 'print' or operatorsStack[-1] == 'read'): #2Args
			operator = operatorsStack.pop()
			value = operandStack.pop()
			typeStack.pop()
			quad = (operator, None, None, value)
			#print('print quad: ' + str(quad))
			quadruples.append(quad)
		elif(operatorsStack[-1] != '='): #4Args
			operator = operatorsStack.pop()
			rightVal = operandStack.pop()
			rightType = typeStack.pop()
			leftVal = operandStack.pop()
			leftType = typeStack.pop()
			resType = getType(leftType, rightType, operator)
			if(resType != 'error'):
				result = avail.next()
				funTable.addTempVar(currentFunId, resType, result)
				quad = (operator, leftVal, rightVal, result)
				#print('quad: ' + str(quad))
				quadruples.append(quad)
				operandStack.append(result)
				typeStack.append(resType)


				leftVal = funTable.getVarAddress(currentFunId, leftVal)
				rightVal = funTable.getVarAddress(currentFunId, rightVal)
				result = funTable.getVarAddress(currentFunId, result)
				operator = operators[operator]
				quad = (operator, leftVal, rightVal, result)
				quadruplesMem.append(quad)


			else:
				print("type mismatch")
				sys.exit()

def p_addOperator(p):
	''' addOperator : '''
	global operatorsStack
	operatorsStack.append(p[-1])

def p_addVariable(p):
	'''addVariable : '''
	global currentVarId
	currentVarId = p[-1]
	if(funTable.searchFun(currentFunId)==True):
		funTable.addVartoFun(currentFunId, currentVarType, currentVarId)
	else:
		print("Funcion no encontrada")

def p_addOperandVar(p):
	''' addOperandVar : '''
	global operandStack, operatorsStack ,currentFunId
	res = funTable.getVarType(currentFunId, p[-1])
	if res != False:
		typeStack.append(res)
		operandStack.append(p[-1])
	else:
		sys.exit()

def p_addOperandCte(p):
	''' addOperandCte : '''
	global operandStack, operatorsStack, funTable
	res = type(p[-1])
	if res == int:
		typeStack.append('int')
		funTable.addCtetoFun(currentFunId, 'int', p[-1])
	elif res == float:
		typeStack.append('float')
		funTable.addCtetoFun(currentFunId, 'float', p[-1])
	elif res == str:
		if(len(p[-1])>1):
			typeStack.append('string')
			funTable.addCtetoFun(currentFunId, 'string', p[-1])
		else:
			typeStack.append('char')
			funTable.addCtetoFun(currentFunId, 'char', p[-1])
	operandStack.append(p[-1])


def p_addId(p):
	''' addId : '''
	global currentVarId, funTable
	currentVarId = p[-1]
	if(funTable.searchVarinFun(currentFunId, currentVarId)):
		typeStack.append(funTable.getVarType(currentFunId, currentVarId))
		operandStack.append(currentVarId)
	else:
		sys.exit()

def fillQuad(end, cont):
	global quadruples, quadruplesMem
	t = list(quadruples[end])
	t[3] = len(quadruples)
	quadruples[end] = tuple(t)
	t = list(quadruplesMem[end])
	t[3] = len(quadruplesMem)
	quadruplesMem[end] = tuple(t)
	#print('quad fill' + str(quadruples[end]))

def p_empty(p):
    '''
    empty : 
    '''

    p[0] = None
def p_error(t):
    if t is not None:
        print ("Illegal token at %s, unexpected %s" % (lexer.lineno, t.value))
        parser.errok()
        sys.exit()
    else:
        print('Unexpected end of file')

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION'),
    ('right', 'EQUAL'),
    ('left', 'AND', 'OR'),
)

#Contruir Lex y Parser
lexer = lex.lex()
parser = yacc.yacc()


def main():
	try:
		#Usare .c para que mi editor lo despliegue mejor
		filename = 'NoFunctions.c'
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

	#print(funTable.getVarType('suma', 'res'))
	print("CUADRUPLOS")
	print(*quadruplesMem, sep = "\n") 

	print(*typeStack, sep = ", ") 
	print(*operandStack, sep = ", ") 
	print(*operatorsStack, sep = ", ")

	print(*quadruples, sep = "\n")

	print(funTable.getVarAddress('global', 'f'))
    #Llamando a Cubo semantico de 2 maneras 
    #print(semanticCube['float']['float']['=='])
    #print(getType('float','int','>'))

main()