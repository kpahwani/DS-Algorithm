# Find the Minimum length Unsorted Subarray, 
# sorting which makes the complete array sorted

import numpy as np

def min_unsorted_subarry(arr):
    n = len(arr)
    start = 0
    end = n-1
    while arr[start]<arr[start+1] and start<end:
        start+=1

    while arr[end]>arr[end-1] and end>start:
        end-=1

    min_val = min(arr[start:end+1])
    max_val = max(arr[start:end+1])

    for i in range(start):
        if arr[i] > min_val:
            start = i
            break

    
    for i in range(n-1, end, -1):
        if arr[i] < max_val:
            end = i
            break

    return start,end


if __name__ == "__main__":
    arr = list(np.random.randint(1,100, 10))
    # arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    start, end = min_unsorted_subarry(arr)
    print(f"To sort the array: {arr}, sort subarry from index {start} to {end}")
