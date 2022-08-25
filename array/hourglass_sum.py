# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true
def hourglassSum(arr):
    max_sum = -math.inf
    
    def add_hourglass(row, col):
        if col + 2 >= len(arr[0]):
            return -math.inf
        next_max = add_hourglass(row, col + 1)
        sum = 0
        # add top and bottom
        for i in range(0, 3):
            sum += arr[row][i + col] + arr[row + 2][i + col]
        #add middle
        sum += arr[row + 1][col + 1]
        new_max = max(next_max, sum)
        return new_max
    
    for i in range(4):
        max_sum = max(add_hourglass(i, 0), max_sum) 
       
    return max_sum
