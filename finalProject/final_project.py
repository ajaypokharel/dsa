import math
from random import random
from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()


def make_graph(n):
    for j in range(n * n):
        g.addVertex(j)

    vert_rand = []
    for j in range(n * n):
        rand = random()
        vert_rand.append(rand)

    for j in range(n * n):
        if j - 1 >= 0 and j % n > 0:
            g.addEdge(j, j - 1, 1)
        if j + 1 <= n * n - 1 and (j + 1) % n > 0:
            g.addEdge(j, j + 1, 1)
        if j - n >= 0:
            g.addEdge(j, j - n, 1)
        if j + n <= n * n - 1:
            g.addEdge(j, j + n, 1)

    for j in range(1, n * n - 1):
        if vert_rand[j] < 0.25:
            if j - 1 > 0 and j % n > 0:
                g.removeEdge(j, j - 1)
                g.removeEdge(j - 1, j)
            if j + 1 < n * n - 1 and (j + 1) % n > 0:
                g.removeEdge(j, j + 1)
                g.removeEdge(j + 1, j)
            if j - n > 0:
                g.removeEdge(j, j - n)
                g.removeEdge(j - n, j)
            if j + n < n * n - 1:
                g.removeEdge(j, j + n)
                g.removeEdge(j + n, j)


def dijkstra(g, i):
    n = g.sizeVertices()  # number of vertices to add
    D = []  # D[i] is the cost/distance to add vertex i
    V = []  # V[i] is the vertex in the MST adjacent to i
    for j in range(0, n):
        D.append(float('inf'))
        V.append(None)

    D[i] = 0

    g.getVertex(i).setMark()

    minIndex = i
    count = 1

    while count < n:

        for w in g.neighboringVertices(minIndex):
            if not w.isMarked():
                k = w.getLabel()
                edgeVal = g.getEdge(minIndex, k).getWeight()
                if D[k] > edgeVal + D[minIndex]:
                    D[k] = D[minIndex] + edgeVal
                    V[k] = minIndex

        # find the first unvisited vertex
        k = -1
        j = 0
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

        g.getVertex(minIndex).setMark()
        count += 1

    return D, V


def find_shortest_path():
    n = int(input("Please enter the size of the matrix: "))

    print("Creating your graph...")
    make_graph(n)
    print()
    print("HERE'S YOUR GRAPH: ")
    print(g)

    # find the shortest path using Dijkstra
    D, V = dijkstra(g, 0)
    print()
    print("The Weight Array for the shortest path to each vertex: ", D)
    print("The Closest Vertex for each shortest edge weight: ", V)

    path = []
    print()
    if D[-1] < math.inf:
        i = - 1
        while i < len(V) - 1:
            if i == 0:
                break
            else:
                path.append(V[i])  # V[V[i]]
                i = V[i]
        path.reverse()
        path.append(len(D) - 1)

        for i in range(len(path)):
            path[i] = str(path[i])

        print("The shortest path length from start to end vertex is: ", len(path) - 1)
        print("The shortest path from start to end vertex is: ", " --> ".join(path))

    else:
        print("The path does not exist")


find_shortest_path()
