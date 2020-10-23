# Orthogonal List 十字链表 针对有向图
# vertetNode: data, first_in, first_out
# arcNode:    weight, tail_vertet, head_vertet, head_link, tail_link


class VertexNode:
    def __init__(self, value, first_in=None, first_out=None):
        self.value = value
        self.first_in = first_in
        self.first_out = first_out


class ArcNode:
    def __init__(self, weight, tail_vertex=None, head_vertex=None, head_link=None, tail_link=None):
        self.weight = weight
        self.tail_vertex = tail_vertex  # out's point
        self.head_vertex = head_vertex  # in's point
        self.head_link = head_link   # in's next's(arc) point
        self.taik_link = tail_link   # out's next's (arc) point
