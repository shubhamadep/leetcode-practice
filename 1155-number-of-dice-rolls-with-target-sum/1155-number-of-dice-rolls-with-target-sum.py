class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9+7

        @lru_cache(None)
        def dp(dice_left: int, target_left: int) -> int:
            if dice_left == 0:
                if target_left == 0:
                    return 1
                return 0
            res = 0
            for i in range(1, k+1):
                res += dp(dice_left-1, target_left-i)
                res %= modulo
            return res % modulo

        return dp(n, target)