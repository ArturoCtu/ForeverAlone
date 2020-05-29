import sys
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
	'endproc' : 23
}

#Definimos lo que tendran nuestras tablas de Variables y Funciones 
class varTable(object):
	def __init__(self):
		self.varlst = {}
		self.ctelst = {}

	def addVar(self, type, id, address):
		self.varlst[id] = {
			'type': type,
			'address' : address
		}
		print("Variable agregada " + type + " " + id + " " + str(address))

	def addCte(self, type, value, address):
		self.ctelst[value] = {
			'type': type,
			'address' : address
		}
		print("Constante agregada " + type + " " + str(value) + " " + str(address))

	def getType(self, id):
		return self.varlst[id]['type']

	def getCteType(self, value):
		return self.ctelst[value]['type']

	def getAddress(self, id):
		return self.varlst[id]['address']

	def getCteAddress(self, value):
		return self.ctelst[value]['address']

	def searchVar(self, id):
		return id in self.varlst

	def searchCte(self, value):
		return value in self.ctelst

	def printVar(self):
		print(self.varlst.items())

class funTable(object):
	def __init__(self):
		self.funlst = {}

	def addFun(self, type, id, nParams, typeParams, idParams, nVars):
		if id in self.funlst.keys():
			print("Error: la funcion " + id + " ya existe")
		else: 
			self.funlst[id] = {
				'type' : type,
				'nParams' : nParams,
				'typeParams' : typeParams,
				'idParams' : idParams,
				'nVars' : nVars,
				'vars' : varTable()
			}


			

	def searchFun(self, id):
		return id in self.funlst

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
	
	def addCtetoFun(self, funId, type, value):
		if(self.funlst[funId]['vars'].searchCte(value)):
			print("La constante " + str(value) + " ya existe, se usara la direccion existente")
		else:
			if(type == 'int'):
				self.funlst[funId]['vars'].addCte(type, value, ConstantLowerLim[0]+ConstantCounter[0])
				ConstantCounter[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addCte(type, value, ConstantLowerLim[1]+ConstantCounter[1])
				ConstantCounter[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addCte(type, value, ConstantLowerLim[2]+ConstantCounter[2])
				ConstantCounter[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addCte(type, value, ConstantLowerLim[3]+ConstantCounter[3])
				ConstantCounter[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addCte(type, value, ConstantLowerLim[4]+ConstantCounter[4])
				ConstantCounter[4] += 1
			print("Constante agregada " + type + " " + str(value) + " to " + funId)
	
	def addTempVar(self, funId, type, id):
		if(self.funlst[funId]['vars'].searchVar(id) or self.funlst['global']['vars'].searchVar(id)):
			print("Error: la variable " + id + " ya existe")
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


	def getVarType(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getType(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getType(id)
		elif(self.funlst[funId]['vars'].searchCte(id)):
			return self.funlst[funId]['vars'].getCteType(id)
		else:
			print("Var "+ str(id) + " Not Found")


	def getVarAddress(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getAddress(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getAddress(id)
		elif(self.funlst[funId]['vars'].searchCte(id)):
			return self.funlst[funId]['vars'].getCteAddress(id)
		else:
			print("Var "+ str(id) + " Not Found ss")



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

