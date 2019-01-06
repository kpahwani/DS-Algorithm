class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    @staticmethod
    def add_left( node, value):
        node.left = Node(value)

    @staticmethod
    def add_right(node, value):
        node.right = Node(value)
