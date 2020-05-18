class avail(object):
 	def __init__(self):
 		self.availC = 0
 		self.temp = "t"

 	def next(self):
 		self.availC+=1
 		return self.temp + str(self.availC)

 	def reset(self):
 		self.availC = 0