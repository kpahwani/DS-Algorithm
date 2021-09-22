from math import floor
import logging
import os

logging.basicConfig(level=logging.INFO)

def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

def binary_search(arr,l,r,k):
    # The array has to be sorted
    # On the similar grounds we have interpolation, exponential, ternary search
    if r<l:
        return -1
    m = floor((r-l)/2)
    if arr[m] == k:
        return m
    elif arr[m] < k:
        return binary_search(arr, m+1, r, k)
    else:
        return binary_search(arr, l, m-1, k)

def jump_search(test_arr, test_val):
    # The array has to be sorted
    arr_len = len(test_arr)
    jump = floor(pow(arr_len,0.5))
    m = jump
    while test_val > test_arr[m] and m < arr_len:
        m += jump
    if m >= arr_len:
        return - 1
    
    return linear_search(test_arr[m-jump:jump+1], test_val)
        

def test_helper(fun, test_arr, test_val):
    logging.info(f"Testing {fun.__name__}: Find {test_val} in {test_arr}")
    if fun == binary_search:
        res = fun(test_arr, 0, len(test_arr) - 1, test_val)
    else:
        res = fun(test_arr, test_val)
    if res != -1:
        logging.info(f"Found value: {test_val} at position {res + 1}")
    else:
        logging.info(f"Value {test_val} not found in {test_arr}")
        
if __name__ == "__main__":
    test_arr, test_val = [1,2,1,4,6,2,7,8,9,13,4,5,-1,30,21,-5,21,45,6,15], 2
    # test_helper(linear_search, test_arr=test_arr, test_val=test_val)
    # test_helper(binary_search, test_arr=sorted(test_arr), test_val=test_val)
    test_helper(jump_search, test_arr=sorted(test_arr), test_val=test_val)