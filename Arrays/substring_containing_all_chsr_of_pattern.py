import sys


def find_substring(str, pat):
    len1 = len(str)
    len2 = len(pat)
    if len1 < len2:
        return -1

    hash_str = [0]*255
    hash_pat = [0]*255
    for i in range(len2):
        hash_pat[ord(pat[i])] += 1

    start, statrt_index, min_len = 0, -1, sys.maxsize
    count = 0

    for j in range(len1):
        hash_str[ord(str[j])] += 1

        if hash_pat[ord(str[j])] != 0 and hash_str[ord(str[j])] <= hash_pat[ord(str[j])]:
            count += 1

        if count == len2:
            while hash_str[ord(str[start])] > hash_pat[ord(str[start])] or hash_str[ord(str[start])] == 0:
                if hash_str[ord(str[start])] > hash_pat[ord(str[start])]:
                    hash_str[ord(str[start])] -= 1
                start += 1

            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                statrt_index = start

    return statrt_index, min_len


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        start_index, min_len = find_substring(str1, str2)
        if start_index != -1:
            print(str1[start_index:start_index+min_len])
        else:
            print('-1')
