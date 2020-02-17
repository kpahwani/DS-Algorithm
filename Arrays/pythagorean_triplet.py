def pair_sum(arr, k):
    l = 0
    r = len(arr) - 1
    while l < r:
        sum = arr[l] + arr[r]
        if sum == k:
            return True
        if sum < k:
            l += 1
        else:
            r -= 1
    return False


def pythagorean_triplet(arr):
    arr = [i*i for i in arr]
    arr.sort()
    for i in range(n-1, 1, -1):
        if pair_sum(arr[:i], arr[i]):
            return True
    return False


# driver function
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        inp_arr = map(int, input().split())
        if pythagorean_triplet(inp_arr):
            print("Yes")
        else:
            print("No")
        t -= 1
