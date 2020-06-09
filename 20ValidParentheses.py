class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                try:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                except:
                    return False
            elif i == ']':
                try:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                except:
                    return False
            elif i == '}':
                try:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                except:
                    return False

            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False