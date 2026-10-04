class Solution:
    def compress(self, chars: List[str]) -> int:
        left = length = 0

        while left < len(chars):
            chars[length] = chars[left]
            length += 1
            right = left + 1

            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            
            if right - left > 1:
                for c in str(right - left):
                    chars[length] = c
                    length += 1
            
            left = right
        
        return length