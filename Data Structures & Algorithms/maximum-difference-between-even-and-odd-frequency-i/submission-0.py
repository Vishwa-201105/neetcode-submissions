class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        max_odd = 0
        min_even = len(s)
        for freq in count.values():
            if freq % 2 == 0:
                min_even = min(min_even, freq)
            else:
                max_odd = max(max_odd, freq)
        
        return max_odd - min_even