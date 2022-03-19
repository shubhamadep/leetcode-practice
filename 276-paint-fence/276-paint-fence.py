'''

number of ways to color 2 fence = k * k
number of ways to color a fence without same color as previous fence = k-1 * number of ways to paint prev fence
nmber of ways to color prev fence without same color as fence i - 2 = k-1 * number of ways to paint i-2nd fence

Combining equations = (k-1) * (dp(i-1) + dp(i-2))

def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        dp = [0] * (n+1)
        dp[1] = k
        dp[2] = k*k

        for i in range(3, n+1):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])

        return dp[-1]
        

'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        two_posts_back = k
        one_post_back = k * k
        
        for i in range(3, n + 1):
            curr = (k - 1) * (one_post_back + two_posts_back)
            two_posts_back = one_post_back
            one_post_back = curr

        return one_post_back