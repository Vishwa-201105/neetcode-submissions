class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in comp_map:
                return [comp_map[comp], i]
            comp_map[num] = i
    