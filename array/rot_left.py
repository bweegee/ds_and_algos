# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
def rotLeft(a, d):
    count = d % len(a)
    new_arr = a[count:]
    new_arr.extend(a[0:count])
    return new_arr
