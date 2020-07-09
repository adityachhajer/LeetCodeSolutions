class Solution:
    def solve(self, S, output, res):
        if S == '':
            res.append(output)
            return
        if S[0].isdigit():
            output = output + str(S[0])
            S = S[1:]
            self.solve(S, output, res)
        else:
            output1 = output + S[0].lower()
            output2 = output + S[0].upper()
            S = S[1:]
            self.solve(S, output1, res)
            self.solve(S, output2, res)

    def letterCasePermutation(self, S: str) -> List[str]:
        output = ''
        res = []
        self.solve(S, output, res)
        return res
