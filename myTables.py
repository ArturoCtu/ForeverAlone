import sys
import json
#Segmentación de Memoria
typeName = ['int', 'float', 'char', 'string', 'bool']

#Limites 2000 Espacios a todo por simplicidad
#Globales 			[int,  float,  char,  string,  bool]
globalLowerLim = 	[1000,  3000,  5000,  7000,  9000]
globalUppperLim = 	[2999,  4999,  6999,  8999, 10999]
globalCounter =		[0,		0,		0,		0,		0]
#Globales Temporales
glTempLowerLim = 	[11000, 13000, 15000, 17000, 19000]
glTempUppperLim = 	[12999, 14999, 16999, 18999, 20999]
glTempCounter =		[0,		0,		0,		0,		0]
#Locales
LocalLowerLim = 	[21000, 23000, 25000, 27000, 29000]
LocalUppperLim = 	[22999, 24999, 26999, 28999, 30999]
LocalCounter =		[0,		0,		0,		0,		0]
#Locales Temporales
LocTempLowerLim =	[31000, 33000, 35000, 37000, 39000]
LocTempUppperLim = 	[32999, 34999, 36999, 38999, 10999]
LocTempCounter =	[0,		0,		0,		0,		0]
#Constantes
ConstantLowerLim = 	[41000, 43000, 45000, 47000, 49000]
ConstantUpperLim = 	[42999, 44999, 46999, 48999, 50999]
ConstantCounter =	[0,		0,		0,		0,		0]
#Pointers
PointerLowerLim = 	[51000, 53000, 55000, 57000, 59000]
PointerCounter =	[0,		0,		0,		0,		0]
#Para convertir operadores a numeros para hacerlos más fácil de manejar en ifs
operators = {
	'+' : 1,
	'-' : 2,
	'*' : 3,
	'/' : 4,
	'&&' : 5,
	'||' : 6,
	'>' : 7,
	'<' : 8,
	'>=' : 9,
	'<=' : 10,
	'!=' : 11,
	'==' : 12,
	'=' : 13,
	'print' : 14,
	'read' : 15,
	'Goto' : 16,
	'GotoF' : 17,
	'GotoV' : 18,
	#Para Funciones
	'ERA' : 19,
	'param' : 20,
	'Gosub' : 21,
	'return' : 22,
	'endproc' : 23,
	'ver' : 24,
	'+dir' : 25
}

#Definimos lo que tendran nuestras tablas de Variables y Funciones 
class varTable(object):
	def __init__(self):
		self.varlst = {}
		self.ctelst = {}

	def addVar(self, type, id, address):
		self.varlst[id] = {
			'type': type,
			'address' : address,
			'isArray' : False,
			'size' : 0
		}
		#print("Variable agregada " + type + " " + id + " " + str(address))

	def addCte(self, type, value, address):
		self.ctelst[value] = {
			'type': type,
			'address' : address
		}
		#print("Constante agregada " + type + " " + str(value) + " " + str(address))
	def toggleArray(self, id, size, funId):
		self.varlst[id]['isArray'] = True
		self.varlst[id]['size'] = size
		if(funId == 'global'):
			if(self.varlst[id]['type'] == 'int'):
				globalCounter[0] += size-1
			if(self.varlst[id]['type'] == 'float'):
				globalCounter[1] += size-1
			if(self.varlst[id]['type'] == 'char'):
				globalCounter[2] += size-1
		else:
			if(self.varlst[id]['type'] == 'int'):
				LocalCounter[0] += size-1
			if(self.varlst[id]['type'] == 'float'):
				LocalCounter[1] += size-1
			if(self.varlst[id]['type'] == 'char'):
				LocalCounter[2] += size-1
	#Funciones getters
	def getType(self, id):
		return self.varlst[id]['type']

	def getCteType(self, value):
		return self.ctelst[value]['type']

	def getAddress(self, id):
		return self.varlst[id]['address']

	def getCteAddress(self, value):
		return self.ctelst[value]['address']
	#Verifica que existan
	def searchVar(self, id):
		return id in self.varlst

	def searchCte(self, value):
		return value in self.ctelst

	def printVar(self):
		print(self.varlst.items())
	#Retorna todas las variables de una funcion
	def getAll(self):
		data = {}
		for key in list(self.varlst.keys()):
			data[key] = {
				'type': self.varlst[key]['type'],
				'address': self.varlst[key]['address'],
				'isArray': self.varlst[key]['isArray'],
				'size': self.varlst[key]['size']
			}
		return data
	#Retorna todas las Constantes
	def getCtes(self):
		data = {}
		for key in list(self.ctelst.keys()):
			data[key] = {
				'type': self.ctelst[key]['type'],
				'address': self.ctelst[key]['address'],
			}
		return data
