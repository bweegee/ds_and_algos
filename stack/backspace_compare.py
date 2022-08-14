class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []

        for i in range(max(len(s), len(t))):
            if i <= len(s) - 1:
                if s[i] != '#': s_stack.append(s[i])
                elif len(s_stack) > 0: s_stack.pop()

            if i <= len(t) - 1:
                if t[i] != '#': t_stack.append(t[i])
                elif len(t_stack) > 0: t_stack.pop()

        return ''.join(s_stack) == ''.join(t_stack)
