from ..NodesLL import TSPNodesLL
from ..Node import Node

class Firefly():

	def __init__(self, ogList, popsize, generations):
		self.ogList = ogList
		self.popsize = popsize
		self.generations = generations
		self.brightest = ogList
		self.ffPop = []

	def performFirefly(self):
		orig_list = self.ogList.copyList()
		self.ffPop.append(orig_list.copyList())
		for i in range(1, self.popsize):
			temp = orig_list.copyList()
			temp.shuffleList()
			self.ffPop.append(temp)


		print("bright is")
		print(self.findBrightest().costFinder())
		#operators()
		#returnBrightest()

	def findBrightest(self):
		brightest = 99999999
		bright_node = None
		for i in range(0, len(self.ffPop)):
			temp = self.ffPop[i].costFinder()
			if temp < brightest:
				brightest = temp
				self.brightest = self.ffPop[i]
		return self.brightest


	#def trimPop():
	#If I store the top (n) costs along with their index I wont have to double lists and then trim them because I can just keep popping the highest cost
	#prob just use old way
	


	#def findEdge(self, best_fly, random_fly):




	#  ---X--------Y---
	#  -----------XY---
	#def xToy(self, best_fly, random_fly):




	#  ---X--------Y---
	#  ---XY-----------
	#def yTox(self, best_fly, random_fly):




	#  ---X--------Y---
	#  ------------YX--
	#def xFromy(self, best_fly, random_fly):




	#  ---X--------Y---
	#  ---YX-----------
	#def yFromx(self, best_fly, random_fly):




	#  ---X--------Y---
	#  ---Y~~~~~~~~X---
	#def mutation(self, best_fly):





