import numpy as np


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

    number_of_nodes = len(adj_mx)
    if len(visited) == number_of_nodes:
        print("This graph is a tree.")
        return True
    else:
        print("This graph is NOT a tree.")
        return False


def read_file(filename):
    data = np.loadtxt(filename, delimiter=",")
    return data


mx = read_file("tree_adj_mx1.txt")
is_tree(mx)
