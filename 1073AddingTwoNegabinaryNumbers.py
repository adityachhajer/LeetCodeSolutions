class Solution:
    def addNegabinary(self, arr1: [int], arr2: [int]) -> [int]:
        result_len = max(len(arr1), len(arr2)) + 2
        # reverse both array
        arr1 = arr1[::-1] + [0] * (result_len - len(arr1))
        arr2 = arr2[::-1] + [0] * (result_len - len(arr2))
        # simply sum, then deal with 2s
        result = [arr1[i] + arr2[i] for i in range(result_len)]

        # note [2, 1] becomes [0, 0]
        #  and [2, 0] becomes [0, 1, 1]
        for i in range(result_len - 2):
            if result[i] >= 2:
                if result[i + 1]:
                    result[i] -= 2
                    result[i + 1] -= 1
                else:
                    result[i] -= 2
                    result[i + 1] += 1
                    result[i + 2] += 1

            # remove extra 0s
        while result != [0] and result[-1] == 0:
            result = result[:-1]

        # reverse again
        return result[::-1]