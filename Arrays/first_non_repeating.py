# First non-repeating character using one traversal of string | Set 2

arr = input("Enter the string : ")
chr_arr = [-1]*256

for i in range(len(arr)):
    if chr_arr[ord(arr[i])] == -1:
        chr_arr[ord(arr[i])] = i
    else:
        chr_arr[ord(arr[i])] = -2

rank = len(arr)
for i in range(len(chr_arr)):
    if chr_arr[i] > 0 and chr_arr[i] < rank:
        rank = chr_arr[i]

print(arr[rank])
