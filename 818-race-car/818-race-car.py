# https://leetcode.com/problems/race-car/discuss/1512080/Greedy-Approach-oror-Normal-conditions-oror-94-faster-oror-Well-Coded

class Solution:
    def racecar(self, target: int) -> int:

        q = deque()
        q.append((0,0,1))
        while q:
            m,p,s = q.popleft()
            if p==target:
                return m
            rev = -1 if s>0 else 1

            q.append((m+1,p+s,s*2))

            if (p+s<target and s<0) or (p+s>target and s>0):        # If you are back to the target and speed is reverse or if you are ahead of target and speed is positive then reverse the speed
                q.append((m+1,p,rev))

        return -1
