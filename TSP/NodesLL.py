from .Node import Node
from math import sqrt, pow
import random
class TSPNodesLL:

	def __init__(self):
		self.head = None

	#insert new node after nother node
	def insertAfter(self, prev_node, new_node):
		new_node.next = prev_node.next
		prev_node.next = new_node
		new_node.prev = prev_node
		if new_node.next is not None: 
			new_node.next.prev = new_node

	def insertBefore(self, next_node, new_node):
		print(self.head.getIndex())
		new_node.next = next_node
		new_node.prev = next_node.prev
		if new_node.prev is not None:
			next_node.prev.next = new_node
		else:
			self.head = new_node
		next_node.prev = new_node

    #Find node given the index
	def getNodeByIndex(self, index):
		current_node = self.head
		while(current_node.getIndex() != index):
			current_node = current_node.next
			if current_node is None: 
				print("index doesn't exist in getNodeByIndex")
				return
		return current_node

    #add node to end of list
	def append(self, new_node):
		new_node.next = None
		if self.head is None: 
			new_node.prev = None
			self.head = new_node 
			return 
		last = self.head
		while(last.next is not None):
			last = last.next
		last.next = new_node
		new_node.prev = last

	#new node at beginning of list
	def push(self, new_node):
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node


	def printList(self):
		current_node = self.head
		while current_node is not None:
			print(current_node.getIndex(), end=", ") 
			current_node = current_node.next
		print()


	def costFinder(self):
		head = self.head
		node1 = self.head
		node2 = node1.getNext()
		total_cost = 0
		while node2 is not None:
			total_cost += sqrt((pow(node2.getXCord() - node1.getXCord(), 2)) + (pow(node2.getYCord() - node1.getYCord(), 2)))
			node1 = node1.getNext()
			node2 = node2.getNext()
			#print(total_cost)
		total_cost += sqrt((pow(node1.getXCord() - head.getXCord(), 2)) + (pow(node1.getYCord() - head.getYCord(), 2))) 
		return total_cost

	def resetList(self):
		self.head = None

	def listSize(self):
		node = self.head
		i = 0
		while(node is not None):
			i += 1
			node = node.getNext()
		return i

	def shuffleList(self):
		node_set = []
		size = self.listSize()
		node = self.head 
		while node is not None:
			node_set.append(node)
			node = node.getNext()
		random.shuffle(node_set)
		self.head = None 
		for i in range(0, len(node_set)):
			self.append(node_set[i])




























