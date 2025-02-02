class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        k = (i + j) // 2        
        while i < j:        
            if nums[k] < nums[k+1]:
                i = k + 1            
            else:
                j = k
            k = (i + j) // 2                  
        return j