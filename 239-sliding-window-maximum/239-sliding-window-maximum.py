class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        i, j = 0, 0
        size = len(nums)
        ans = []
        
        while j < size:
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
                
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                ans.append(queue[0])
                if queue and nums[i] == queue[0]:
                    queue.popleft()
                i += 1
                j += 1
        
        return ans
        