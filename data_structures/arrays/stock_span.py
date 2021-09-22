from Arrays.special_stack import isEmpty
from Arrays.special_stack import push
from Arrays.special_stack import pop
from Arrays.special_stack import top_of_stack


def calculate_stock_span(stock_price):
    stock_stack = []
    push(stock_stack, 0)
    result_span = [1]*len(stock_price)
    for i in range(1, len(stock_price)):
        while not isEmpty(stock_stack) and stock_price[top_of_stack(stock_stack)] < stock_price[i]:
            pop(stock_stack)

        result_span[i] = i + 1 if isEmpty(stock_stack) else i - top_of_stack(stock_stack)

        push(stock_stack, i)

    return result_span


# driver function
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [int(i) for i in input().split()]
        res = calculate_stock_span(arr)
        res = ' '.join(res)
        print(res)
        t -= 1
