import numpy as np


# backtracking part
adj_mx = np.loadtxt("input_graph3.txt", delimiter=',')

backtracking_table = np.full([len(adj_mx), len(adj_mx)], -1)

for r in range(len(adj_mx) - 1):
    for i in range(len(adj_mx)):
        for j in range(len(adj_mx)):
            if i == j:
                continue

            for k in range(len(adj_mx)):
                if adj_mx[i][k] > 0 and adj_mx[k][j] > 0:
                    path_i_k_j = adj_mx[i][k] + adj_mx[k][j]

                    if adj_mx[i][j] == 0:
                        adj_mx[i][j] = path_i_k_j
                        backtracking_table[i][j] = k

                    elif path_i_k_j < adj_mx[i][j]:
                        adj_mx[i][j] = path_i_k_j
                        backtracking_table[i][j] = k


def backtracking_func(bk_table, start, end):
    k_tmp = bk_table[start][end]

    if k_tmp == -1:
        print(start, '-', end)
        return [start, end]

    part1_arr = backtracking_func(bk_table, start, k_tmp)
    part2_arr = backtracking_func(bk_table, k_tmp, end)

    arr = part1_arr + part2_arr
    return arr


tree_adjmx = np.zeros([len(adj_mx), len(adj_mx)])

root = 0
for j in range(len(adj_mx)):
    path_arr = backtracking_func(backtracking_table, root, j)

    for k in range(len(path_arr) - 1):
        if path_arr[k] != path_arr[k + 1]:
            tree_adjmx[path_arr[k]][path_arr[k + 1]] = 1
            tree_adjmx[path_arr[k + 1]][path_arr[k]] = 1

print(str(tree_adjmx).replace('[', '').replace(']', '').replace('.', ','))
