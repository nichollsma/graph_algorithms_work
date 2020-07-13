import numpy as np

adj_mx = np.loadtxt("", delimiter=',')
print(adj_mx)

for r in range(len(adj_mx) - 1):
    for i in range(len(adj_mx)):
        for j in range(len(adj_mx)):
            if i == j:
                continue

            for k in range(len(adj_mx)):
                if adj_mx[i][k] > 0 and adj_mx[k][j] > 0:
                    path_i_j_k = adj_mx[i][k] + adj_mx[k][j]

                    if adj_mx[i][j] == 0:
                        adj_mx[i][j] = path_i_j_k

                    elif path_i_j_k < adj_mx[i][j]:
                        adj_mx[i][j] = path_i_j_k

print('------------')
print(adj_mx)


# backtracking part
adj_mx = np.loadtxt("", delimiter=',')

backtracking_table = np.full([len(adj_mx), len(adj_mx)], -1)

for r in range(len(adj_mx) - 1):
    for i in range(len(adj_mx)):
        for j in range(len(adj_mx)):
            if i == j:
                continue

            for k in range(len(adj_mx)):
                if adj_mx[i][k] > 0 and adj_mx[k][j] > 0:
                    path_i_j_k = adj_mx[i][k] + adj_mx[k][j]

                    if adj_mx[i][j] == 0:
                        adj_mx[i][j] = path_i_j_k
                        backtracking_table[i][j] = k

                    elif path_i_j_k < adj_mx[i][j]:
                        adj_mx[i][j] = path_i_j_k
                        backtracking_table[i][j] = k

print('------------')
print(backtracking_table)


def backtracking_func(bk_table, start, end):
    k_tmp = bk_table[start][end]

    if k_tmp == -1:
        print(start, '-', end)
        return

    backtracking_func(bk_table, start, k_tmp)
    backtracking_func(bk_table, k_tmp, end)


backtracking_func(backtracking_table, 1, 3)
print('------------')
backtracking_func(backtracking_table, 0, 3)
print('------------')
backtracking_func(backtracking_table, 2, 3)
print('------------')
backtracking_func(backtracking_table, 1, 5)
