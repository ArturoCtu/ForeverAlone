import json
#Memoria Virtual segmentada
class memory(object):
	def __init__(self):
		self.int = {}
		self.float = {}
		self.char = {}
		self.string = {}
		self.bool = {}

	def indexVartoMem(self, address, value):
		if(address >= 41000 and address <= 42999):
			self.int[address] = value
		if(address >= 43000 and address <= 44999):
			self.float[address] = value
		if(address >= 45000 and address <= 46999):
			self.char[address] = value
		if(address >= 47000 and address <= 48999):
			self.string[address] = value
		if(address >= 49000 and address <= 50999):
			self.bool[address] = value

	def getValuefromMem(self, address):
		if(address >= 41000 and address <= 42999):
			return int(self.int[address])
		if(address >= 43000 and address <= 44999):
			return float(self.float[address])
		if(address >= 45000 and address <= 46999):
			return self.char[address]
		if(address >= 47000 and address <= 48999):
			return self.string[address]
		if(address >= 49000 and address <= 50999):
			return self.bool[address]

class memSegment(object):
	def __init__(self):
		self.segmentlst = {'global', 'glTemp', 'local', 'locTemp', 'ctes'}
		self.segmentlst['ctes'] = {
			'memory' : memory()
		}

	def indexVar(self, address, value):
		self['ctes'].indexVartoMem(address, value)

	def getValue(self, address):
		self['ctes'].getValuefromMem(address)
			
memory = memSegment()

#Ejecuta el codigo de cuadruplos
def excecute(quads):
	with open('compiled.out') as infile:
		data = json.load(infile)
		ctes = data['ctes']['values']
		vars = data['global']['vars']
		for cte in ctes:
			memory.indexVar(ctes[cte]['address'],cte)


		print(memory.getValue(47000))