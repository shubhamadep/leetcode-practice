'''

1,5,8,5,7,6,4,3,1

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #search for first decreasing element (a) from the back. 
        lengthNums = len(nums)
        pivot = -1
        
        for i in range(lengthNums - 1):
            if nums[lengthNums - 1 - i] > nums[lengthNums - i - 2]:
                pivot = lengthNums - i - 2       
                break
        
        #if decreasing not found, return ascending order. 
        if pivot == -1 : 
            nums.reverse()
        else:
            #Then search the closest number to a.
            closestValueIndex = pivot+1
            for x in range(pivot+2, lengthNums):
                if nums[x] > nums[pivot]:
                    closestValueIndex = x
                else:
                    break
            # print(closestValueIndex)
            #swap closest value and pivot
            nums[pivot], nums[closestValueIndex] = nums[closestValueIndex], nums[pivot]
            # print(nums, closestValueIndex)
            #reverse the numbers to the right of a.
            self.listReverse(nums, pivot+1, lengthNums)
    
    def listReverse(self, nums, pivot, lengthNums):
        i, j = pivot, lengthNums-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        