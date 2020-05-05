import ply.lex as lex
import ply.yacc as yacc
import sys
# LEXSINT v3
# Lista de Tokens para Patito++
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
    'COLON',
    'LBRACKET', 
    'RBRACKET',
    'LSQRBRACKET', #FALTA
    'RSQRBRACKET', #FALTA
    'LPARENTHESIS',
    'RPARENTHESIS',
    'QUOTE', #FALTA

    #Constants (Integer,  Float, Char, String)
    'CTEI',
    'CTEF',   
    'CTEC', #FALTA
    'CTESTRING',

    #Assignment (=)
    'EQUALS'
]

# Lista de Palabras reservadas
reserved = {
    # FALTA IMPLEMENTAR
    #Strucutral and Functional
    'program': 'PROGRAM',
    'main': 'MAIN',
    'function': 'FUNCTION',
    'void': 'VOID',
    'return': 'RETURN',
    'end': 'END', #FALTA

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
    'from': 'FROM', #FALTA
    'to': 'TO', #FALTA

    #IO
    'print': 'PRINT', #FALTA
    'read': 'READ' #FALTA
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
t_COLON = r'\:'
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSQRBRACKET = r'\['
t_RSQRBRACKET = r'\]'
t_QUOTE = r'\"'

#Assignment
t_EQUALS = r'\='

#Espacios en Blanco
t_ignore = r' '

#Saltos de Linea
def t_newline(t):
    r'\n+'
#Ignorar Indentacion
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


lexer = lex.lex()

'''
Quick Lexer Test 
lexer.input("ab3 = 'a'")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''
def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON programa1
    '''
    p[0] = 'SUCCESS'
def p_programa1(p):
    '''
    programa1 : decvars bloque programa2
    programa1 : decvars bloque
  			  | programa2
    '''
def p_programa2(p):
    '''
    programa2 :  principal
    ''' 
def p_principal(p):
    '''
    principal : MAIN LPARENTHESIS parameters RPARENTHESIS LBRACKET decvars estatuto RBRACKET END
    '''   
def p_decvars(p):
	'''
	decvars : multivars
			| empty
	'''
def p_multivars(p):
	'''
	multivars : vars 
			| vars multivars
	'''
def p_vars(p):
    '''
    vars : VAR tipo ID SEMICOLON 
    	 | VAR tipo ID vars1
    	 | VAR tipo ID arr SEMICOLON
    	 | VAR tipo ID arr vars1 
    '''
def p_vars1(p):
	'''
	vars1 : COMMA ID vars1
		  | COMMA ID SEMICOLON
		  | COMMA ID arr vars1 
		  | COMMA ID arr SEMICOLON

	'''
def p_tipo(p):
    '''
    tipo : INT 
        | FLOAT
        | CHAR 
        | STRING
    '''
def p_arr(p):
	'''
	arr : LSQRBRACKET CTEI RSQRBRACKET
	'''
def p_parameters(p):
    '''
    parameters : parameters2
    	| empty
    '''
def p_parameters2(p):
	'''
	parameters2 : tipo ID
		| tipo ID parameters3 
	'''
def p_parameters3(p):
	'''
	parameters3 : COMMA ID parameters3
			| COMMA tipo ID parameters3
			| COMMA ID
			| COMMA tipo ID
	'''
def p_bloque(p):
    '''
    bloque : funcion
    	| funcion bloque 
    	| empty
    
    '''
def p_funcion(p):
	'''
	funcion : FUNCTION tipo ID LPARENTHESIS parameters RPARENTHESIS LBRACKET decvars estatuto retorno RBRACKET
		| FUNCTION VOID ID LPARENTHESIS parameters RPARENTHESIS LBRACKET decvars estatuto RBRACKET
	'''
def p_retorno(p):
	'''
	retorno : RETURN ID SEMICOLON
	'''
def p_estatuto(p):
    '''
    estatuto : estatuto2 
    	| empty
    '''
def p_estatuto2(p):
	'''
	estatuto2 : estatuto3
		| estatuto3 estatuto2 
	'''
def p_estatuto3(p):
    '''
    estatuto3 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    ''' 
def p_asignacion(p):
	'''
	asignacion : ID EQUALS expresion 
		| ID arr EQUALS expresion
	'''
def p_llamada(p):
	'''
	llamada : ID LPARENTHESIS expresion RPARENTHESIS 
	'''
def p_lectura(p):
	'''
	lectura : READ LPARENTHESIS leevars RPARENTHESIS
	'''
def p_leevars(p):
	'''
	leevars : ID
		| ID COMMA leevars
		| ID arr
		| ID arr COMMA leevars
	'''
def p_escritura(p):
	'''
	escritura : PRINT LPARENTHESIS escritura1 RPARENTHESIS
	'''
def p_escritura1(p):
	'''
	escritura1 : escritura2 
		| escritura2 COMMA escritura1
	'''
def p_escritura2(p):
	'''
	escritura2 : CTEI
		| CTEF
		| CTESTRING
		| CTEC
		| expresion 
	'''
def p_for(p):
	'''
	for : FOR LPARENTHESIS FROM asignacion COMMA TO expresion RPARENTHESIS LBRACKET estatuto RBRACKET
	'''
def p_if(p):
	'''
	if : IF LPARENTHESIS expresion RPARENTHESIS THEN LBRACKET estatuto RBRACKET
		| IF LPARENTHESIS expresion RPARENTHESIS THEN LBRACKET estatuto RBRACKET else  

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
def p_expresion(p):
 	'''
 	expresion : expresion1
 		| expresion1 OR expresion1
 	'''
def p_expresion1(p):
	'''
	expresion1 : expresion2
		| expresion2 AND expresion2
	'''
def p_expresion2(p):
	'''
	expresion2 : suma
		| suma expresioncomp suma
	'''
def p_expresioncomp(p):
	'''
    expresioncomp : suma GTHAN suma
             | suma LTHAN suma
             | suma GTHANEQ suma
             | suma LTHANEQ suma
             | suma DIFFERENT suma 	
	'''
def p_suma(p):
	'''
	suma : multiplicacion
		| multiplicacion PLUS multiplicacion
		| multiplicacion MINUS multiplicacion
	'''
def p_multiplicacion(p):
	'''
	multiplicacion : expresion3
		| expresion3 MULTIPLICATION expresion3
		| expresion3 DIVISION expresion3
	'''
def p_expresion3(p):
	'''
	expresion3 : CTEI
    	| CTEF
    	| CTEC
    	| CTESTRING
    	| LPARENTHESIS expresion3 RPARENTHESIS
    	| llamada
    	| leevars
	'''
def p_empty(p):
    '''
    empty : 
    '''

    
def p_error(p):
    print("Syntax error at '%s'" % p.value)


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
            print(tok)
        if (parser.parse(content, tracking = True) == 'SUCCESS'):
            print ("Correct Syntax")
        else: 
            print("Syntax error")
    except EOFError:
        print(EOFError)

main()