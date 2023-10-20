import unittest

from lab3.lvl3.src.is_tree_balanced import is_tree_balanced
from lab3.lvl3.src.is_tree_balanced import BinaryTree


class TestIsTreeBalanced(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(is_tree_balanced(None), True)

    def test_balanced_tree(self):
        root = BinaryTree(25)
        root.left = BinaryTree(20)
        root.left.left = BinaryTree(15)
        root.left.right = BinaryTree(17)
        root.right = BinaryTree(40)
        root.right.left = BinaryTree(30)
        root.right.right = BinaryTree(45)
        self.assertEqual(is_tree_balanced(root), True)

    def test_unbalanced_tree(self):
        root = BinaryTree(25)
        root.left = BinaryTree(10)
        root.left.left = BinaryTree(5)
        root.right = BinaryTree(40)
        root.left.left.left = BinaryTree(1)
        self.assertEqual(is_tree_balanced(root), False)

    def test_worth_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(10)
        root.left.left = BinaryTree(25)
        root.left.left.left = BinaryTree(30)
        root.left.left.left.left = BinaryTree(40)
        root.right = BinaryTree(100)
        root.right.right = BinaryTree(1000)
        root.right.right.right = BinaryTree(10000)
        root.right.right.right.right = BinaryTree(100000)
        self.assertEqual(is_tree_balanced(root), False)


if __name__ == '__main__':
    unittest.main()
