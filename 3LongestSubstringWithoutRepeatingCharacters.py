class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if s == '':
            return 0
        c = 0
        l = []
        d = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in l:
                    c = c + 1
                    l.append(s[j])
                else:
                    if c > d:
                        d = c
                    c = 0
                    l = []
                    break
        return d

