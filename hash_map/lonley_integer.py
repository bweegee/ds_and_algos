# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem
def lonelyinteger(a):
    hash = dict()
    for i in range(len(a)):
        hash[a[i]] = hash.get(a[i], 0) + 1
        
    for digit in hash:
        if hash[digit] == 1:
            return digit
