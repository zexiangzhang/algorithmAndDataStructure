# breadth_first_search
# use standard lib queue
from queue import Queue

from adjacency_matrix import AdjacencyMatrix


def breadth_first_search_traverse(graph):
    number = graph.get_number()
    vertex_visited = [False] * number
    q = Queue()
    for i in range(number):  # foreach only for Directed Graph or not Connected Graph
        if not vertex_visited[i]:
            q.put(i)
            vertex_visited[i] = True

            while (not q.empty()):
                key = q.get()
                print(graph.vertex[key])
                vertex_keys = graph.get_vertex_outdegrees(key)
                for j, value in enumerate(vertex_keys):
                    if value and not vertex_visited[j]:
                        vertex_visited[j] = True
                        q.put(j)


test = AdjacencyMatrix(False, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
test.insert_arc('A', 'B', 1)
test.insert_arc('A', 'F', 1)
test.insert_arc('B', 'G', 1)
test.insert_arc('F', 'G', 1)
test.insert_arc('E', 'F', 1)
test.insert_arc('E', 'H', 1)
test.insert_arc('D', 'E', 1)
test.insert_arc('D', 'H', 1)
test.insert_arc('G', 'H', 1)
test.insert_arc('D', 'G', 1)
test.insert_arc('D', 'I', 1)
test.insert_arc('C', 'D', 1)
test.insert_arc('C', 'I', 1)
test.insert_arc('B', 'C', 1)
test.insert_arc('B', 'I', 1)

breadth_first_search_traverse(test)

print('=====================')

# adjacency list
from adjacency_list import AdjacencyList, VertexNode


def breadth_first_search_traverse_list(graph):
    number = graph.get_number()
    vertex_visited = [False] * number
    q = Queue()
    for i in range(number):  # foreach only for Directed Graph or not Connected Graph
        if not vertex_visited[i]:
            q.put(i)
            vertex_visited[i] = True

            while (not q.empty()):
                key = q.get()
                v = graph.vertex[key]
                print(v)
                tmp_arc = v.first_arc
                while tmp_arc:
                    j = graph.get_vertex_key(tmp_arc.to_vertex)
                    if not vertex_visited[j]:
                        vertex_visited[j] = True
                        q.put(j)
                    tmp_arc = tmp_arc.next_arc


a = VertexNode('A')
b = VertexNode('B')
c = VertexNode('C')
d = VertexNode('D')
e = VertexNode('E')
f = VertexNode('F')
g = VertexNode('G')
h = VertexNode('H')
i = VertexNode('I')

test_list = AdjacencyList(False, a, b, c, d, e, f, g, h, i)
test_list.add_arc(a, b, 1)
test_list.add_arc(a, f, 1)
test_list.add_arc(b, g, 1)
test_list.add_arc(f, g, 1)
test_list.add_arc(e, f, 1)
test_list.add_arc(e, h, 1)
test_list.add_arc(d, e, 1)
test_list.add_arc(d, h, 1)
test_list.add_arc(g, h, 1)
test_list.add_arc(d, g, 1)
test_list.add_arc(d, i, 1)
test_list.add_arc(c, d, 1)
test_list.add_arc(c, i, 1)
test_list.add_arc(b, c, 1)
test_list.add_arc(b, i, 1)

vertex_visited_list = [False] * test_list.get_number()
breadth_first_search_traverse_list(test_list)
