class Base:
	def __init__(self,regno,color):
		self.color =  color
		self.regno = regno

class Car(Base):

	def __init__(self,regno,color):
		Base.__init__(self,regno,color)

	def getType(self):
		return "Car"
