from collections import deque
class TrieNode:
    def __init__(self):
        self.tri_nodes = [None for _ in range(26)]
        self.terminating = False
        self.word = ""
        
    def _next(self, index):
        return self.tri_nodes[index]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def _char_to_index(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            index = self._char_to_index(char)
            if not curr.tri_nodes[index]:
                curr.tri_nodes[index] = TrieNode()
            curr = curr._next(index)
        curr.terminating = True
        curr.word = word
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        q = deque([])
        
        q.append(trie.root)
        result = ''
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for j in range(25, -1, -1):
                    if curr.tri_nodes[j] is not None and curr.tri_nodes[j].terminating:
                        result = curr.tri_nodes[j].word
                        q.append(curr.tri_nodes[j])
        return result