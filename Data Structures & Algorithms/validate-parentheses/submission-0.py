class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stk.append(s[i])
            
            else:
                if not stk:
                    return False
                top = stk.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
            
        return len(stk) == 0
