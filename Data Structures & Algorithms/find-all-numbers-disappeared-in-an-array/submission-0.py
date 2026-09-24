class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set1 = set(range(1, n + 1))
        set2= set(nums)

        diff = set1 - set2

        return list(diff)