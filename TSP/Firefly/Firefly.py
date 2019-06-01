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
		for x in range(0, self.generations):
			for i in range(0, self.popsize):
				edge_set = self.findEdges(self.brightest, self.ffPop[3])
				self.xToy(self.ffPop[i], edge_set)
				self.yTox(self.ffPop[i], edge_set)
				self.xFromy(self.ffPop[i], edge_set)
				self.yFromx(self.ffPop[i], edge_set)
				self.mutation(self.brightest)
			self.trimPop()
			print(self.brightest.costFinder())

	def findBrightest(self):
		brighter = 99999999
		for i in range(0, len(self.ffPop)):
			temp = self.ffPop[i].costFinder()
			if temp < brighter:
				brighter = temp
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
	#  ---Y~~~~~~~~X---
	def mutation(self, best_fly):
		random1 = random.randint(1, best_fly.listSize())
		random2 = random.randint(1, best_fly.listSize())
		new_fly = best_fly.copyList()
		while random1 == random2 :
			random2 = random.randint(1, best_fly.listSize())
			while random1 == 1 and random2 == best_fly.listSize() or random2 == 1 and random1 == best_fly.listSize():
				random2 = random.randint(1, best_fly.listSize())
		if random1 > random2:
			temp = random1
			random1 = random2
			random2 = temp
		index1 = new_fly.getIndexByPos(random1)
		index2 = new_fly.getIndexByPos(random2)
		range_size = (random2-random1)
		node1 = new_fly.getNodeByIndex(index1)
		node2 = new_fly.getNodeByIndex(index2)
		for _ in range(range_size):
			temp = node2.getPrev()
			new_fly.removeNode(node2)
			new_fly.insertBefore(node1, node2)
			node2 = temp
		self.ffPop.append(new_fly)
			
	#  ---X--------Y---
	#  -----------XY---
	def xToy(self, random_fly, edges):
		x_edge = []
		x_edge = edges[0]
		new_fly = random_fly.copyList()
		y_node = new_fly.getNodeByIndex(edges[1][0])
		for x_index in x_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(x_index)
			new_fly.removeNode(temp_node)
			new_fly.insertBefore(y_node, temp_node)
		self.ffPop.append(new_fly)

	#  ---X--------Y---
	#  ---XY-----------
	def yTox(self, random_fly, edges):
		y_edge = []
		y_edge = edges[1]
		new_fly = random_fly.copyList()
		x_node = new_fly.getNodeByIndex(edges[0][0])
		for y_index in y_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(y_index)
			new_fly.removeNode(temp_node)
			new_fly.insertAfter(x_node, temp_node)
		self.ffPop.append(new_fly)

	#  ---X--------Y---
	#  ------------YX--
	def xFromy(self, random_fly, edges):
		x_edge = edges[0]
		y_edge = edges[1]
		new_fly = random_fly.copyList()
		y_node = new_fly.getNodeByIndex(edges[1][0])
		for x_index in x_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(x_index)
			new_fly.removeNode(temp_node)
			new_fly.insertAfter(y_node, temp_node)
		x_node = new_fly.getNodeByIndex(edges[0][0])
		for y_index in y_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(y_index)
			new_fly.removeNode(temp_node)
			new_fly.insertBefore(x_node, temp_node)
		self.ffPop.append(new_fly)


	#  ---X--------Y---
	#  ---YX-----------
	def yFromx(self, random_fly, edges):
		x_edge = edges[0]
		y_edge = edges[1]
		new_fly = random_fly.copyList()
		x_node = new_fly.getNodeByIndex(edges[0][0])
		for y_index in y_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(y_index)
			new_fly.removeNode(temp_node)
			new_fly.insertBefore(x_node, temp_node)
		y_node = new_fly.getNodeByIndex(edges[1][0])	
		for x_index in x_edge[::-1]:
			temp_node = new_fly.getNodeByIndex(x_index)
			new_fly.removeNode(temp_node)
			new_fly.insertAfter(y_node, temp_node)
		self.ffPop.append(new_fly)

	def trimPop(self):
		new_pop = []
		#self.ffPop
		for i in range(0, self.popsize):
			temp = self.findBrightest()
			new_pop.append(temp)
			self.ffPop.remove(temp)
		self.ffPop = new_pop


