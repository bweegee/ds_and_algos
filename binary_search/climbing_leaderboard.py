# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
def climbingLeaderboard(ranked, player):
    # Write your code here
    ranks = sorted(list(set(ranked)), reverse=True)
    results = []
    for i in range(len(player)):
        left = 0
        right = len(ranks) - 1
        while left < len(ranks) and ranks[left] > player[i]:
            mid = (left + right)//2
            if ranks[mid] > player[i]:
                left = mid + 1
            else:
                right = mid
        results.append(left + 1)
    
    return results
