# 二叉链表
class TwoBinaryNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def set_data(self, value):
        self.data = value

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

# 三叉链表


class ThreeBinaryNode:
    def __init__(self, data, left_child, right_child, parent):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent


# 遍历二叉树
# init
a_node = TwoBinaryNode('A')
b_node = TwoBinaryNode('B')
c_node = TwoBinaryNode('C')
d_node = TwoBinaryNode('D')
e_node = TwoBinaryNode('E')
f_node = TwoBinaryNode('F')
g_node = TwoBinaryNode('G')
h_node = TwoBinaryNode('H')
i_node = TwoBinaryNode('I')
a_node.set_left_child(b_node)
a_node.set_right_child(c_node)
b_node.set_left_child(d_node)
c_node.set_left_child(e_node)
c_node.set_right_child(f_node)
d_node.set_left_child(g_node)
d_node.set_right_child(h_node)
e_node.set_right_child(i_node)

# 前序遍历


def pre_order_traverse(tree):
    if not tree:
        return
    print(tree.data)
    pre_order_traverse(tree.left_child)
    pre_order_traverse(tree.right_child)


pre_order_traverse(a_node)
print('--------')

# 中序遍历


def in_order_traverse(tree):
    if not tree:
        return
    in_order_traverse(tree.left_child)
    print(tree.data)
    in_order_traverse(tree.right_child)


in_order_traverse(a_node)
print('--------')

# 后序遍历


def post_order_traverse(tree):
    if not tree:
        return
    post_order_traverse(tree.left_child)
    post_order_traverse(tree.right_child)
    print(tree.data)


post_order_traverse(a_node)

# 由中序遍历和前后遍历中的任一种，可以唯一确定一个树结构。
# 由前后遍历，无法确定一个树结构。
print('===================')

# 建立二叉树（通过满二叉树）

class StringList:
    def __init__(self, string):
        self.string_list = list(string)
        self.string_list.reverse()

    def pop(self):
        return self.string_list.pop()

    def isEmpty(self):
        return not len(self.string_list)


def create_tree_by_pre_order(string_list):
    if string_list.isEmpty():
        return
    data = string_list.pop()

    if data == '*':
        return None

    node = TwoBinaryNode(data)
    node.set_left_child(create_tree_by_pre_order(string_list))
    node.set_right_child(create_tree_by_pre_order(string_list))

    return node


string_list = StringList('ABDGH***CE*IF**')

test_tree = create_tree_by_pre_order(string_list)
pre_order_traverse(test_tree)

# 线索二叉树 == 双向链表二叉树 便于经常遍历和查找结点
class ThreadedBinaryTreeNode:
    def __init__(self, data, left_child=None, left_tag=True, right_child=None, right_tag=True):
        self.data = data
        self.left_child = left_child
        self.left_tag = left_tag
        self.right_child = right_child
        self.right_tag = right_tag


# 中序线索化二叉树
pre = None  # 最新访问的结点

def in_threading(tree):
    global pre
    if tree:
        in_threading(tree.left_child)

        if not tree.left_child:
            tree.left_tag = False
            tree.left_child = pre

        if not pre.right_child:
            pre.right_tag = False
            pre.right_child = tree

        pre = tree

        in_threading(tree.right_child)
