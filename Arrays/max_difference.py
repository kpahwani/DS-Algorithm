'''
    Raman loves Mathematics a lot. One day his maths teacher gave him an interesting problem.

    He was given an array 'A' consisting of 'n' integers, he was needed to find the maximum value of the following expression:

    |Ai - Aj| + |i - j|
    where, 0<= i,j <n and Ai, Aj are the Array elements.
'''

t = input()
while t:
    n = input()
    a = map(int, input().split())
    first_array = [a[i]+i for i in range(len(a))]
    second_array = [a[i]-i for i in range(len(a))]
    print(max(max(first_array)-min(first_array), max(second_array)-min(second_array)))
    t -= 1
