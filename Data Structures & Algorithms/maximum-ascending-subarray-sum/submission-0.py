class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        total = nums[0]
        
        for i in range(len(nums)):
            if i> 0 and nums[i] <= nums[i - 1]:
                res = nums[i]
            else:
                res += nums[i]
            
            total = max(total, res)
        
        return total