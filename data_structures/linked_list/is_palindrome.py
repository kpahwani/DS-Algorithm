
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function should return true/false or 1/0


class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


def push(arr, val):
    arr.append(val)


def pop(arr):
    return arr.pop(-1)


def isEmpty(arr):
    return True if not len(arr) else False


def isPalindrome(head):
    if not head:
        return True

    stack = []
    temp = head
    while (temp):
        push(stack, temp.data)
        temp = temp.next

    temp = head
    while stack:
        if temp.data != pop(stack):
            break
        temp = temp.next

    if stack:
        return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        if isPalindrome(head):
            print(1)
        else:
            print(0)
