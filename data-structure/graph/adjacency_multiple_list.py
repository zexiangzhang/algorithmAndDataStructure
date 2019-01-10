# Adjacency Multiple List 邻接多重表 针对无向图
class VertexNode:
    def __init__(self, value, first_edge=None):
        self.value = value
        self.first_edge = value


class EdgeNode:
    def __init__(self, weight, ivex=None, ilink=None, jvex=None, jlink=None):
        self.weight = weight
        self.ivex = ivex
        self.ilink = ilink
        self.jvex = jvex
        self.jlink = jlink
