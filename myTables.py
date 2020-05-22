#Segmentación de Memoria

typeName = ['int', 'float', 'char', 'string', 'bool']
typeSize = [0,	0,	0,	0,	0]
#Limites 2000 Espacios a todo por simplicidad
#Globales 			[int,  float,  char,  string,  bool]
globalLowerLim = 	[1000,  3000,  5000,  7000,  9000]
globalUppperLim = 	[2999,  4999,  6999,  8999, 10999]
#Globales Temporales
glTempLowerLim = 	[11000, 13000, 15000, 17000, 19000]
glTempUppperLim = 	[12999, 14999, 16999, 18999, 20999]
#Locales
LocalLowerLim = 	[21000, 23000, 25000, 27000, 29000]
LocalUppperLim = 	[22999, 24999, 26999, 28999, 30999]
#Locales Temporales
LocTempLowerLim =	[31000, 33000, 35000, 37000, 39000]
LocTempUppperLim = 	[32999, 34999, 36999, 38999, 10999]
#Constantes
ConstantLowerLim = 	[41000, 43000, 45000, 47000, 49000]
ConstantUpperLim = 	[42999, 44999, 46999, 48999, 50999]

virtualMemory =[]

#Definimos lo que tendran nuestras tablas de Variables y Funciones 
class varTable(object):
	def __init__(self):
		self.varlst = {}

	def addVar(self, type, id, address):
		self.varlst[id] = {
			'type': type,
			'address' : address
		}
		print("Variable agregada " + type + " " + id + " " + str(address))

	def getType(self, id):
		return self.varlst[id]['type']

	def getAddress(self, id):
		return self.varlst[id]['address']

	def searchVar(self, id):
		return id in self.varlst

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
			#print("Funcion agregada", type, id)

	def searchFun(self, id):
		return id in self.funlst

	def addVartoFun(self, funId, type, id):
		if(self.funlst[funId]['vars'].searchVar(id) or self.funlst['global']['vars'].searchVar(id)):
			print("Error: la variable " + id + " ya existe")
		elif(funId	== 'global'):
				if(type == 'int'):
					self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[0]+typeSize[0])
					typeSize[0] += 1
				if(type == 'float'):
					self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[1]+typeSize[1])
					typeSize[1] += 1
				if(type == 'char'):
					self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[2]+typeSize[2])
					typeSize[2] += 1
				if(type == 'string'):
					self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[3]+typeSize[3])
					typeSize[3] += 1
				if(type == 'bool'):
					self.funlst[funId]['vars'].addVar(type, id, globalLowerLim[4]+typeSize[4])
					typeSize[4] += 1
		else:
			if(type == 'int'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[0]+typeSize[0])
				typeSize[0] += 1
			if(type == 'float'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[1]+typeSize[1])
				typeSize[1] += 1
			if(type == 'char'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[2]+typeSize[2])
				typeSize[2] += 1
			if(type == 'string'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[3]+typeSize[3])
				typeSize[3] += 1
			if(type == 'bool'):
				self.funlst[funId]['vars'].addVar(type, id, LocalLowerLim[4]+typeSize[4])
				typeSize[4] += 1

		#print("Variable agregada " + type + " " + id +  + " to " + funId)

	def getVarType(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getType(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getType(id)
		else:
			print("Var "+ id + " Not Found")


	def getVarAddress(self, funId, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			return self.funlst[funId]['vars'].getAddress(id)
		elif(self.funlst['global']['vars'].searchVar(id)):
			return self.funlst['global']['vars'].getAddress(id)
		else:
			print("Var "+ id + " Not Found")


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
