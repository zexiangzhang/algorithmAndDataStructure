# Kruskal O(nlogn)
# use Arc Array
# 重点是排好序的边集数组，依次循环
# 判断新的边是否会形成环路, 形成环路就不需要 TODO Think this find function

from arc_array import ArcArray, Vertex, Arc


def find_arc(link_arcs, key):
    while link_arcs[key] > 0:
        key = link_arcs[key]
    return key


def mini_span_tree_kruskal(graph):
    number = graph.get_number()
    link_arcs = [0] * number
    arc_number = graph.get_arc_number()

    for i in range(arc_number):
        arc = graph.get_arc(i)
        n = find_arc(link_arcs, arc.tail)
        m = find_arc(link_arcs, arc.head)

        if n != m:
            link_arcs[n] = m
            print(link_arcs)
            print(graph.get_vertex(arc.tail).value,
                  '-->', graph.get_vertex(arc.head).value)


if __name__ == '__main__':
    vertex = Vertex()
    vertex.create_and_add_vertex('A')
    vertex.create_and_add_vertex('B')
    vertex.create_and_add_vertex('C')
    vertex.create_and_add_vertex('D')
    vertex.create_and_add_vertex('E')
    vertex.create_and_add_vertex('F')
    vertex.create_and_add_vertex('G')
    vertex.create_and_add_vertex('H')
    vertex.create_and_add_vertex('I')
    test = ArcArray(vertex)

    # 关键点　按照权重排序
    test.create_and_add_arc(4, 7, 7)
    test.create_and_add_arc(2, 8, 8)
    test.create_and_add_arc(0, 1, 10)
    test.create_and_add_arc(0, 5, 11)
    test.create_and_add_arc(1, 8, 12)
    test.create_and_add_arc(1, 6, 16)
    test.create_and_add_arc(3, 7, 16)
    test.create_and_add_arc(5, 6, 17)
    test.create_and_add_arc(1, 2, 18)
    test.create_and_add_arc(6, 7, 19)
    test.create_and_add_arc(3, 4, 20)
    test.create_and_add_arc(3, 8, 21)
    test.create_and_add_arc(2, 3, 22)
    test.create_and_add_arc(3, 6, 24)
    test.create_and_add_arc(4, 5, 26)

    mini_span_tree_kruskal(test)