class funTable(object):
	def __init__(self):
		self.funlst = {}
	#Definimos el constructor y que va a contener
	def addFun(self, type, id, nParams, typeParams, idParams, nVars, startQuad):
		if id in self.funlst.keys():
			print("Error: la funcion " + id + " ya existe")
		else: 
			self.funlst[id] = {
				'type' : type,
				'nParams' : nParams,
				'typeParams' : typeParams,
				'idParams' : idParams,
				'nVars' : nVars,
				'startQuad' : startQuad,
				'vars' : varTable()
			}
	def setArray(self, funId, id, size):
		self.funlst[funId]['vars'].toggleArray(id, size, funId)

	def getArrSize(self, funId, id):
		return self.funlst[funId]['vars'].varlst[id]['size']

	#Va por toda la informacion que vamos a neceistar en máquina virtual
	def compileEverything(self, quads):
		data = {}
		dataaux = {}
		for key in list(self.funlst.keys()):
			data[key] = {
				'type': self.funlst[key]['type'],
				'nParams': self.funlst[key]['nParams'],
				'typeParams': self.funlst[key]['typeParams'],
				'idParams': self.funlst[key]['idParams'],
				'nVars': self.funlst[key]['nVars'],
				'startQuad': self.funlst[key]['startQuad'],
				'vars': self.funlst[key]['vars'].getAll()
			}
		data['ctes'] = {
		'values': self.funlst['global']['vars'].getCtes()
		}
		i=0
		data['excecution'] = {
			'quads' : str(quads)	
			}
		return data

	def getAllCtes(self):
		data = {}
		data['ctes']  = self.funlst['global']['vars'].getCtes()
		return data
	#Cada que una funcion se cierre reseteamos la memoria
	def resetVarAdresses(self):
		global LocalCounter, LocTempCounter, ConstantCounter
		LocalCounter=[0,0,0,0,0]
		LocTempCounter=[0,0,0,0,0]
		PointerCounter=[0,0,0,0,0]
	#Registra un parametro como propio de una funcion
	def registerParam(self, funId, type, id):
		self.funlst[funId]['nParams'] +=1
		self.funlst[funId]['typeParams'].append(type)
		self.funlst[funId]['idParams'].append(id)
	#Funciones Getters
	def getParamNumber(self, funId):
		return self.funlst[funId]['nParams']

	def getParamType(self, funId, n):
		return self.funlst[funId]['typeParams'][n]

	def getParamId(self, funId, n):
		return self.funlst[funId]['idParams'][n]

	def getParamAddress(self, funId, id):
		return self.funlst[funId]['vars'].getVarAddress(id)

	def searchFun(self, id):
		return id in self.funlst
	#Agregamos variables a funciones
	def addVartoFun(self, funId, type, id):
		if(self.funlst[funId]['vars'].searchVar(id) or self.funlst['global']['vars'].searchVar(id)):
			print("Error: la variable " + id + " ya existe")
			sys.exit()
		elif(funId	== 'global'):
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[0]+globalCounter[0])
				globalCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[1]+globalCounter[1])
				globalCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[2]+globalCounter[2])
				globalCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[3]+globalCounter[3])
				globalCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[4]+globalCounter[4])
				globalCounter[4] += 1
		else:
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[0]+LocalCounter[0])
				LocalCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[1]+LocalCounter[1])
				LocalCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[2]+LocalCounter[2])
				LocalCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[3]+LocalCounter[3])
				LocalCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[4]+LocalCounter[4])
				LocalCounter[4] += 1

		#print("Variable agregada " + type + " " + str(id) + " to " + funId)
	#Agregamos Constantes al global
	def addCtetoFun(self, funId, type, value):
		if(self.funlst['global']['vars'].searchCte(value)):
			pass
			#print("La constante " + str(value) + " ya existe, se usara la direccion existente")
		else:
			if(type == 'int'):
				self.funlst['global']['vars'].addCte(type, value, ConstantLowerLim[0]+ConstantCounter[0])
				ConstantCounter[0] += 1
			if(type == 'float'):
				self.funlst['global']['vars'].addCte(type, value, ConstantLowerLim[1]+ConstantCounter[1])
				ConstantCounter[1] += 1
			if(type == 'char'):
				self.funlst['global']['vars'].addCte(type, value, ConstantLowerLim[2]+ConstantCounter[2])
				ConstantCounter[2] += 1
			if(type == 'string'):
				self.funlst['global']['vars'].addCte(type, value, ConstantLowerLim[3]+ConstantCounter[3])
				ConstantCounter[3] += 1
			if(type == 'bool'):
				self.funlst['global']['vars'].addCte(type, value, ConstantLowerLim[4]+ConstantCounter[4])
				ConstantCounter[4] += 1
	#Agregamos Variables temporales a una funcion	
	def addTempVar(self, funId, type, id):
		if(self.funlst[funId]['vars'].searchVar(id) or self.funlst['global']['vars'].searchVar(id)):
			print("Error: la variable " + id + " ya existe")
		if(id[0] == '*'):
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, PointerLowerLim[0]+PointerCounter[0])
				PointerCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, PointerLowerLim[1]+PointerCounter[1])
				PointerCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, PointerLowerLim[2]+PointerCounter[2])
				PointerCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, PointerLowerLim[3]+PointerCounter[3])
				PointerCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, PointerLowerLim[4]+PointerCounter[4])
				PointerCounter[4] += 1
		elif(funId	== 'global'):
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, glTempLowerLim[0]+glTempCounter[0])
				glTempCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, glTempLowerLim[1]+glTempCounter[1])
				glTempCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, glTempLowerLim[2]+glTempCounter[2])
				glTempCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, glTempLowerLim[3]+glTempCounter[3])
				glTempCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, glTempLowerLim[4]+glTempCounter[4])
				glTempCounter[4] += 1
		else:
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, LocTempLowerLim[0]+LocTempCounter[0])
				LocTempCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, LocTempLowerLim[1]+LocTempCounter[1])
				LocTempCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, LocTempLowerLim[2]+LocTempCounter[2])
				LocTempCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, LocTempLowerLim[3]+LocTempCounter[3])
				LocTempCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, LocTempLowerLim[4]+LocTempCounter[4])
				LocTempCounter[4] += 1

	#Mas getters para retornar informacion
	def getVarType(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getType(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getType(id)
		elif(self.funlst['global']['vars'].searchCte(id)):
			return self.funlst['global']['vars'].getCteType(id)
		else:
			print("Var "+ str(id) + " Not Found")
			sys.exit()


	def getVarAddress(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getAddress(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getAddress(id)
		elif(self.funlst['global']['vars'].searchCte(id)):
			return self.funlst['global']['vars'].getCteAddress(id)
		else:
			print("Var "+ str(id) + " Not Found ss")
			sys.exit()

	#busca una variable en una funcion
	def searchVarinFun(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return True
		elif(self.funlst['global']['vars'].searchVar(id)):
			return True
		else:
			print("Var "+ id + " Not Found")
			return False 

	def printFunVars(self, funId):
		if id in self.funlst:
				self.funlst[funId]['vars'].printVar()
	#Regresa donde empeiza una funcion en quads
	def getStartQuad(self, funId):
		return self.funlst[funId]['startQuad']

