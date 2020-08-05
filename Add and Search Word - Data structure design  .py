class WordDictionary:

    def __init__(self):
        self.words = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        for w in self.words[len(word)]:
            for i, c in enumerate(word):
                if c not in ['.', w[i]]: break
            else:
                return True
        return False