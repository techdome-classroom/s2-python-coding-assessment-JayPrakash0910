class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for curr in s:
            if curr in bracket_map: 
                stack.append(curr)
            elif curr in bracket_map.values(): 
                if stack and bracket_map[stack[-1]] == curr:
                    stack.pop() 
                else:
                    return False  
        return not stack 
        
solution = Solution()
s = input("Enter a string of parentheses: ")
print(solution.isValid(s))
