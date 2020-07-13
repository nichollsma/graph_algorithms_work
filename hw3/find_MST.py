import numpy as np
data = np.loadtxt("MST_mx1.txt", delimiter=",")


def is_tree(adj_mx):
    starting_points = [0]
    visited = []
    while len(starting_points) > 0:
        start = starting_points.pop()
        visited.append(start)
        for i in range(len(adj_mx[start])):
            if adj_mx[start][i] == 1:
                if not visited.__contains__(i) and starting_points.__contains__(i):
                    print("This graph is NOT a tree.")
                    return False
                if not visited.__contains__(i) and not starting_points.__contains__(i):
                    starting_points.append(i)

    print("This graph is a tree.")
    return True
#    number_of_nodes = len(adj_mx)
#    if len(visited) == number_of_nodes:
#        print("This graph is a tree.")
#        return True
#    else:
#        print("This graph is NOT a tree.")
#        return False


def read_file(filename):
    mx = np.loadtxt(filename, delimiter=",")
    return mx


def find_MST(wt_mx):
    num_nodes = len(wt_mx)
    num_edges = 0
    edges = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0 and i<j:
                edges.append((data[i][j], i, j))

    sorted_edges = sorted(edges)
    mst_mx = np.zeros([len(data), len(data)])

    print(mst_mx)

    for i in range(len(sorted_edges)):
        if num_edges == num_nodes - 1:
            break
        weight, nodeA, nodeB = sorted_edges[i]
        print(weight, nodeA, nodeB)

        mst_mx[nodeA][nodeB] = weight
        mst_mx[nodeB][nodeA] = weight
        num_edges += 1

        print(str(mst_mx).replace('[', '').replace(']', '').replace('.', ','))
        if is_tree(mst_mx):
            continue
        else:
            mst_mx[nodeA][nodeB] = 0
            mst_mx[nodeB][nodeA] = 0
            num_edges -= 1


data = read_file("MST_mx1.txt")
find_MST(data)
