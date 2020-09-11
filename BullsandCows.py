class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls=0
        cows=0
        i=0
        a=len(secret)
        while(i<a):
            if guess[i]  in secret:
                if guess[i]==secret[i]:
                    bulls+=1
                    secret=secret[:i]+'*'+secret[i+1:]
                    guess = guess[:i] + '*' + guess[i + 1:]
            i+=1
        i=0
        while(i<a):
            if guess[i]  in secret and guess[i] !='*':
                cows += 1
                x=secret.index(guess[i])
                secret=secret[:x]+'*'+secret[x+1:]
            i += 1

        return str(bulls)+'A'+str(cows)+'B'