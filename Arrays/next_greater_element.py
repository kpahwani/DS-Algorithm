from Arrays.special_stack import isEmpty
from Arrays.special_stack import push
from Arrays.special_stack import pop
from Arrays.special_stack import top_of_stack


def next_greater_element(arr):
    stack = [0]
    result = [-1]*len(arr)
    for i in range(1, len(arr)):

        if isEmpty(stack) or arr[top_of_stack(stack)] > arr[i]:
            push(stack, i)
        else:
            while not isEmpty(stack) and arr[top_of_stack(stack)] < arr[i]:
                result[pop(stack)] = arr[i]

            push(stack, i)

    return result


# driver function
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(i) for i in input().split()]
        res = next_greater_element(arr)
        res = ' '.join(map(str, res))
        print(res)
        t -= 1
