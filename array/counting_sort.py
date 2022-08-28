# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem
def countingSort(arr):
    result = [0] * 100
    for i in range(len(arr)):
        result[arr[i]] += 1
    return result
