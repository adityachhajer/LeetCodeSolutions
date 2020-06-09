class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        stack = []
        maxLen = 0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    maxLen = max(i - stack[-1], maxLen)
                else:
                    stack.append(i)

        return maxLen