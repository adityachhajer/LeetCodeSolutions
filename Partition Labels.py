class Solution:
    def partitionLabels(self, S):
        ends = {c: i for i, c in enumerate(S)}
        curr, out = 0, [0]

        while curr < len(S):
            last = ends[S[curr]]
            while curr <= last:
                symb = S[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)

        return [out[i] - out[i - 1] for i in range(1, len(out))]
