from ..NodesLL import TSPNodesLL
from ..Node import Node

class Firefly():

	def __init__(self, ogList, popsize, generations):
		self.ogList = ogList
		self.popsize = popsize
		self.generations = generations
		self.brightest = ogList

	def performFirefly(self):
		ffPopulation = []
		orig_list = self.ogList.copyList()
		ffPopulation.append(orig_list.copyList())
		for i in range(1, self.popsize):
			temp = orig_list.copyList()
			temp.shuffleList()
			ffPopulation.append(temp)

		#operators()
		#returnBrightest()



	#def trimPop():
	#If I store the top (n) costs along with their index I wont have to double lists and then trim them because I can just keep popping the highest cost

	#def xToy(self, best_fly, random_fly):


	#def yTox(self, best_fly, random_fly):


	#def xFromy(self, best_fly, random_fly):


	#def yFromx(self, best_fly, random_fly):


	#def mutation(self, best_fly):