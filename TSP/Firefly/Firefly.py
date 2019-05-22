from ..NodesLL import TSPNodesLL
from ..Node import Node

class Firefly():

	def __init__(self, ogList, popsize, generations):
		self.ogList = ogList
		self.popsize = popsize
		self.generations = generations

	def performFirefly(self):
		ffPopulation = []
		orig_list = self.ogList.copyList()
		ffPopulation.append(orig_list.copyList())
		for i in range(1, self.popsize):
			temp = orig_list.copyList()
			temp.shuffleList()
			ffPopulation.append(temp)
		

		#for i in range(0, self.popsize):
			#print(i)
			#print(ffPopulation[i].printList())
			#print(ffPopulation[i].listSize())

