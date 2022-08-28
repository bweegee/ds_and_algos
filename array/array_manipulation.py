def arrayManipulation(n, queries):
    max_sum = -math.inf
    arr = [0] * n
    for i in range(len(queries)):
        arr[queries[i][0]] = queries[i][2]
        arr[queries[i][1]] = -abs(queries[i][2])

    for i in range(len(arr)):
        max_sum = max(max_sum, arr[i])

    return max_sum
