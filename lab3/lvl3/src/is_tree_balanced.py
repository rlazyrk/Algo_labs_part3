class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def node_height(node: BinaryTree) -> int:
    if not node:
        return 0

    left_child_height = node_height(node.left)
    right_child_height = node_height(node.right)

    if left_child_height == -1:
        return -1

    if right_child_height == -1:
        return -1

    if abs(left_child_height - right_child_height) > 1:
        return -1
    else:
        return max(left_child_height, right_child_height) + 1


def is_tree_balanced(node: BinaryTree) -> bool:
    return node_height(node) != -1
