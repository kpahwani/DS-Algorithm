# Subset Sum Problem


def recursive_implementation(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if sum < arr[n-1]:
        return recursive_implementation(arr, n-1, sum)
    return recursive_implementation(arr, n-1, sum) or recursive_implementation(arr, n-1, sum - arr[n-1])


def dp_implementation(arr, n, sum):
    dp = [[False]*(sum+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][0] = True




arr = map(int, input("Enter array:").split())
sum = input("Enter sum: ")
print(recursive_implementation(arr, len(arr), sum))
print(dp_implementation(arr, len(arr), sum))
