from collections import defaultdict
class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board:
            return []

        M, N = len(board), len(board[0])
        res = []
        wordtrie = Trie(words)

        for i in range(M):
            for j in range(N):
                dfs(board, i, j, wordtrie.root, "", res)

        return sorted(res)

def dfs(board, i, j, node, path, res):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return

    node = node.children.get(board[i][j], None)

    if node is None:
        return

    path += board[i][j]

    if node.isword:
        res.append(path)
        node.isword = False

    temp = board[i][j]
    board[i][j] = "."
    dfs(board, i+1, j, node, path, res)
    dfs(board, i-1, j, node, path, res)
    dfs(board, i, j+1, node, path, res)
    dfs(board, i, j-1, node, path, res)
    board[i][j] = temp
    return

class TrieNode():
    def __init__(self):
        self.isword = False
        self.children = collections.defaultdict(TrieNode)

class Trie():
    def __init__(self, words=[]):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isword = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w, None)
            if node is None:
                return False
        return node.isword
