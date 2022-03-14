# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/1202992/Python-oror-98-faster-oror-Well-explained-oror-Sliding-Window

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        best = score = sum(cardPoints[:k])
        for i in range(1,k+1):
            score = score - cardPoints[k-i] + cardPoints[-i]
            best = max(best,score)
        return best