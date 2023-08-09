from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class WordSearch:
    def findWords(self, board: List[List[str]], root: TrieNode) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        # Directions for up, down, left, right, and the four diagonals
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


def populateTrie(root):
    f = open("wordlist.txt", "r")
    for line in f:
        root.addWord(line.strip())


def inputBoard():
    print(
        "Input board rows one-by-one.\
        Use Enter to switch to the next row.\
        Type 'done' when finished."
    )

    board = []
    while True:
        row_str = input("Enter row: ")
        if row_str.lower() == "done":
            break
        board.append(list(row_str))

    return board


def main():
    board = inputBoard()
    # print board nicely
    for row in board:
        print(row)

    root = TrieNode()
    populateTrie(root)
    ws = WordSearch()
    print(ws.findWords(board, root))


main()
