import matplotlib.pyplot as plt
from NodesLL import TSPNodesLL
from Node import Node


#plt.arrow(0,0,1,3)
#plt.arrow(1,3,2,4)
#plt.show()
print("Dd")

def createTSPGraph(nodesLL):
    #plt.plot(0, 0,150,150)
    node = nodesLL.head
    x = []
    y = []
    while(node is not None):
        x.append(node.getXCord())
        y.append(node.getYCord())
        node = node.getNext()
    plt.plot(x,y,'co')
    arrow_size = float(max(x))/float(100)
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = arrow_size, length_includes_head=True)
    for i in range(0, len(x)-1):
        try:
            plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), head_width = arrow_size, length_includes_head = True)
        except:
            pass
    plt.show(block=False)
    return plt