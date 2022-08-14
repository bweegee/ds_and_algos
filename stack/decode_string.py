class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                #get string to repeat
                substring = ''
                while stack[-1] != '[':
                    char = stack.pop()
                    substring = char + substring
                #pop opening bracket
                stack.pop()

                #get amount to multiply by
                count = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    count = digit + count

                stack.append(int(count) * substring)

        return ''.join(stack)
