# idea: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/1581292/Well-Explained-oror-Thought-process-oror-94-faster

# great template for binary search questions: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/769698/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def feasible(capacity):
            days = 1
            tempCapacity = 0
            
            for w in weights:
                tempCapacity += w
                if tempCapacity > capacity:
                    tempCapacity = w
                    days += 1
                    if days > D:
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right-left) // 2
            if feasible(mid):
                right = mid-1
            else:
                left = mid+1
        return left