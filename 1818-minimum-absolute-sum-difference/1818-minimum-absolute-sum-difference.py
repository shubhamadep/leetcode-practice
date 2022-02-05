class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sortedNums1 = sorted(nums1)
        total = 0
        for i in range(len(nums1)):
            total += abs(nums1[i] - nums2[i])
        
        #returns target or next largest element if target not found which could be a fit. 
        def binarySearch(arr, target):
            start, end = 0, len(arr) - 1
            while start <= end:
                mid = start + (end - start) // 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return start
        
        length = len(nums1)
        best = total
        for x, y in zip(nums1, nums2):
            diff = abs(x - y)
            possibleFit = binarySearch(sortedNums1, y)
            
                
            if 0 <= possibleFit < length:
                potentialVal = sortedNums1[possibleFit]
                potentialSum = total - diff + abs(potentialVal - y)
                best = min(potentialSum, best)
            
            if possibleFit - 1 < length:
                potentialVal = sortedNums1[possibleFit-1]
                potentialSum = total - diff + abs(potentialVal -y)
                best = min(potentialSum, best)
        
        return best % (10 ** 9 + 7)
            
        