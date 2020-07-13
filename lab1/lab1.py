import numpy as np
import random


def is_connected(adj_mx):
    starting_points = [0]
    visited = []
    while len(starting_points) > 0:
        start = starting_points.pop()
        visited.append(start)
        for i in range(len(adj_mx[start])):
            if adj_mx[start][i] == 1:
                if not visited.__contains__(i) and not starting_points.__contains__(i):
                    starting_points.append(i)

    number_of_nodes = len(adj_mx)
    if len(visited) == number_of_nodes:
        return True
    else:
        return False


def is_eulerian(adj_mx):
    for i in range(len(adj_mx)):
        if sum(adj_mx[i]) % 2 != 0:
            return False

    return True


def eularian_gen(n, min_edges):
    mx = np.zeros([n, n])

    found = False
    while not found:
        mx = np.zeros([n, n])
        for edge_count in range(int(n * (n - 1)/2)):
            row = random.randint(0, n-1)
            col = random.randint(0, n-1)

            if row != col:
                mx[row][col] = 1
                mx[col][row] = 1

            if edge_count >= min_edges and is_connected(mx) and is_eulerian(mx):
                print(str(mx).replace('[', '').replace(']', '').replace('.', ','))
                found = True
                break


# eularian_gen(12, 6)
data = np.loadtxt("mx.txt", delimiter=",")
if is_connected(data):
    print("True")
else:
    print("False")