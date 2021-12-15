import itertools
from math import inf

def lucky_candies(prizes, k):
    dp = [-inf] * k
    dp[0] = 0
    for x in prizes:
        dp = [max(v, x + dp[(r - x) % k]) for r, v in enumerate(dp)]
    return dp[0]

lucky_candies([1,2,3,4,5], 3)