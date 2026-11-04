class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adding a word follows the standard Trie insertion process. 
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        """
        We traverse the word with index i, starting at the root of the Trie. 
        For normal characters, we search as usual. When encountering a dot ('.'), we try all possible characters by recursively extending the search in each direction. 
        If any path leads to a valid word, we return true; otherwise, we return false. 
        Although we try all paths for a dot, the time complexity is still O(n) because there are at most two dots ('.') in the word, making the complexity O((26^2) * n).
        """
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
