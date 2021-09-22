import sys


# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)


# Function should pop an element from stack
def pop(arr):
    return arr.pop()


# function should return 1/0 or True/False
def isFull(n, arr):
    return True if len(arr) == n else False


# function should return 1/0 or True/False
def isEmpty(arr):
    return True if len(arr) == 0 else False


# function should return 1/0 or True/False
def top_of_stack(arr):
    if not isEmpty(arr):
        return arr[-1]
    return None


# function should return minimum element from the stack
def getMin(n, arr):
    min_val = sys.maxsize
    while not isEmpty(arr):
        min_val = min(pop(arr), min_val)
    return min_val


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
