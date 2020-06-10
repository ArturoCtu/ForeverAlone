import json
import sys
#Memoria Virtual segmentada
class memory(object):
	def __init__(self):
		#Global
		self.gint= {}
		self.gfloat = {}
		self.gchar = {}
		self.gbool = {}
		#Local
		self.lint= {}
		self.lfloat = {}
		self.lchar = {}
		self.lbool = {}
		#Temp
		self.tint= {}
		self.tfloat = {}
		self.tchar = {}
		self.tbool = {}
		#CTES
		self.cint= {}
		self.cfloat = {} 
		self.cchar = {}
		self.cbool = {}
		self.cstring = {}
		#Pointers
		self.pointers = {}

#Limites 2000 Espacios a todo por simplicidad
#If para saber que tipo de variable es y donde meterla
	def indexVar(self, address, value):
		#Global
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				self.gint[address] = value
			if(address >= 3000 and address <= 4999):
				self.gfloat[address] = value
			if(address >= 5000 and address <= 6999):
				self.gchar[address] = value
			if(address >= 7000 and address <= 8999):
				pass#self.gstring[address] = value
			if(address >= 9000 and address <= 10999):
				self.gbool[address] = value
		#Temporales Globales
		if(address >= 11000 and address <= 20999):
			if(address >= 11000 and address <= 12999):
				self.tint[address] = value
			if(address >= 13000 and address <= 14999):
				self.tfloat[address] = value
			if(address >= 15000 and address <= 16999):
				self.tchar[address] = value
			if(address >= 17000 and address <= 18999):
				pass#self.tstring[address] = value
			if(address >= 19000 and address <= 20999):
				self.tbool[address] = value
		#Locales
		if(address >= 21000 and address <= 30999):
			if(address >= 21000 and address <= 22999):
				self.lint[address] = value
			if(address >= 23000 and address <= 24999):
				self.lfloat[address] = value
			if(address >= 25000 and address <= 26999):
				self.lchar[address] = value
			if(address >= 27000 and address <= 28999):
				pass#self.lstring[address] = value
			if(address >= 29000 and address <= 30999):
				self.lbool[address] = value
		#Temporales Locales
		if(address >= 31000 and address <= 40999):
			if(address >= 31000 and address <= 32999):
				self.tint[address] = value
			if(address >= 33000 and address <= 34999):
				self.tfloat[address] = value
			if(address >= 35000 and address <= 36999):
				self.tchar[address] = value
			if(address >= 37000 and address <= 38999):
				pass#self.tstring[address] = value
			if(address >= 39000 and address <= 40999):
				self.tbool[address] = value
		#Constantes
		if(address >= 41000 and address <= 50999):
			if(address >= 41000 and address <= 42999):
				self.cint[address] = value
			if(address >= 43000 and address <= 44999):
				self.cfloat[address] = value
			if(address >= 45000 and address <= 46999):
				self.cchar[address] = value
			if(address >= 47000 and address <= 48999):
				self.cstring[address] = value
			if(address >= 49000 and address <= 50999):
				self.cbool[address] = value
		#Pointers
		if(address >= 51000 and address <= 60999):
			if(address >= 51000 and address <= 52999):
				self.pointers[address] = value

	#Mismo if pero ahora para regresar el valor
	def getValue(self, address):
		#Global
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				return int(self.gint[address])
			if(address >= 3000 and address <= 4999):
				return float(self.gfloat[address])
			if(address >= 5000 and address <= 6999):
				return self.gchar[address]
			if(address >= 7000 and address <= 8999):
				pass#return self.gstring[address]
			if(address >= 9000 and address <= 10999):
				return self.gbool[address]
		#Temporales Globales
		if(address >= 11000 and address <= 20999):
			if(address >= 11000 and address <= 12999):
				return int(self.tint[address])
			if(address >= 13000 and address <= 14999):
				return float(self.tfloat[address])
			if(address >= 15000 and address <= 16999):
				return self.tchar[address]
			if(address >= 17000 and address <= 18999):
				pass#return self.tstring[address]
			if(address >= 19000 and address <= 20999):
				return self.tbool[address]
		#Locales
		if(address >= 21000 and address <= 30999):
			if(address >= 21000 and address <= 22999):
				return int(self.lint[address])
			if(address >= 23000 and address <= 24999):
				return float(self.lfloat[address])
			if(address >= 25000 and address <= 26999):
				return self.lchar[address]
			if(address >= 27000 and address <= 28999):
				pass#return self.lstring[address]
			if(address >= 29000 and address <= 30999):
				return self.lbool[address]
		#Temporales Locales
		if(address >= 31000 and address <= 40999):
			if(address >= 31000 and address <= 32999):
				return int(self.tint[address])
			if(address >= 33000 and address <= 34999):
				return float(self.tfloat[address])
			if(address >= 35000 and address <= 36999):
				return self.tchar[address]
			if(address >= 37000 and address <= 38999):
				pass#return self.tstring[address] 
			if(address >= 39000 and address <= 40999):
				return bool(self.tbool[address])
		#Constantes
		if(address >= 41000 and address <= 50999):
			if(address >= 41000 and address <= 42999):
				return int(self.cint[address])
			if(address >= 43000 and address <= 44999):
				return float(self.cfloat[address])
			if(address >= 45000 and address <= 46999):
				return self.cchar[address]
			if(address >= 47000 and address <= 48999):
				return self.cstring[address]
			if(address >= 49000 and address <= 50999):
				return self.cbool[address]
		#Pointers
		if(address >= 51000 and address <= 60999):
			if(address >= 51000 and address <= 52999):
				return self.pointers[address]


