class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                left[i] = left[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                right[i] = right[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        
        return -1