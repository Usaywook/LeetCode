class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2: return 0
        MAX = 10**5
        min_peak, max_peak = MAX + 1, -MAX - 1
        min_peak_idx, max_peak_idx = -1, N
        start, end = 1, 0
        for i in range(N-1):
            if nums[i] > nums[i+1] and nums[i+1] < min_peak:
                min_peak = nums[i+1]
                min_peak_idx = i+1
        for i in range(min_peak_idx, -1, -1):                
            if nums[i] > min_peak:        
                start = i        
        for i in range(N-1, 0, -1):        
            if nums[i] < nums[i-1] and nums[i-1] > max_peak:
                max_peak = nums[i-1]
                max_peak_idx = i-1                
        for i in range(max_peak_idx, N):        
            if nums[i] < max_peak:                    
                end = i 
        return end - start + 1