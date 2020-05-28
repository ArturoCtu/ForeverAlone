from collections import defaultdict

semanticCube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))
#Asignacion
semanticCube['int']['int']['='] = 'int'
semanticCube['float']['float']['='] = 'float'
semanticCube['char']['char']['='] = 'char'

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
semanticCube['int']['char']['+'] = semanticCube['char']['int']['+'] = 'Error'
semanticCube['int']['char']['-'] = semanticCube['char']['int']['-'] = 'Error'
semanticCube['int']['char']['*'] = semanticCube['char']['int']['*'] = 'Error'
semanticCube['int']['char']['/'] = semanticCube['char']['int']['/'] = 'Error'
semanticCube['float']['char']['+'] = semanticCube['char']['float']['+'] = 'Error'
semanticCube['float']['char']['-'] = semanticCube['char']['float']['-'] = 'Error'
semanticCube['float']['char']['*'] = semanticCube['char']['float']['*'] = 'Error'
semanticCube['float']['char']['/'] = semanticCube['char']['float']['/'] = 'Error'

#Asignaciones
semanticCube['int']['int']['='] = 'int'
semanticCube['float']['float']['='] = 'float'
semanticCube['char']['char']['='] = 'char' 
#Errores
semanticCube['char']['int']['='] = semanticCube['int']['char']['='] = 'Error'
semanticCube['char']['float']['='] = semanticCube['float']['char']['='] = 'Error'

#Comparaciones
#Integers
semanticCube['int']['int']['>'] = 'bool'
semanticCube['int']['int']['<'] = 'bool'
semanticCube['int']['int']['>='] = 'bool'
semanticCube['int']['int']['<='] = 'bool'
semanticCube['int']['int']['!='] = 'bool'
semanticCube['int']['int']['=='] = 'bool'
#Floats
semanticCube['float']['float']['>'] = 'bool'
semanticCube['float']['float']['<'] = 'bool'
semanticCube['float']['float']['>='] = 'bool'
semanticCube['float']['float']['<='] = 'bool'
semanticCube['float']['float']['!='] = 'bool'
semanticCube['float']['float']['=='] = 'bool'
#Mixta
semanticCube['int']['float']['>'] = semanticCube['float']['int']['>'] = 'bool' 
semanticCube['int']['float']['<'] = semanticCube['float']['int']['<'] = 'bool' 
semanticCube['int']['float']['>='] = semanticCube['float']['int']['>='] = 'bool' 
semanticCube['int']['float']['<='] = semanticCube['float']['int']['<='] = 'bool' 
semanticCube['int']['float']['!='] = semanticCube['float']['int']['!='] = 'bool'
semanticCube['int']['float']['=='] = semanticCube['float']['int']['=='] = 'bool' 
#Chars
semanticCube['char']['char']['<'] = 'Error'
semanticCube['char']['char']['>'] = 'Error'
semanticCube['char']['char']['>='] = 'Error'
semanticCube['char']['char']['<='] = 'Error'
semanticCube['char']['char']['!='] = 'Error'
semanticCube['char']['char']['=='] = 'bool'
#Errores con equivalencia
semanticCube['int']['char']['>'] = semanticCube['char']['int']['>'] = 'Error'
semanticCube['float']['char']['>'] = semanticCube['char']['float']['>'] = 'Error'
semanticCube['int']['char']['<'] = semanticCube['char']['int']['<'] = 'Error'
semanticCube['float']['char']['<'] = semanticCube['char']['float']['<'] = 'Error'
semanticCube['int']['char']['>='] = semanticCube['char']['int']['>='] = 'Error'
semanticCube['float']['char']['>='] = semanticCube['char']['float']['>='] = 'Error'
semanticCube['int']['char']['<='] = semanticCube['char']['int']['<='] = 'Error'
semanticCube['float']['char']['<='] = semanticCube['char']['float']['<='] = 'Error'
semanticCube['int']['char']['!='] = semanticCube['char']['int']['!='] = 'Error'
semanticCube['float']['char']['!='] = semanticCube['char']['float']['!='] = 'Error'
semanticCube['int']['char']['=='] = semanticCube['char']['int']['=='] = 'Error'
semanticCube['float']['char']['=='] = semanticCube['char']['float']['=='] = 'Error'

#Operadores Logicos
semanticCube['int']['int']['||'] = 'bool'
semanticCube['int']['int']['&&'] = 'bool'
semanticCube['float']['float']['||'] = 'bool'
semanticCube['float']['float']['&&'] = 'bool'
semanticCube['char']['char']['||'] = 'bool'
semanticCube['char']['char']['&&'] = 'bool'
semanticCube['bool']['bool']['&&'] = 'bool'
semanticCube['bool']['bool']['||'] = 'bool'
#Errores
semanticCube['int']['char']['||'] = semanticCube['char']['int']['||'] = 'Error'
semanticCube['char']['float']['||'] = semanticCube['char']['float']['||'] = 'Error'
semanticCube['char']['int']['&&'] = semanticCube['char']['int']['&&'] = 'Error'
semanticCube['char']['float']['&&'] = semanticCube['char']['float']['&&'] = 'Error'
#Errores Bool
semanticCube['bool']['int']['&&'] = semanticCube['int']['bool']['&&'] = 'Error'
semanticCube['bool']['int']['||'] = semanticCube['int']['bool']['||'] = 'Error'
semanticCube['bool']['float']['&&'] = semanticCube['float']['bool']['&&'] = 'Error'
semanticCube['bool']['float']['||'] = semanticCube['float']['bool']['||'] = 'Error'
semanticCube['bool']['char']['&&'] = semanticCube['char']['bool']['&&'] = 'Error'
semanticCube['bool']['char']['||'] = semanticCube['char']['bool']['||'] = 'Error'
semanticCube['bool']['int']['>'] = semanticCube['int']['bool']['>'] = 'Error'
semanticCube['bool']['int']['<'] = semanticCube['int']['bool']['<'] = 'Error'
semanticCube['bool']['int']['>='] = semanticCube['int']['bool']['>='] = 'Error'
semanticCube['bool']['int']['<='] = semanticCube['int']['bool']['<='] = 'Error'
semanticCube['bool']['int']['=='] = semanticCube['int']['bool']['=='] = 'Error'
semanticCube['bool']['int']['!='] = semanticCube['int']['bool']['!='] = 'Error'
semanticCube['bool']['float']['>'] = semanticCube['float']['bool']['>'] = 'Error'
semanticCube['bool']['float']['<'] = semanticCube['float']['bool']['<'] = 'Error'
semanticCube['bool']['float']['>='] = semanticCube['float']['bool']['>='] = 'Error'
semanticCube['bool']['float']['<='] = semanticCube['float']['bool']['<='] = 'Error'
semanticCube['bool']['float']['=='] = semanticCube['float']['bool']['=='] = 'Error'
semanticCube['bool']['float']['!='] = semanticCube['float']['bool']['!='] = 'Error'
semanticCube['bool']['char']['>'] = semanticCube['char']['bool']['>'] = 'Error'
semanticCube['bool']['char']['<'] = semanticCube['char']['bool']['<'] = 'Error'
semanticCube['bool']['char']['>='] = semanticCube['char']['bool']['>='] = 'Error'
semanticCube['bool']['char']['<='] = semanticCube['char']['bool']['<='] = 'Error'
semanticCube['bool']['char']['=='] = semanticCube['char']['bool']['=='] = 'Error'
semanticCube['bool']['char']['!='] = semanticCube['char']['bool']['!='] = 'Error'



def getType(left,right, operator):
	return semanticCube[left][right][operator]
