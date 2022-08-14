class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n
        
        for i in range(m - 1):
            tempRow = [1] * n
            for j in range(n - 2, -1, -1):
                tempRow[j] = tempRow[j + 1] + row[j]
            row = tempRow
            
        return row[0]
