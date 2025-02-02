class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0    
        ans_length = 10**5
        sub_array_sum = 0
        for end in range(len(nums)):        
            sub_array_sum += nums[end]                  
            if sub_array_sum >= target and end - start + 1 < ans_length:            
                ans_length = end - start + 1                    
            while sub_array_sum >= target:                  
                sub_array_sum -= nums[start]
                start += 1            
                if sub_array_sum >= target and end - start + 1 < ans_length:                
                    ans_length = end - start + 1                
            
        return 0 if ans_length == 10**5 else ans_length                                                                 