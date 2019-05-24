from ..NodesLL import TSPNodesLL
from ..Node import Node
import random

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
		temp = self.findEdges(self.brightest, self.ffPop[3])
		print(temp)
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


	def findEdges(self, best_fly, random_fly):
		edges = [[],[]]
		random_pos = random.randint(1,best_fly.listSize()-1)
		#Would be slightly more efficient to make this return a node and pull index rather than getting nodes in both methods
		index1 = best_fly.getIndexByPos(random_pos)
		node1 = best_fly.getNodeByIndex(index1)
		node2 = node1.getNext()
		index2 = node2.getIndex()
		random_node1 = random_fly.getNodeByIndex(index1)
		random_node2 = random_fly.getNodeByIndex(index2)
		pos1 = random_fly.getPosByIndex(index1)
		pos2 = random_fly.getPosByIndex(index2)
		reverse = False
		#If the X and Y is reversed for the random node it will swap random_node1 and random_node2 to match the index's with the best_fly X/Y
		if pos1 > pos2:
			reverse = True
			temp = Node().copyNode(random_node1)
			random_node1 = Node().copyNode(random_node2)
			random_node2 = temp
		backup_r1 = Node().copyNode(random_node1)
		backup_r2 = Node().copyNode(random_node2)
		#best_fly.printList()
		#random_fly.printList()
		
		# Create X set of edges
		# This will take the X (left) location based on the best_fly and work outwords to determine if the random_list has any matching nodes to collect in a set
		# Depending on if the random_fly X/Y needed flipped (reversed) it will either be the left node also and work towards the left 
		# or the right node and work towards the right (reversed = True)
		while node1 is not None and random_node1 is not None and random_node2 is not None:
			if reverse is False:
				if node1.getIndex() == random_node1.getIndex():
					edges[0].append(random_node1.getIndex())
					node1 = node1.getPrev()
					random_node1 = random_node1.getPrev()
				else:
					break
			else:
				if node1.getIndex() == random_node2.getIndex():
					edges[0].append(random_node2.getIndex())
					node1 = node1.getPrev()
					random_node2 = random_node2.getNext()
				else:
					break
		#Resets the node starting location for the random location because either could have changed depending on reversed=True/Fale
		random_node1 = backup_r1
		random_node2 = backup_r2
		# This will create edge set for the best fly's Y(right) location and work the same as the above section.
		# The main difference is node 2 will work towards it's outside which is to the right instead of the left.
		while node2 is not None and random_node1 is not None and random_node2 is not None:
			if reverse is False:
				if node2.getIndex() == random_node2.getIndex():
					edges[1].append(random_node2.getIndex())
					node2 = node2.getNext()
					random_node2 = random_node2.getNext()
				else:
					break
			else:
				if node2.getIndex() == random_node1.getIndex():
					edges[1].append(random_node1.getIndex())
					node2 = node2.getNext()
					random_node1 = random_node1.getPrev()
				else:
					break
		#Will return a 2D List where edges[0][:] is the X edge set and edges[1][:] is the Y edge set
		return edges


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




	#def trimPop():
	#If I store the top (n) costs along with their index I wont have to double lists and then trim them because I can just keep popping the highest cost
	#prob just use old way

