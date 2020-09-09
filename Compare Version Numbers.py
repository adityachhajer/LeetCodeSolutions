class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = re.sub('^0*', '', version1)
        version2 = re.sub('^0*', '', version2)

        v1 = version1.split('.')
        v2 = version2.split('.')

        len1 = len(v1)
        len2 = len(v2)

        i = 0
        length = max(len1, len2)
        if len1 != len2:
            if len1 < len2:
                sublist = ('0 ' * (len2 - len1)).split()
                v1 = v1 + sublist
            else:
                sublist = ('0 ' * (len1 - len2)).split()
                v2 = v2 + sublist
        for i in range(0, length):
            if v1[i] == '': v1[i] = '0'
            if v2[i] == '': v2[i] = '0'

            if int(v1[i]) > int(v2[i]):
                return 1
                break
            elif int(v1[i]) < int(v2[i]):
                return -1
                break
            i += 1
        return 0

