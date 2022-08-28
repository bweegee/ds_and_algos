# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != (i + 1):
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swaps += 1
    return swaps
