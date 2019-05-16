from NodesLL import TSPNodesLL
from Node import Node
from FileReader import FileReader
import os

def main(): 
	cwd = os.getcwd()
	filename = cwd + '/Problem_Sets/a280.xlsx'

	test1 = Node().newNode(1, 5, 10)
	test2 = Node().newNode(2, 5, 10)
	test3 = Node().newNode(3, 5, 10)
	newLL = TSPNodesLL()
	newLL2 = TSPNodesLL()
	#print(anode.getIndex())
	test4 = Node().newNode(4, 5, 10)

	newLL.append(test1)
	newLL.append(test2)
	newLL.append(test3)
	newLL.insertBefore(test1, test4)
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
	print(sample.costFinder())

if __name__ == "__main__":
	main()