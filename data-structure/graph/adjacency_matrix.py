# Adjacency Matrix
# two array, one is vertexs(one dimension), one is arc(two dimension)
# arc[i][j] = 1 or 0
#             A  B  C  D
#          A  0  1  0  1
#          B  1  0  1  0
#          C  0  1  0  1
#          D  1  0  1  0


class AdjacencyMatrix:
    directed = False  # is or not directed
    vertex = []
    arc = []

    def __init__(self, directed, *args):
        self.directed = directed
        number = len(args)
        self.vertex = list(args)
        self.arc = [[None for _ in range(number)] for _ in range(number)]

    def insert_arc(self, v1, v2, weight):
        index1 = self.vertex.index(v1)
        index2 = self.vertex.index(v2)
        self.arc[index1][index2] = weight

        if not self.directed:
            self.arc[index2][index1] = weight

    def has_arc(self, k1, k2):
        return bool(self.arc[k1][k2])

    def get_arc(self, k1, k2, default=0):
        return self.arc[k1][k2] if self.arc[k1][k2] else default

    def get_number(self):
        return len(self.vertex)

    def get_vertex_value(self, key):
        return self.vertex[key]

    def get_vertex_key(self, v):
        for key, value in enumerate(self.vertex):
            if value == v:
                return key

    def get_vertex_outdegrees(self, key):
        return self.arc[key]

    def __repr__(self):
        number = len(self.vertex)
        for index1 in range(number):
            for index2 in range(number):
                print(self.vertex[index1], ' -> ',
                      self.vertex[index2], ' : ', self.arc[index1][index2])
        return "\n"


if __name__ == '__main__':
    test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D')
    test.insert_arc('A', 'B', 1)
    test.insert_arc('A', 'C', 2)
    test.insert_arc('C', 'B', 3)
    test.insert_arc('D', 'B', 4)
    print(test)

    test2 = AdjacencyMatrix(True, 'A', 'B', 'C', 'D')
    test2.insert_arc('A', 'B', 1)
    test2.insert_arc('A', 'C', 2)
    test2.insert_arc('C', 'B', 3)
    test2.insert_arc('D', 'B', 4)
    print(test2)
