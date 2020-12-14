# You are given a parentheses sequence, check if it's regular.

# Example

#     For s = "()()(())", the output should be
#     validParenthesesSequence(s) = true;
#     For s = "()()())", the output should be
#     validParenthesesSequence(s) = false.

def validParenthesesSequence(s):
    opening = "{[("
    closing = "}])"
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0