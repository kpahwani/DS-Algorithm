from Trees.binary_tree import BinaryTree


def get_vertical_order(root, hd, mapping):
    if not root:
        return

    if hd not in mapping:
        mapping[hd] = []

    mapping[hd].append(root.key)
    get_vertical_order(root.left, hd-1, mapping)
    get_vertical_order(root.right, hd+1, mapping)
    

def print_vertical_order(mapping):
    for key in sorted(mapping.iterkeys()):
        for val in mapping[key]:
            print(val),
        print

mapping = {}

tree = BinaryTree(1)
tree.add_left(tree.root, 2)
tree.add_right(tree.root, 3)
tree.add_left(tree.root.left, 4)
tree.add_right(tree.root.right, 5)

get_vertical_order(tree.root, hd=0, mapping=mapping)
print_vertical_order(mapping)
