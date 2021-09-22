from Trees.binary_tree import BinaryTree


head = None


def transform_btree_to_dll(root):
    global head
    if not root:
        return

    transform_btree_to_dll(root.right)
    root.right = head
    if head:
        head.left = root
    head = root
    transform_btree_to_dll(root.left)


def print_dll(head):
    temp = head
    while temp:
        print(temp.key, end=" ")
        temp = temp.right
    print("")


if __name__ == "__main__":
    b_tree = BinaryTree(10)
    b_tree.add_left(b_tree.root, 12)
    b_tree.add_right(b_tree.root, 15)
    b_tree.add_left(b_tree.root.left, 25)
    b_tree.add_right(b_tree.root.left, 30)
    b_tree.add_left(b_tree.root.right, 36)
    transform_btree_to_dll(b_tree.root)
    print_dll(head)
