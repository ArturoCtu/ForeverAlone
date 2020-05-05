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

    #Matrices () 
    'TRANSPOSE', #FALTA
    'INVERSE', #FALTA
    'DETERMINANT', #FALTA

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
    'to': 'to', #FALTA

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

#Matrices
t_TRANSPOSE = r'\¡'
t_INVERSE = r'\?'
t_DETERMINANT = r'\$'

#Assignment
t_EQUALS = r'\='

#Espacios en Blanco
t_ignore = r' '

#Saltos de Linea
def t_newline(t):
    r'\n+'

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

def p_programa1(p):
    '''
    programa1 : vars bloque programa2
    programa1 : vars bloque
    | programa2
    '''

def p_programa2(p):
    '''
    programa2 :  principal
    ''' 

def p_principal(p):
    '''
    principal : MAIN LPARENTHESIS parameters RPARENTHESIS LBRACKET vars estatuto RBRACKET END
    '''   
    
def p_tipo(p):
    '''
    tipo : INT 
         | FLOAT
         | CHAR
         | STRING
    '''    

def p_vars(p):
    '''
    vars : var 
         | empty
    '''

def p_var(p):
    '''
    var : VAR var2 var2
    ''' 

def p_var1(p):
    '''
        var1 : ID
        | ID COMMA var1
        | ID arr 
        | ID arr COMMA var1
        | ID mat COMMA var1
        | ID mat
        | empty
    ''' 
def p_var2(p):
    '''
        var2 : tipo var1 SEMICOLON
            | tipo arr SEMICOLON
            | tipo mat SEMICOLON
            | empty
    ''' 

    
def p_arr(p):
    '''
    arr : LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET 
    
    '''  

def p_mat(p):
    '''
    mat : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET LBRACKET exp RBRACKET
        | LBRACKET exp RBRACKET LBRACKET CTEI RBRACKET
        | LBRACKET CTEI RBRACKET LBRACKET exp RBRACKET
    ''' 
    
def p_bloque(p):
    '''
    bloque : function bloque
            | empty
    
    '''     

def p_function(p):
    '''
    function : FUNCTION VOID function1 
             | FUNCTION tipo function2 
    '''  

def p_function1(p):
    '''
    function1 : ID LPARENTHESIS parameters RPARENTHESIS SEMICOLON LBRACKET vars estatuto RBRACKET 
    '''  

def p_function2(p):
    '''
    function2 : ID LPARENTHESIS parameters RPARENTHESIS SEMICOLON LBRACKET vars estatuto RETURN exp SEMICOLON RBRACKET   
    '''  

def p_estatuto(p):
    '''
    estatuto : estatuto1 estatuto 
              | empty
    ''' 

def p_estatuto1(p):
    '''
    estatuto1 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    ''' 

def p_asignacion(p):
    '''
    asignacion : ID EQUALS exp
               | ID arr EQUALS exp
               | ID mat EQUALS exp
    ''' 
    

def p_param(p):
    '''
    parameters : tipo param1  
          | empty
    
    ''' 

def p_param1(p):
    '''
    param1 : ID
           | ID COMMA param1
           | empty 
    ''' 
    

def p_llamada(p): 
    '''
    llamada : ID LPARENTHESIS exp RPARENTHESIS
    ''' 

def p_if(p):
    '''
    if : IF LPARENTHESIS exp RPARENTHESIS LBRACKET estatuto RBRACKET 
        | IF LPARENTHESIS exp RPARENTHESIS LBRACKET estatuto RBRACKET else
    ''' 

def p_else(p):
    '''
    else : ELSE LBRACKET estatuto RBRACKET 
        | empty
    ''' 

def p_for(p):
    '''
    for : FOR LPARENTHESIS for1 RPARENTHESIS LBRACKET estatuto RBRACKET 
    '''

def p_for1(p):
    '''
    for1 : FROM asignacion TO exp
    '''

def p_while(p):
    '''
    while : WHILE LPARENTHESIS exp RPARENTHESIS LBRACKET estatuto RBRACKET 
    ''' 

def p_escritura(p):
     '''
    escritura : PRINT LPARENTHESIS escritura1 RPARENTHESIS
    ''' 

def p_escritura1(p):
     '''
    escritura1 : escritura2 COMMA escritura2
               | escritura2
    ''' 

def p_escritura2(p):
     '''
    escritura2 : CTESTRING  
               | CTEI
               | CTEF 
               | exp
    ''' 

def p_lectura(p):
    '''
    lectura : READ LPARENTHESIS var1 RPARENTHESIS
    ''' 

def p_exp(p):
    '''
    exp : nexp  
        | nexp OR nexp
    ''' 

def p_nexp(p):
    '''
    nexp : compexp
         | compexp AND compexp
    ''' 

def p_compexp(p):
    '''
    compexp : sumexp 
            | compexp1 sumexp
    ''' 

def p_compexp1(p):
    '''
    compexp1 : sumexp GT sumexp
             | sumexp LT sumexp
             | sumexp GTE sumexp
             | sumexp LTE sumexp
             | sumexp NE sumexp 
    ''' 

def p_sumexp(p):
    '''
    sumexp : mulexp  
           | mulexp PLUS mulexp
           | mulexp MINUS mulexp
    ''' 

def p_mulexp(p):
    '''
    mulexp : pexp  
           | pexp MUL pexp
           | pexp DIV pexp
    '''

def p_pexp(p):
    '''
    pexp : var1  
         | CTEI
         | CTEF
         | CTEC
         | llamada
         | LPARENTHESIS exp RPARENTHESIS
    '''


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    #print("Syntax error at '%s'" % p.value)
    print("Syntax Error in input!", p)
    
parser = yacc.yacc()

def main():
    try:
        #nombreArchivo = 'test1.txt'
        nombreArchivo = 'test1'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print ("Correct Syntax")
        else: 
            print("Syntax error")
    except EOFError:
        print("ERROREOF")

main()