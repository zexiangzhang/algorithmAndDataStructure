# Diejkstra 迪杰斯特拉 最短路径算法 O(n^2)
# 要求到该点的最短路径，　通过求到改点相连点的最短路径,　也就是之前点的最短路径


def mini_path_dijkstra(graph):
    number = graph.get_number()

    # init
    short_vertexs = [0] * number
    short_path_weight = [0] * number
    final = [0] * number  # final[x] store Vo ~ Vx short path
    final[0] = 1

    for i in range(1, number):
        short_path_weight[i] = graph.get_arc(
            0, i, 255)  # set 255 as max weight

    for i in range(1, number):
        min = 100  # set max weight

        # if has link between i, j
        for j in range(1, number):
            if not final[j] and short_path_weight[j] < min:
                k = j
                min = short_path_weight[j]

        final[k] = 1  # get short path set 1
        print(final)

        # if not has link between i, j or has short one
        for j in range(1, number):
            if not final[j] and min + \
                    graph.get_arc(k, j, 255) < short_path_weight[j]:
                short_path_weight[j] = min + graph.get_arc(k, j)
                short_vertexs[j] = k

    print(short_vertexs)
    print(short_path_weight)


if __name__ == '__main__':
    from adjacency_matrix import AdjacencyMatrix
    test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
    test.insert_arc('A', 'B', 1)
    test.insert_arc('A', 'C', 5)
    test.insert_arc('B', 'C', 3)
    test.insert_arc('B', 'D', 7)
    test.insert_arc('B', 'E', 5)
    test.insert_arc('C', 'E', 1)
    test.insert_arc('C', 'F', 7)
    test.insert_arc('D', 'G', 3)
    test.insert_arc('D', 'E', 2)
    test.insert_arc('E', 'F', 3)
    test.insert_arc('E', 'G', 6)
    test.insert_arc('E', 'H', 9)
    test.insert_arc('F', 'H', 5)
    test.insert_arc('G', 'H', 2)
    test.insert_arc('G', 'I', 7)
    test.insert_arc('H', 'I', 4)

    mini_path_dijkstra(test)
