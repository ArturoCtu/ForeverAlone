import json
import sys


class memory(object):
	def __init__(self):
		self.instancelst = {}
		self.int = {}
		self.float = {}
		self.char = {}
		self.bool = {}

	def addInstance(self, id):
		if id in self.instancelst.keys():
			print("Error: la instacia " + id + " ya existe")
		else: 
			self.instancelst[id] = {
				'int' : self.int,
				'float' : self.float,
				'char' : self.char,
				'bool' : self.bool
			}

	def addVar(self, address, type, value, instance):
		if(type == 'int'):
			self.instancelst[instance]['int'][address] = value
		elif(type == 'float'):
			self.instancelst[instance]['float'][address] = value
		elif(type == 'char'):
			self.instancelst[instance]['char'][address] = value
		elif(type == 'string'):
			self.instancelst[instance]['string'][address] = value
		elif(type == 'bool'):
			self.instancelst[instance]['bool'][address] = value

	def returnValue(self, address, type, instance):
		if(type == 'int'):
			return int(self.instancelst[instance]['int'][address])
		elif(type == 'float'):
			return float(self.instancelst[instance]['float'][address])
		elif(type == 'char'):
			return self.instancelst[instance]['char'][address]
		elif(type == 'string'):
			return self.instancelst[instance]['string'][address]
		elif(type == 'bool'):
			return self.instancelst[instance]['bool'][address]


	#If para saber que tipo de variable es y donde meterla
	def indexVar(self, address, value, funId):
		#Global
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				self.addVar(address, 'int', value, 'global')
			elif(address >= 3000 and address <= 4999):
				self.addVar(address, 'float', value, 'global')
			elif(address >= 5000 and address <= 6999):
				self.addVar(address, 'char', value, 'global')
			elif(address >= 7000 and address <= 8999):
				pass#self.gstring[address] = value
			elif(address >= 9000 and address <= 10999):
				self.addVar(address, 'bool', value, 'global')
		#Temporales Globales
		elif(address >= 11000 and address <= 20999):
			if(address >= 11000 and address <= 12999):
				self.addVar(address, 'int', value, 'global')
			elif(address >= 13000 and address <= 14999):
				self.addVar(address, 'float', value, 'global')
			elif(address >= 15000 and address <= 16999):
				self.addVar(address, 'char', value, 'global')
			elif(address >= 17000 and address <= 18999):
				pass#self.tstring[address] = value
			elif(address >= 19000 and address <= 20999):
				self.addVar(address, 'bool', value, 'global')
		#Locales
		elif(address >= 21000 and address <= 30999):
			if(address >= 21000 and address <= 22999):
				self.addVar(address, 'int', value, funId)
			elif(address >= 23000 and address <= 24999):
				self.addVar(address, 'float', value, funId)
			elif(address >= 25000 and address <= 26999):
				self.addVar(address, 'char', value, funId)
			elif(address >= 27000 and address <= 28999):
				pass#self.lstring[address] = value
			elif(address >= 29000 and address <= 30999):
				self.addVar(address, 'bool', value, funId)
		#Temporales Locales
		elif(address >= 31000 and address <= 40999):
			if(address >= 31000 and address <= 32999):
				self.addVar(address, 'int', value, funId)
			elif(address >= 33000 and address <= 34999):
				self.addVar(address, 'float', value, funId)
			elif(address >= 35000 and address <= 36999):
				self.addVar(address, 'char', value, funId)
			elif(address >= 37000 and address <= 38999):
				pass#self.tstring[address] = value
			elif(address >= 39000 and address <= 40999):
				self.addVar(address, 'bool', value, funId)
		#Constantes
		elif(address >= 41000 and address <= 50999):
			if(address >= 41000 and address <= 42999):
				self.addVar(address, 'int', value, 'const')
			elif(address >= 43000 and address <= 44999):
				self.addVar(address, 'float', value, 'const')
			elif(address >= 45000 and address <= 46999):
				self.addVar(address, 'char', value, 'const')
			elif(address >= 47000 and address <= 48999):
				self.addVar(address, 'string', value, 'const')
			elif(address >= 49000 and address <= 50999):
				self.addVar(address, 'bool', value, 'const')
		#Pointers
		elif(address >= 51000 and address <= 60999):
			if(address >= 51000 and address <= 52999):
				self.addVar(address, 'int', value, 'pointers')

	def getValue(self, address, funId):
		#Global
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				return self.returnValue(address, 'int', 'global')
			elif(address >= 3000 and address <= 4999):
				return self.returnValue(address, 'float', value, 'global')
			elif(address >= 5000 and address <= 6999):
				return self.returnValue(address, 'char', 'global')
			elif(address >= 7000 and address <= 8999):
				pass#self.gstring[address] = value
			elif(address >= 9000 and address <= 10999):
				return self.returnValue(address, 'bool', 'global')
		#Temporales Globales
		elif(address >= 11000 and address <= 20999):
			if(address >= 11000 and address <= 12999):
				return self.returnValue(address, 'int', 'global')
			elif(address >= 13000 and address <= 14999):
				return self.returnValue(address, 'float', 'global')
			elif(address >= 15000 and address <= 16999):
				return self.returnValue(address, 'char', 'global')
			elif(address >= 17000 and address <= 18999):
				pass#self.tstring[address] = value
			elif(address >= 19000 and address <= 20999):
				return self.returnValue(address, 'bool', 'global')
		#Locales
		elif(address >= 21000 and address <= 30999):
			if(address >= 21000 and address <= 22999):
				return self.returnValue(address, 'int', funId)
			elif(address >= 23000 and address <= 24999):
				return self.returnValue(address, 'float', funId)
			elif(address >= 25000 and address <= 26999):
				return self.returnValue(address, 'char', funId)
			elif(address >= 27000 and address <= 28999):
				pass#self.lstring[address] = value
			elif(address >= 29000 and address <= 30999):
				return self.returnValue(address, 'bool', funId)
		#Temporales Locales
		elif(address >= 31000 and address <= 40999):
			if(address >= 31000 and address <= 32999):
				return self.returnValue(address, 'int', funId)
			elif(address >= 33000 and address <= 34999):
				return self.returnValue(address, 'float', funId)
			elif(address >= 35000 and address <= 36999):
				return self.returnValue(address, 'char', funId)
			elif(address >= 37000 and address <= 38999):
				pass#self.tstring[address] = value
			elif(address >= 39000 and address <= 40999):
				return self.returnValue(address, 'bool', funId)
		#Constantes
		elif(address >= 41000 and address <= 50999):
			if(address >= 41000 and address <= 42999):
				return self.returnValue(address, 'int', 'const')
			elif(address >= 43000 and address <= 44999):
				return self.returnValue(address, 'float', 'const')
			elif(address >= 45000 and address <= 46999):
				return self.returnValue(address, 'char', 'const')
			elif(address >= 47000 and address <= 48999):
				return self.returnValue(address, 'string', 'const')
			elif(address >= 49000 and address <= 50999):
				return self.returnValue(address, 'bool', 'const')
		#Pointers
		elif(address >= 51000 and address <= 60999):
			if(address >= 51000 and address <= 52999):
				return self.returnValue(address, 'int', 'pointers')



