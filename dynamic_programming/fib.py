class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dp(n, hash):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if hash.has_key(n):
                return hash[n]
            sum = dp(n - 1, hash) + dp(n - 2, hash)
            hash[n] = sum
            return sum
        return dp(n, {})
