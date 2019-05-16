from NodesLL import TSPNodesLL
from Node import Node
import pandas as pd


class FileReader():

	def __init__(self, filename, nodesLL):
		self.__filename = filename
		self.__nodesLL = nodesLL

	#Run all functions and return the newly generated linked list. This will act as a the intial route
	def generateLL(self):
		file = self.loadFile()
		self.excelToNodes(file)
		return self.__nodesLL
	
	#Pull file from excel using filename	
	def loadFile(self):
		file = pd.read_excel(self.__filename, skiprows=6, header=None)
		return file

	#This function will populate your nodesLL with nodes as given by the excel file
	def excelToNodes(self,file):
		print("start")
		i=0
		while(file[0][i] != 'EOF'):
			#for x in range(3):
				#print(file[x][i], end=" ")
			self.__nodesLL.append(Node().newNode(file[0][i],file[1][i],file[2][i]))
			#print()
			i += 1
