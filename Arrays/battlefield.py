# The war goes on.The Knights and the Demons are fighting at their fullest but as expected, the evil is
# dominating the good ones.In order to defeat the Demons the knights have to come together.
# Initially everyone is standing in a circular path at the top of the Demon tower.The warrior
# at index 1 is standing next to warrior at index n and before the warrior at index 2.In order to win
# the fight the knights have to come together.
# The knights have a special power through which they can swap them self with anyone.
# Help the Knights decide the minimum number of swaps they have to do so that all of them stand together.

t = input()
while t:
    n = input()
    arr = raw_input()
    window_len = arr.count('K')
    arr += arr
    count_k = arr[:window_len].count('K')
    max_k = count_k
    for i in range(window_len, 2*n, 1):
        if arr[i] == 'K':
            count_k += 1
        if arr[i - window_len] == 'K':
            count_k -= 1
        max_k = max(count_k, max_k)
    print window_len - max_k
    t -= 1
