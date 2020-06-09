# class Solution(object):
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()

import collections
s=["eat","tea","tan","ate","nat","bat"]
ans=collections.defaultdict(list)
for i in s:
    ans[tuple(sorted(i))].append(i)
print(ans.values())