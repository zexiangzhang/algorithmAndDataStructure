class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(tree: TreeNode):
    if not tree:
        return []
    result_list = []
    cur_layer = [tree]
    count = 0
    while cur_layer:
        cur_list = []
        next_layer = []
        for node in cur_layer:
            cur_list.append(node.val)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        if count // 2 == 0:
            cur_list.reverse()
        result_list.append(cur_list)
        cur_layer = next_layer
    print(result_list)