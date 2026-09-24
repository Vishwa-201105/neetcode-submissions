class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stk = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stk and curr > stk[-1]:
                val = stk.pop()
                idx = nums1idx[val]
                res[idx] = curr
            
            if curr in nums1idx:
                stk.append(curr)
            
        return res
