#Definimos lo que tendran nuestras tablas de Variables y Funciones 
class varTable(object):
	def __init__(self):
		self.varlst = {}

	def addVar(self, type, id):
		self.varlst[id] = {
			'type': type
		}

	def searchVar(self, id):
		return id in self.varlst

	def printVar(self):
		print(self.varlst.items())

class funTable(object):
	def __init__(self):
		self.funlst = {}

	def addFun(self, type, id, nParams, typeParams, idParams, nVars):
		if id in self.funlst.keys():
			print("Error: la funcion" + id + "ya existe")
		else: 
			self.funlst[id] = {
				'type' : type,
				'nParams' : nParams,
				'typeParams' : typeParams,
				'idParams' : idParams,
				'nVars' : nVars,
				'vars' : varTable()
			}
			print("Funcion agregada", type, id)

	def searchFun(self, id):
		return id in self.funlst

	def addVartoFun(self, funId, type, id):
		if(self.funlst[funId]['vars'].searchVar(id)):
			print("Error: la variable" + id + "ya existe")
		else:
			self.funlst[funId]['vars'].addVar(type, id)
			print("Variable agregada", id)

	def printFunVars(self, funId):
		if id in self.funlst:
				self.funlst[funId]['vars'].printVar()

'''
z = funTable()

z.addFun('void', 'ImprimeParametros', 3,
['int', 'float', 'char'],['uno','dos', 'tres'], 0)


z.addVartoFun('ImprimeParametros','int', 'i')
z.addVartoFun('ImprimeParametros', 'float', 'o')
z.addVartoFun('ImprimeParametros', 'char', 'p')

print(z.searchFun('ImprimeParametros'))
print(z.searchFun('hgrughurhgu'))

z.printFunVars('hola')
'''