memory = memory()
#Reconstruye la memoria global que tenemos en un archivo
def rebuildGlobal():
	with open('compiled.out') as infile:
		data = json.load(infile)
		ctes = data['ctes']['values']
		vars = data['global']['vars']
		for cte in ctes:
			memory.indexVar(ctes[cte]['address'],cte,'const')
		#Si no tiene valor le asigna su mismo address como un lenguaje normal
		for var in vars:
			memory.indexVar(vars[var]['address'],vars[var]['address'],'global')
#Reconstruye la memoria de una funcion que tenemos en un archivo
def rebuildFunctionMemory(funId):
	with open('compiled.out') as infile:
		data = json.load(infile)
		vars = data[funId]['vars']
		#Si no tiene valor le asigna su mismo address como un lenguaje normal
		for var in vars:
			memory.indexVar(vars[var]['address'],vars[var]['address'], 'main')			
def era(funId):
	with open('compiled.out') as infile:
		data = json.load(infile)
		nParams = data[funId]['nParams']


#Ejecuta el codigo de cuadruplos
def excecute(quads):
	currentContext = 'main'

	memory.addInstance('global')
	memory.addInstance('const')
	memory.addInstance('main')
	memory.addInstance('pointers')
	rebuildGlobal()

	rebuildFunctionMemory('main')
	#print(*quads, sep = "\n")
	#Vamos al main
	i = quads[0][3] 
	#i -> quad pointer
	while (i < len(quads)):
		operator = quads[i][0]
		pos1 = quads[i][1]
		pos2 = quads[i][2]
		pos3 = quads[i][3]

		if pos3 != None:
			if pos3 >= 51000:
				pos3 = memory.getValue(pos3, currentContext)
		if pos2 != None:
			if pos2 >= 51000:
				pos2 = memory.getValue(pos2, currentContext)
		if pos1 != None:
			if pos1 >= 51000:
				pos1 = memory.getValue(pos1, currentContext)


		#Operaciones basicas
		if operator == 1:
			res = memory.getValue(pos1, currentContext) + memory.getValue(pos2, currentContext)
			memory.indexVar(pos3, res, currentContext)
		elif operator == 2:
			res = memory.getValue(pos1, currentContext) - memory.getValue(pos2, currentContext)
			memory.indexVar(pos3, res, currentContext)
		elif operator == 3:
			res = memory.getValue(pos1, currentContext) * memory.getValue(pos2, currentContext)
			memory.indexVar(pos3, res, currentContext)
		elif operator == 4:
			res = memory.getValue(pos1, currentContext) / memory.getValue(pos2, currentContext)
			memory.indexVar(pos3, res, currentContext)
		#Operaciones Logicas
		elif operator == 5:
			if (memory.getValue(pos1, currentContext) and memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 6:
			if (memory.getValue(pos1, currentContext) or memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 7:
			if (memory.getValue(pos1, currentContext) > memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 8:
			if (memory.getValue(pos1, currentContext) < memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 9:
			if (memory.getValue(pos1, currentContext) >= memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 10:
			if (memory.getValue(pos1, currentContext) <= memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 11:
			if (memory.getValue(pos1, currentContext) != memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		elif operator == 12:
			if (memory.getValue(pos1, currentContext) == memory.getValue(pos2, currentContext)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res, currentContext)
		#Asignacion
		elif operator == 13:
			res = memory.getValue(pos3, currentContext)
			#print(pos1,'=',pos3)
			memory.indexVar(pos1, res, currentContext)
		#Print
		elif operator == 14:
			#print(pos3)
			res = memory.getValue(pos3, currentContext)
			print(res)
		#Read
		elif operator == 15:
			res = input()
			memory.indexVar(pos3, res, currentContext)
		#Gotos
		elif operator == 16:
			i = pos3-1
		elif operator == 17:
			if(not memory.getValue(pos1, currentContext)):
				i = pos3-1
		elif operator == 18:
			pass
		#Funciones
		elif operator == 19:
			era(pos3)
		elif operator == 20:
			pass
		elif operator == 21:
			pass
		elif operator == 22:
			pass
		elif operator == 23:
			pass
		#Ver
		elif operator == 24:
			if memory.getValue(quads[i][1], currentContext) > quads[i][3]:
				print("Arreglo Fuera de rango")
				sys.exit()
		elif operator == 25:
			res = quads[i][1] + memory.getValue(quads[i][2], currentContext)
			memory.indexVar(quads[i][3], res, currentContext)
		i+=1
