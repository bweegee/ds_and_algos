class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s): return []
        p_hash, s_hash = {}, {}
        for i in range(len(p)):
            p_hash[p[i]] = 1 + p_hash.get(p[i], 0)
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)

        results = [0] if p_hash == s_hash else []

        left = 0
        for right in range(len(p), len(s)):
            s_hash[s[right]] = 1 + s_hash.get(s[right], 0)
            s_hash[s[left]] -= 1
            
            if s_hash[s[left]] == 0:
                s_hash.pop(s[left])
                
            left += 1

            if s_hash == p_hash:
                results.append(left)

        return results
