class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        c = pattern
        str_list = str.split(" ")
        if len(c) != len(str_list):
            return False
        s = ''
        k = []
        p = []
        for i in str:
            if i != " ":
                s = s + i
            else:
                if s not in k:
                    k.append(s)
                    p.append(s)
                    s = ""

                else:
                    p.append(s)
                    s = ""
        if s not in k:
            k.append(s)
            p.append(s)
        else:
            p.append(s)

        t = {}

        if len(set(c)) == len(k):
            for i in range(0, len(c)):
                if c[i] not in t.keys():
                    t[c[i]] = p[i]
                else:
                    if t[c[i]] != p[i]:
                        return False

        else:
            return False
        return True


