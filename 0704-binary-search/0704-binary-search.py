class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.RecursiveBS(nums, 0, len(nums)-1, target)

    def RecursiveBS(self, arr, low, high, x):
        if high < low:
            return -1
        else:
            mid = low + (high - low) // 2
            if arr[mid] ==  x:
                return mid
            elif arr[mid] > x:
                return self.RecursiveBS(arr, low, mid-1, x)
            else:
                return self.RecursiveBS(arr, mid+1, high, x)
    
    def IterativeBS(self, arr, low, high, x):
        while low <= high:
            mid  = low + (high - low) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1