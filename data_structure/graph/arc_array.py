# arc Array 边集数组
class ArcNode:
    def __init__(self, weight,  tail, head):
        self.weight = weight
        self.tail = tail
        self.head = head


class Arc:
    store = []

    def __init__(self, *arc_nodes):
        self.store = list(arc_nodes)

    def add_arc(self, arc_node):
        self.store.append(arc_node)

    def create_and_add_arc(self, k1, k2, weight):
        arc = ArcNode(weight, k1, k2)
        self.store.append(arc)

    def get_arc(self, key):
        return self.store[key]

    def get_number(self):
        return len(self.store)


class VertexNode:
    def __init__(self, value):
        self.value = value


class Vertex:
    store = []

    def __init__(self, *vertex_nodes):
        self.store = list(vertex_nodes)

    def add_vertex(self, vertex_node):
        self.store.append(vertex_node)

    def create_and_add_vertex(self, value):
        vertex_node = VertexNode(value)
        self.store.append(vertex_node)

    def get_vertex(self, key):
        return self.store[key]

    def get_number(self):
        return len(self.store)


class ArcArray:
    def __init__(self, vertex=Vertex(), arc=Arc()):
        self.vertex = vertex
        self.arc = arc

    def create_and_add_arc(self, k1, k2, weight):
        self.arc.create_and_add_arc(k1, k2, weight)

    def create_and_add_vertex(self, value):
        self.vertex.create_and_add_vertex(value)

    def get_vertex(self, key):
        return self.vertex.get_vertex(key)

    def get_arc(self, key):
        return self.arc.get_arc(key)

    def get_vertex_arcs(self, key):
        arcs = []
        for arc in self.arc:
            if arc.tail == key or arc.head == key:
                arcs.append(arc)

        return arcs

    def get_number(self):
        return self.vertex.get_number()

    def get_arc_number(self):
        return self.arc.get_number()
