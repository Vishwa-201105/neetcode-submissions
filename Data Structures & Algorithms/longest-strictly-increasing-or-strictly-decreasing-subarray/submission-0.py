class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1

        for i in range(n-1):
            curr_len = 1
            for j in range(i + 1, n):
                if nums[j] == nums[j - 1] or((nums[i] < nums[i + 1]) != (nums[j - 1] < nums[j])):
                    break
                curr_len += 1
            
            res = max(res, curr_len)
        
        return res

