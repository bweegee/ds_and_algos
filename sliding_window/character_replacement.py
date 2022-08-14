class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hash = {}
        results = 0

        left = 0
        max_char_counter = 0
        for right in range(len(s)):
            hash[s[right]] = 1 + hash.get(s[right], 0)
            max_char_counter = max(max_char_counter, hash[s[right]])

            # window length - most repeated charcter = amt to change
            # move left pointer until it's equal to k
            while((right - left + 1) - max_char_counter > k):
                hash[s[left]] -= 1
                left += 1

            results = max(max_char_counter, right - left + 1)

        return results
