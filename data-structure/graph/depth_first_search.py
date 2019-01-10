# depth first search
# adjacency matrix
from adjacency_matrix import AdjacencyMatrix


def depth_first_search(graph, i):
    global vertex_visited
    vertex_visited[i] = True
    print(graph.get_vertex_value(i))

    for j in range(graph.get_number()):
        if graph.has_arc(i, j) and not vertex_visited[j]:
            depth_first_search(graph, j)


def depth_first_search_traverse(graph):
    global vertex_visited
    for i in range(graph.get_number()):
        if not vertex_visited[i]:
            depth_first_search(graph, i)


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

vertex_visited = [False] * test.get_number()
depth_first_search_traverse(test)

print('=====================')
# adjacency list
from adjacency_list import AdjacencyList, VertexNode


def depth_first_search_list(graph, i):
    global vertex_visited_list
    vertex_visited_list[i] = True
    current_vertex = graph.get_vertex_value(i)
    print(current_vertex.value)
    first_arc = current_vertex.first_arc

    while first_arc:
        to_vertex = first_arc.to_vertex
        j = graph.get_vertex_key(to_vertex)

        if not vertex_visited_list[j]:
            depth_first_search_list(graph, j)
        first_arc = first_arc.next_arc


def depth_first_search_traverse_list(graph):
    global vertex_visited_list
    for i in range(graph.get_number()):
        if not vertex_visited_list[i]:
            depth_first_search_list(graph, i)


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
depth_first_search_traverse_list(test_list)
