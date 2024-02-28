
class Class1:
	def __init__(self, dim):
		self.dim = dim 
		self.cost = 0
		self.fin = 0
	def calc(self):
		self.fin = (0.05 * self.dim) * self.dim
		self.cost = 1 + 0.75 + self.fin	
		
	def costt(self):
		return self.cost
	def find(self):
		return self.fin 
	
