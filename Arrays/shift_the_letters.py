# Problem : https://www.hackerearth.com/challenge/competitive/january-circuits-19/algorithm/shift-the-array-4074fac2/


def cal_distance(a, b):
    if a - b <= 0:
        return abs(a-b)
    return 26 - (a-b)


arr = list(input())
k = input()
n = len(arr)
dist_arr = [cal_distance(ord(arr[i])-97,  (ord(arr[i+1])-97)) for i in range(n-1)]

print (dist_arr)
# TO DO