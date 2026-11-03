class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    """
    A Trie is structured as a tree-like data structure where each node contains a hash map (or an array for fixed character sets) to store references to its child nodes, which represent characters. 
    Each node also includes a boolean flag to indicate whether the current node marks the end of a valid word. 
    The Trie starts with a root node that does not hold any character and serves as the entry point for all operations. 
    The child nodes of the root and subsequent nodes represent unique characters from the words stored in the Trie, forming a hierarchical structure based on the prefixes of the words.
    """
    def __init__(self):
        # I am thinking we need the root, boolean flag
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        To insert a word, we iterate through the characters of the word with index i, starting at the root of the Trie as the current node. If the current node already contains word[i], we continue to the next character and move to the node that word[i] points to. If word[i] is not present, we create a new node for word[i] and continue the process until we reach the end of the word. We mark the boolean variable as true as it is the end of the inserted word.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Searching for a word is similar to inserting, but instead of creating new nodes, we return false if we don't find a character in the path while iterating or if the end-of-word marker is not set to true when we reach the end of the word.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        