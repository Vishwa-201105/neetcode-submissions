class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        count = 1

        for c in arr:
            freq[c] = freq.get(c, 0) + 1
        
        for c, i in freq.items():
            if i == 1 and count == k:
                return c
            elif i == 1:
                count += 1

        return ""
            