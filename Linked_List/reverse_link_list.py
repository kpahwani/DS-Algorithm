class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            # arr.append(str(temp.data))
            temp = temp.next
        print()


def reverse(head, k):
    curr = head
    start_end = []

    prev = None
    while curr:
        temp_k = k
        val = dict(
            start=None,
            end=None
        )
        val['end'] = curr
        while temp_k and curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            temp_k -= 1
        val['start'] = prev
        start_end.append(val)

    for i in range(len(start_end)-1):
        start_end[i]['end'].next = start_end[i+1]['start']
    if len(start_end)-1:
        start_end[i + 1]['end'].next = None

    return start_end[0]['start']


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
