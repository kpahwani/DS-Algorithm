class Node:
    def __init__(self, value=None):
        self.key = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    @staticmethod
    def add_left(node, value):
        node.left = Node(value)

    @staticmethod
    def add_right(node, value):
        node.right = Node(value)

    @staticmethod
    def inorder_traversal(root):
        if not root:
            return
        BinaryTree.inorder_traversal(root.left)
        print(root.key)
        BinaryTree.inorder_traversal(root.right)

