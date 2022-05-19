#-----------------------------------------------
#  CSC 211 Dijkstra's Algorithm Implementation
#-----------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

def dijkstra(g, i):
    '''
    Dijkstra's Algorithm
    for graph g, starting with vertex i
    '''

    n = g.sizeVertices()  # number of vertices to add
    D = []  # D[i] is the cost/distance to add vertex i
    V = []  # V[i] is the vertex in the MST adjacent to i
    count = 0
    for j in range(0, n):
        D.append(float('inf'))
        V.append(None)

    # create MST and add vertex i into it
    D[i] = 0
    g.getVertex(i).setMark()
    # recently added vertex
    minIndex = i

    # add vertices until the mst has as many vertices as g
    while count < n-1:

        # update D and V based on minIndex
        for w in g.neighboringVertices(minIndex):
            if not w.isMarked():
                k = w.getLabel()
                edgeVal = g.getEdge(minIndex, k).getWeight()
                if D[k] > edgeVal:
                    D[k] = D[minIndex] + edgeVal
                    V[k] = minIndex

        # find the first unvisited vertex
        k = -1
        j = 1
        while k < 0 and j < n:
            if not g.getVertex(j).isMarked():
                k = j
            j += 1

        # find minimum cost unvisited vertex
        minIndex = k
        for j in range(0, n):
            if not g.getVertex(j).isMarked():
                if D[j] < D[minIndex]:
                    minIndex = j

        # add new vertex to the MST and mark it in g

        g.getVertex(minIndex).setMark()
        count += 1
    print("D =>", D)
    print("V ==>", V)
#-----------------------------------
# Test out the method below

g = LinkedDirectedGraph()

# add vertices
# for i in range(0,9):
#     g.addVertex(i)

# add edges
# g.addEdge(0,1,3.8)
# g.addEdge(1,0,3.8)
# g.addEdge(1,2,1.3)
# g.addEdge(2,1,1.3)
# g.addEdge(3,4,1.6)
# g.addEdge(4,3,1.6)
# g.addEdge(4,5,3.1)
# g.addEdge(5,4,3.1)
# g.addEdge(6,7,4.3)
# g.addEdge(7,6,4.3)
# g.addEdge(7,8,1.1)
# g.addEdge(8,7,1.1)
# g.addEdge(0,3,0.6)
# g.addEdge(3,0,0.6)
# g.addEdge(1,4,1.2)
# g.addEdge(4,1,1.2)
# g.addEdge(2,5,0.7)
# g.addEdge(5,2,0.7)
# g.addEdge(3,6,2.2)
# g.addEdge(6,3,2.2)
# g.addEdge(4,7,3.4)
# g.addEdge(7,4,3.4)
# g.addEdge(5,8,1.2)
# g.addEdge(8,5,1.2)


for i in range(0, 6):
    g.addVertex(i)

g.addEdge(0, 1, 0.4)
g.addEdge(1, 0, 0.4)
g.addEdge(0, 5, 2.2)
g.addEdge(5, 0, 2.2)
g.addEdge(0, 2, 0.2)
g.addEdge(2, 0, 0.2)
g.addEdge(1, 2, 0.1)
g.addEdge(2, 1, 0.1)
g.addEdge(1, 3, 0.2)
g.addEdge(3, 1, 0.2)
g.addEdge(2, 3, 0.6)
g.addEdge(3, 2, 0.6)
g.addEdge(2, 4, 0.8)
g.addEdge(4, 2, 0.8)
g.addEdge(3, 4, 0.3)
g.addEdge(4, 3, 0.3)
g.addEdge(3, 5, 0.5)
g.addEdge(5, 3, 0.5)

print(g)

# try it out
dijkstra(g,0)

