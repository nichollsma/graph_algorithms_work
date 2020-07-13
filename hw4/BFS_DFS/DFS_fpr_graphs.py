import numpy as np


adj_mx = np.loadtxt("input_graph3.txt", delimiter=',')

visited = []
root = 0

tree_mx = np.zeros([len(adj_mx), len(adj_mx)])


def dfs_rec(start):
    visited.append(start)
    for i in range(len(adj_mx)):
        if adj_mx[start][i] == 1:
            if not visited.__contains__(i):
                print(start, '->', i)
                tree_mx[start][i] = 1
                tree_mx[i][start] = 1
                dfs_rec(i)


dfs_rec(root)

print(str(tree_mx).replace('[', '').replace(']', '').replace('.', ','))
