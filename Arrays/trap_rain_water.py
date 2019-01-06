def find_water(heights, n):
    max_left = [0]*n
    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = (max(max_left[i-1], heights[i]))

    max_right = [0]*n
    max_right[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        max_right[i] = (max(max_right[i + 1], heights[i]))

    water = 0
    for i in range(n):
        if min(max_left[i], max_right[i]) - heights[i] > 0:
            water += min(max_left[i], max_right[i]) - heights[i]

    return water


input_arr = map(int, raw_input("Enter heights: ").split())
print find_water(heights=input_arr, n=len(input_arr))
