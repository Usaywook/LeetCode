class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, q, r = 0, 0, len(nums) - 1
    
        while q <= r:        
            if nums[q] == 0:            
                nums[p], nums[q] = nums[q], nums[p]                            
                p += 1                    
                q += 1                 
            elif nums[q] == 2:            
                nums[r], nums[q] = nums[q], nums[r]                
                r -= 1                 
            else:
                q += 1
        return nums