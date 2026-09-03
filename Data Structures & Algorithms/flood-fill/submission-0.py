class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor = image[sr][sc]

        if originalcolor == color:
            return image

        row, col = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color
        directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == originalcolor:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image