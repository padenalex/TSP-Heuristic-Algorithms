from NodesLL import TSPNodesLL
from Node import Node
from FileReader import FileReader
from GraphTSP import createTSPGraph
import matplotlib.pyplot as plt
from os import getcwd

#TODO Need to make permanent head of 0,0

def main(): 
	cwd = getcwd()
	filename = cwd + '/Problem_Sets/a280.xlsx'

	test1 = Node().newNode(1, 5, 10)
	test2 = Node().newNode(2, 11, 28)
	test3 = Node().newNode(3, 31, 48)
	test4 = Node().newNode(4, 50, 50)
	newLL = TSPNodesLL()
	newLL2 = TSPNodesLL()
	#print(anode.getIndex())


	newLL.append(test1)
	newLL.append(test2)
	newLL.append(test3)
	newLL.append(test4)
	newLL.printList()

	gotNode = newLL.getNodeByIndex(3)
	#print("ttttt")
	#print(gotNode.getIndex())

	x = FileReader(filename, newLL2)
	sample = x.generateLL()
	print()
	print("run")
	print()
	sample.printList()
	print()
	#print(sample.costFinder())
	plt = createTSPGraph(sample)

	#sample.resetList()
	sample.printList()
	print("s")
	sample.shuffleList()
	sample.printList()
	plt.show()
	t = createTSPGraph(sample)
	t.show()

if __name__ == "__main__":
	main()