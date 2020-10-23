# base common tree
class BaseTree:
    def __init__(self):
        pass

    def destory(self):
        pass

    def create(self, definition):
        pass

    def clear(self):
        pass

    def isEmpty(self):
        pass

    def depth(self):
        pass

    def root(self):
        pass

    # 返回结点n的值
    def value(self, n):
        pass

    # 给结点n赋值
    def assign(self, n, value):
        pass

    def parent(self, n):
        pass

    def left_child(self, n):
        pass

    def right_sibling(self, n):
        pass

    # 在n结点的i子树位置插入c树
    def insert_child(self, n, i, c):
        pass

    # 删除n结点的第i位置的子树
    def delete_child(self, n, i):
        pass

# parent表示法


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

# parent 与 长子表示法


class PFCNode:
    def __init__(self, value, parent, first_child):
        self.value = value
        self.parent = parent
        self.first_child = first_child

# parent first_child right_sibling


class PFCRSNode:
    def __init__(self, value, parent, first_child, right_sibling):
        self.value = value
        self.parent = parent
        self.first_child_first_child
        self.right_sibling = right_sibling

# 连续空间


class ParentTree(BaseTree):
    store = []
    root = Node()
    n = 0  # 结点个数

    def __init__(self, root, n):
        self.root = root
        self.store.append(root)
        self.n = n


# child表示法 多重链表表示法
# 1. 用树的degree作为每个结点默认的子个数
DEGREE = 5


class ChildNode1:
    store = [None for i in range(DEGREE)]

    def __init__(self, value, *args):
        self.value = value
        self.store = list(args)

# 2. 用每个结点的度作为子个数


class ChildNode2:
    def __init__(self, value, degree, *args):
        self.value = value
        self.degree = degree
        self.store = [args[v] for i in range(degree)]


class ChildNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SingleChildNode:
    def __init__(self, value, first_child):
        self.value = value
        self.first_child = first_child

# 改进之后的child_parent表示法, child表示法的升级


class SingleParentChildNode:
    def __init__(self, value, parent, first_child):
        self.value = value
        self.parent = parent
        self.first_child = first_child


class ChildTree:
    store = []

    def __init__(self, n):
        self.store = [SingleParentChildNode() for _ in range(n)]


# child_sibling表示法 (二叉树)
class ChildSiblingNode:
    def __init__(self, value, first_child, right_sibling):
        self.value = value
        self.first_child = first_child
        self.right_sibling = right_sibling

# child_sibling_parnet


class ParentChildSiblingNode:
    def __init__(self, value, parent, first_child, right_sibling):
        self.value = value
        self.parent = parent
        self.first_child = first_child
        self.right_sibling = right_sibling
