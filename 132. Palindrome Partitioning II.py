class Solution:
    def minCut(self, s: str) -> int:


        def isPalindrome(start, end):
            while (start < end):
                if (s[start] != s[end]):
                    return False
                start += 1
                end -= 1
            return True

        n = len(s)
        dp = [n - 1] * n
        dp[0] = 0

        # check for string, result = 0
        if isPalindrome(0, n - 1):
            return 0

        # check for string, result == 1
        # optimization for test case : "aaaaaa....aabbaa.....aaaaaa"
        for i in range(1, len(s)):
            if isPalindrome(0, i - 1) and isPalindrome(i, n - 1):
                return 1

        # check for string, result > 1
        for i in range(1, n):
            for j in range(i + 1):
                if (isPalindrome(j, i)):
                    dp[i] = min(dp[i], dp[j - 1] + 1) if (j > 0) else 0
        return dp[-1]