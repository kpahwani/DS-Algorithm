# A contiguous subarray is defined as unique if all the integers contained within it occur exactly once.
# There is a unique weight associated with each of the subarray. Unique weight for any subarray equals it's length
# if it's unique, 0 otherwise. Your task is to calculate the sum of unique weights of all the contiguous subarrays
# contained within a given array.

t = input()
while t:
    n = input()
    arr = map(int, raw_input().split())
    s = set()
    result = 0
    for i in range(n):
        while arr[i] not in s and i < n:
            s.add(arr[i])
            i += 1
        # result +=
        pass
    t -= 1
# TO DO