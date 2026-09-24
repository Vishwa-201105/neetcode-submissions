class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        count = 0

        for c in arr:
            freq[c] = freq.get(c, 0) + 1
        
        for c in freq:
            if freq[c] == 1:
                count += 1
                if count == k:
                    return c
        
        if count < k:
            return ""
            