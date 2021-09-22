from data_structures.linked_list import Linked_List
from random import randint

def partition_list(head):
    a = head
    b = head
    while b

    return a, b

def merge_sorted_ll(a, b):
    pass

def merge_sort_ll(head):
    if not head:
        return
    a, b = partition_list(head)
    merge_sort_ll(a)
    merge_sort_ll(b)
    merge_sorted_ll(a, b)

if __name__ == "__main__":
    ll = Linked_List()
    for i in range(5):
        ll.insert(randint(1,50))
    merge_sort_ll(ll.head)