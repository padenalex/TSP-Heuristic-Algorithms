from TSP.NodesLL import TSPNodesLL
from TSP.Node import Node
from TSP.FileReader import FileReader
from TSP.GraphTSP import createTSPGraph
from TSP.Firefly import Firefly
import matplotlib.pyplot as plt
from os import getcwd

#TODO
#random idea double mutate after ~10% of generations with no change
#optimize trimp population because it's v/ inefficient atm

def main(): 
	cwd = getcwd()
	filename = cwd + '/Problem_Sets/eil51.xlsx'
	newLL = TSPNodesLL()
	x = FileReader(filename, newLL).generateLL()
	newLL.printList()
	#print(newLL.costFinder())
	newLL.shuffleList()
	firefly = Firefly.Firefly(newLL, 8, 500).performFirefly()
	#newLL.removeNode(newLL.getNodeByIndex(14))
	#newLL.printList()
	plt.show()
	t = createTSPGraph(firefly)
	t.show()

if __name__ == "__main__":
	main()