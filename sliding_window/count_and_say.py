class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        if n <= 0: return ""
        def count_and_say(n):
            if n == 1:
                return "1"
            prev_say = count_and_say(n - 1)
            
            left = 0
            count = 0
            new_say = ""
            for right in range(len(prev_say)):
                if prev_say[left] != prev_say[right]:
                    new_say += str(count) + prev_say[left]
                    count = 0
                    left = right
                count += 1
            # catch the final count and char
            new_say += str(count) + prev_say[left]
            return new_say
        
        return count_and_say(n)
