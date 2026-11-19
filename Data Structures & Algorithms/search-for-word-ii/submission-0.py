class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        root = {}
        end = "$"

        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[end] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(row, col, parent):
            char = board[row][col]
            node = parent.get(char)
            if node is None:
                return

            # Remove only the terminal marker to avoid duplicate results.
            word = node.pop(end, None)
            if word is not None:
                result.append(word)

            board[row][col] = "#"  # Used in this path only.

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] in node
                ):
                    dfs(nr, nc, node)

            board[row][col] = char

            # No unfound words remain beneath this prefix.
            if not node:
                del parent[char]

        for row in range(rows):
            for col in range(cols):
                if not root:
                    return result
                if board[row][col] in root:
                    dfs(row, col, root)

        return result