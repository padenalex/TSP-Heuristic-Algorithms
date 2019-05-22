class Node():

	def __init__(self):
		#Could make a starting location from avg of all nodes (or such) rather than using one of the points but will skew from public best results comparison
		self.next = None
		self.prev = None
		self.__index = None
		self.__xcord = None
		self.__ycord = None

	#set index and cords on an existing node
	def setNode(self, index, xcord, ycord):
		self.next = None
		self.prev = None
		self.__index = index
		self.__xcord = xcord
		self.__ycord = ycord

	#Create a new node and return it
	def newNode(self, index, xcord, ycord):
		self.next = None
		self.prev = None
		self.__index = index
		self.__xcord = xcord
		self.__ycord = ycord
		return self

	def getIndex(self):
		return self.__index

	def getXCord(self):
		return self.__xcord

	def getYCord(self):
		return self.__ycord

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev