from collections import deque


def max_of_all_subarray(arr, k):
    q = deque()

    for i in range(k):
        while len(q) > 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, n):
        print(str(arr[q[0]]), end=" ")

        while len(q) > 0 and q[0] <= i-k:
            q.popleft()

        while len(q) > 0 and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    print(arr[q[0]])


# driver function
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        arr = [int(i) for i in input().split()]
        max_of_all_subarray(arr, k)
        t -= 1
