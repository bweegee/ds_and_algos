class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        hash = {}
        secret = list(secret)
        guess = list(guess)
        for i in range(len(secret) - 1, -1, -1):
            if secret[i] == guess[i]:
                bulls += 1
                guess.pop(i)
            elif hash.has_key(secret[i]):
                hash[secret[i]] += 1
            else:
                hash[secret[i]] = 1
        
        for i in range(len(guess)):
            if hash.has_key(guess[i]) and hash[guess[i]] > 0:
                cows += 1
                hash[guess[i]] -= 1
        
        return str(bulls) + 'A' + str(cows) + 'B'
