# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        dict_brackets = {')': '(', '}': '{', ']': '['}
        currents = deque([])
        
        for w in s:
            if w not in dict_brackets:
                currents.append(w)
            else:
                if len(currents) < 1 or currents[-1] != dict_brackets[w]:
                    return False
                currents.pop()
        
        return len(currents) == 0