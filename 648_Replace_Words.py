class TrieNode:
    def __init__(self):
        self.tri_nodes = [None for _ in range(26)]
        self.terminating = False
        
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
        
    def search(self, word):
        found_word = ""
        curr = self.root
        for char in word:
            index = self._char_to_index(char)
            if not curr.tri_nodes[index]:
                break
            curr = curr._next(index)
            found_word+=char
            if curr.terminating:
                return found_word
        return word
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        res = []
        
        sentence = sentence.split(" ")
        
        for word in sentence:
            found_word = trie.search(word)
            res.append(found_word)
        return " ".join(res)
            
        