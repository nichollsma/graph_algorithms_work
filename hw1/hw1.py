import numpy as np
data = np.loadtxt("adj_mx.txt", delimiter=",")
num_rows = np.shape(data)[0]
maxDegree = 0
maxNode = -1

for i in range(num_rows):
    degCount = 0
    for j in range(num_rows):
        if data[i][j] == 1:
            degCount += 1
    if degCount > maxDegree:
        maxNode = i
        maxDegree = degCount
    print("Node %d has a degree of %d" % (i, degCount))
print()

if maxNode == -1:
    print("There is not a node with a maximum degree")
    print()
else:
    print("Node %d has the maximum degree of %d" % (maxNode, maxDegree))
    print()

edgeList_a = []
edgeList_b = []
edgeListF = []
for i in range(num_rows):
    for j in range(num_rows):
        if data[i][j] == 1:
            edgeList_a.append(i)
            edgeList_b.append(j)
for i in range(len(edgeList_a)):
    a = edgeList_a[i]
    b = edgeList_b[i]
    if ("(%d, %d)" % (b, a)) not in edgeListF:
        edgeListF.append("(%d, %d)" % (a, b))
print("Edge List:")
print(edgeListF)

adjList = [[] for i in range(num_rows)]
for i in range(len(edgeList_a)):
    a = edgeList_a[i]
    b = edgeList_b[i]
    adjList[a].append(b)
print("Adjacency List:")
for i in range(len(adjList)):
    print(i, ":", adjList[i])
