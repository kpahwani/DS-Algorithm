a1 = map(int, raw_input("Array 1 values: ").split())
a2 = map(int, raw_input("Array 2 values: ").split())

hash_set = set(a1)
for val in a2:
    if val not in hash_set:
        print "Not a subset"

print "Subset"