class instances(object):
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

	def indexVar(self, address, value, instance):
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				self.instancelst[instance]['int'][address] = value
			if(address >= 3000 and address <= 4999):
				self.float[address] = value
			if(address >= 5000 and address <= 6999):
				self.char[address] = value
			if(address >= 7000 and address <= 8999):
				pass#self.gstring[address] = value
			if(address >= 9000 and address <= 10999):
				self.bool[address] = value

	def getValue(self, address, instance):
		if(address >= 1000 and address <= 10999):
			if(address >= 1000 and address <= 2999):
				return int(self.instancelst[instance]['int'][address])
			if(address >= 3000 and address <= 4999):
				return float(self.float[address])
			if(address >= 5000 and address <= 6999):
				return self.char[address]
			if(address >= 7000 and address <= 8999):
				pass#return self.gstring[address]
			if(address >= 9000 and address <= 10999):
				return self.bool[address]



memory = memory()
#Reconstruye la memoria global que tenemos en un archivo
def rebuildCtes():
	with open('compiled.out') as infile:
		data = json.load(infile)
		ctes = data['ctes']['values']
		vars = data['global']['vars']
		for cte in ctes:
			memory.indexVar(ctes[cte]['address'],cte)
		#Si no tiene valor le asigna su mismo address como un lenguaje normal
		for var in vars:
			memory.indexVar(vars[var]['address'],vars[var]['address'])
#Reconstruye la memoria de una funcion que tenemos en un archivo
def rebuildFunctionMemory(funId):
	with open('compiled.out') as infile:
		data = json.load(infile)
		vars = data[funId]['vars']
		#Si no tiene valor le asigna su mismo address como un lenguaje normal
		for var in vars:
			memory.indexVar(vars[var]['address'],vars[var]['address'])			
def era(funId):
	with open('compiled.out') as infile:
		data = json.load(infile)
		nParams = data[funId]['nParams']


#Ejecuta el codigo de cuadruplos
def excecute(quads):
	instace = instances()
	instace.addInstance('global')
	instace.indexVar(1000, 25, 'global')

	print(instace.getValue(1000, 'global'))

	rebuildCtes()
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
				pos3 = memory.getValue(pos3)
		if pos2 != None:
			if pos2 >= 51000:
				pos2 = memory.getValue(pos2)
		if pos1 != None:
			if pos1 >= 51000:
				pos1 = memory.getValue(pos1)


		#Operaciones basicas
		if operator == 1:
			res = memory.getValue(pos1) + memory.getValue(pos2)
			memory.indexVar(pos3, res)
		elif operator == 2:
			res = memory.getValue(pos1) - memory.getValue(pos2)
			memory.indexVar(pos3, res)
		elif operator == 3:
			res = memory.getValue(pos1) * memory.getValue(pos2)
			memory.indexVar(pos3, res)
		elif operator == 4:
			res = memory.getValue(pos1) / memory.getValue(pos2)
			memory.indexVar(pos3, res)
		#Operaciones Logicas
		elif operator == 5:
			if (memory.getValue(pos1) and memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 6:
			if (memory.getValue(pos1) or memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 7:
			if (memory.getValue(pos1) > memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 8:
			if (memory.getValue(pos1) < memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 9:
			if (memory.getValue(pos1) >= memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 10:
			if (memory.getValue(pos1) <= memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 11:
			if (memory.getValue(pos1) != memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		elif operator == 12:
			if (memory.getValue(pos1) == memory.getValue(pos2)):
				res = True
			else:
				res = False
			memory.indexVar(pos3, res)
		#Asignacion
		elif operator == 13:
			res = memory.getValue(pos3)
			#print(pos1,'=',pos3)
			memory.indexVar(pos1, res)
		#Print
		elif operator == 14:
			#print(pos3)
			res = memory.getValue(pos3)
			print(res)
		#Read
		elif operator == 15:
			res = input()
			memory.indexVar(pos3, res)
		#Gotos
		elif operator == 16:
			i = pos3-1
		elif operator == 17:
			if(not memory.getValue(pos1)):
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
			if memory.getValue(quads[i][1]) > quads[i][3]:
				print("Arreglo Fuera de rango")
				sys.exit()
		elif operator == 25:
			res = quads[i][1] + memory.getValue(quads[i][2])
			memory.indexVar(quads[i][3], res)
		i+=1
