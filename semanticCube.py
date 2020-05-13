from collections import defaultdict

semanticCube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

#Operaciones
#Integer
semanticCube['int']['int']['+'] = 'int'
semanticCube['int']['int']['-'] = 'int'
semanticCube['int']['int']['*'] = 'int'
semanticCube['int']['int']['/'] = 'float'
#Float
semanticCube['float']['float']['+'] = 'float'
semanticCube['float']['float']['-'] = 'float'
semanticCube['float']['float']['*'] = 'float'
semanticCube['float']['float']['/'] = 'float'
#Char
semanticCube['char']['char']['+'] = 'Error'
semanticCube['char']['char']['-'] = 'Error'
semanticCube['char']['char']['*'] = 'Error'
semanticCube['char']['char']['/'] = 'Error'
#Mixtas con Equivalencias INT - FLOAT
semanticCube['int']['float']['+'] = semanticCube['float']['int']['+'] = 'float'
semanticCube['int']['float']['-'] = semanticCube['float']['int']['-'] = 'float'
semanticCube['int']['float']['*'] = semanticCube['float']['int']['*'] = 'float'
semanticCube['int']['float']['/'] = semanticCube['float']['int']['/'] = 'float'
#Mixtas con Equivalencias INT - CHAR - FLOAT
semanticCube['char']['int']['+'] = semanticCube['int']['char']['+'] = 'Error'
semanticCube['char']['float']['+'] = semanticCube['float']['char']['+'] = 'Error'
semanticCube['char']['int']['-'] = semanticCube['int']['char']['-'] = 'Error'
semanticCube['char']['float']['-'] = semanticCube['float']['char']['-'] = 'Error'
semanticCube['char']['int']['*'] = semanticCube['int']['char']['*'] = 'Error'
semanticCube['char']['float']['*'] = semanticCube['float']['char']['*'] = 'Error'
semanticCube['char']['int']['/'] = semanticCube['int']['char']['/'] = 'Error'
semanticCube['char']['float']['/'] = semanticCube['float']['char']['/'] = 'Error'

#Asignaciones
semanticCube['int']['int']['='] = 'int'
semanticCube['float']['float']['='] = 'float'
semanticCube['char']['char']['='] = 'char' 

#Comparaciones
#Integers
semanticCube['int']['int']['>'] = 'bool'
semanticCube['int']['int']['<'] = 'bool'
semanticCube['int']['int']['>='] = 'bool'
semanticCube['int']['int']['<='] = 'bool'
semanticCube['int']['int']['!='] = 'bool'
#Floats
semanticCube['float']['float']['>'] = 'bool'
semanticCube['float']['float']['<'] = 'bool'
semanticCube['float']['float']['>='] = 'bool'
semanticCube['float']['float']['<='] = 'bool'
semanticCube['float']['float']['!='] = 'bool'
#Chars
semanticCube['char']['char']['<'] = 'Error'
semanticCube['char']['char']['>'] = 'Error'
semanticCube['char']['char']['>='] = 'Error'
semanticCube['char']['char']['<='] = 'Error'
semanticCube['char']['char']['!='] = 'Error'
#Errores
semanticCube['char']['int']['='] = semanticCube['int']['char']['='] = 'Error'
semanticCube['char']['float']['='] = semanticCube['float']['char']['='] = 'Error'
semanticCube['char']['int']['>'] = semanticCube['int']['char']['>'] = 'Error'
semanticCube['char']['float']['>'] = semanticCube['float']['char']['>'] = 'Error'
semanticCube['char']['int']['<'] = semanticCube['int']['char']['<'] = 'Error'
semanticCube['char']['float']['<'] = semanticCube['float']['char']['<'] = 'Error'
semanticCube['char']['int']['>='] = semanticCube['int']['char']['>='] = 'Error'
semanticCube['char']['float']['>='] = semanticCube['int']['float']['>='] = 'Error'
semanticCube['char']['int']['<='] = semanticCube['int']['char']['<='] = 'Error'
semanticCube['char']['float']['<='] = semanticCube['float']['char']['<='] = 'Error'
semanticCube['char']['int']['!='] = semanticCube['int']['char']['!='] = 'Error'
semanticCube['char']['float']['!='] = semanticCube['float']['char']['!='] = 'Error'

#Operadores Logicos
semanticCube['int']['int']['||'] = 'bool'
semanticCube['int']['int']['&&'] = 'bool'
semanticCube['float']['float']['||'] = 'bool'
semanticCube['float']['float']['&&'] = 'bool'
semanticCube['char']['char']['||'] = 'bool'
semanticCube['char']['char']['&&'] = 'bool'
#Errores
semanticCube['char']['int']['||'] = semanticCube['int']['char']['||'] = 'Error'
semanticCube['char']['float']['||'] = semanticCube['char']['float']['||'] = 'Error'
semanticCube['char']['int']['&&'] = semanticCube['char']['int']['&&'] = 'Error'
semanticCube['char']['float']['&&'] = semanticCube['char']['float']['&&'] = 'Error'


#NO TENGO == AGREGAR A LEXER PARSER Y CUBO SEMANTICO
