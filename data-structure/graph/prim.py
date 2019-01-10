# depth first search
# adjacency matrix
# 选取第一个点之后，讲第一个点的边中选出最近的, 产生第二个点
# 从第一个点和第二个点中的边上选出下一个最近的点, 产生第三个点
# 从第一个点, 第二个点, 第三个点的边中选出下一个最近的点, 产生第四个点
# 以此类推到最后一个点 TODO Think this lowcast variable
# O(n^2)

from adjacency_matrix import AdjacencyMatrix


def mini_span_tree_prim(graph):
    MAX = 1000  # max weight

    number = graph.get_number()
    adjvex = [0] * number
    lowcast = [0] * number

    for i in range(1, number):
        lowcast[i] = graph.get_arc(0, i, MAX)

    for i in range(1, number):
        min = MAX
        j, k = 1, 0

        while j < number:
            if lowcast[j] != 0 and lowcast[j] < min:
                min = lowcast[j]
                k = j
            j += 1

        print(adjvex[k], k)
        lowcast[k] = 0
        for j in range(1, number):
            if lowcast[j] != 0 and graph.get_arc(k, j, MAX) < lowcast[j]:
                lowcast[j] = graph.get_arc(k, j, MAX)
                adjvex[j] = k


test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
test.insert_arc('A', 'B', 10)
test.insert_arc('A', 'F', 11)
test.insert_arc('B', 'G', 16)
test.insert_arc('F', 'G', 17)
test.insert_arc('E', 'F', 26)
test.insert_arc('E', 'H', 7)
test.insert_arc('D', 'E', 20)
test.insert_arc('D', 'H', 16)
test.insert_arc('G', 'H', 19)
test.insert_arc('D', 'G', 24)
test.insert_arc('D', 'I', 21)
test.insert_arc('C', 'D', 22)
test.insert_arc('C', 'I', 8)
test.insert_arc('B', 'C', 18)
test.insert_arc('B', 'I', 12)

mini_span_tree_prim(test)
