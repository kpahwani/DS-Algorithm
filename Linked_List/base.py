class DoublyNode:
    def __init__(self, data=None, back=None, fwd=None):
        self.data = data
        self.fwd = fwd
        self.back = back


class DoublyLinkList:
    def __init__(self):
        self.head = None

    def add(self, elm):
        if self.head:
            temp = self.head
            while temp.fwd:
                temp = temp.fwd
            node = DoublyNode(elm, temp, None)
            temp.fwd = node
        else:
            self.head = DoublyNode(elm, None, None)

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.fwd
        print("")





