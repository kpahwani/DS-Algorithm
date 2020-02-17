class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.data, end=' ')
            self.traverse(root.right)


# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree


def traverse_level_order(root):
    queue = []
    if root:
        queue.append(root)
        while len(queue) != 0:
            element = queue.pop(0)
            print(element.data, end=" ")
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = {}
        root = None
        root = tree.createNode(int(arr[0]))
        lis[root.data] = root
        k = 0
        for j in range(n):
            if int(arr[k]) in lis:
                ptr = tree.createNode(int(arr[k + 1]))
                if arr[k + 2] == 'L':
                    lis[int(arr[k])].left = ptr
                else:
                    lis[int(arr[k])].right = ptr
                lis[int(arr[k + 1])] = ptr
                k += 3
        traverse_level_order(root)
        print()

