MOD = 1000000007
n = input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())

a.sort()
b.sort()

result = 0
for i in range(n):
    result += abs(a[i] - b[i])
    result %= MOD

print result
