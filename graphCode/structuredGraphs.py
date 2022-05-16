#-------------------------------------------
#  structuredGraphs.py
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()

# add vertices
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

# add edges
g.addEdge(0,1,1)
g.addEdge(1,0,1)

g.addEdge(0,2,1)
g.addEdge(2,0,1)

g.addEdge(1,3,1)
g.addEdge(3,1,1)

g.addEdge(2,3,1)
g.addEdge(3,2,1)


print(g)



