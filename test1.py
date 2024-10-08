def is_valid(s: str) -> bool:
    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    bracket_stack = []

    for ch in s:
        if ch in bracket_pairs: 
            if not bracket_stack or bracket_stack[-1] != bracket_pairs[ch]:
                return False 
            bracket_stack.pop() 
        else:
            bracket_stack.append(ch) 

    return not bracket_stack


# Example test cases
s = "()"
print(f"Input: {s} Output: {is_valid(s)}")

s = "()[]{}"
print(f"Input: {s} Output: {is_valid(s)}")

s = "(]"
print(f"Input: {s} Output: {is_valid(s)}")
