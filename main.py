from TSP.NodesLL import TSPNodesLL
from TSP.Node import Node
from TSP.FileReader import FileReader
from TSP.GraphTSP import createTSPGraph
from TSP.Firefly import Firefly
import matplotlib.pyplot as plt
from os import getcwd


def main(): 
	cwd = getcwd()
	filename = cwd + '/Problem_Sets/a280.xlsx'
	newLL = TSPNodesLL()
	x = FileReader(filename, newLL).generateLL()
	newLL.printList()
	print(newLL.costFinder())
	firefly = Firefly.Firefly(newLL, 20, 30).performFirefly()
	#newLL.removeNode(newLL.getNodeByIndex(14))
	#newLL.printList()
	plt.show()
	#t = createTSPGraph(sample)
	#t.show()

if __name__ == "__main__":
	main()