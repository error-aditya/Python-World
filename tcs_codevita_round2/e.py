from collections import deque

class VaishnaviGame:
    def __init__(self, n, m, matrix, k):
        self.n = n
        self.m = m
        self.matrix = matrix
        self.k = k
        self.start = self.find_start()
        self.visited = [[False] * m for _ in range(n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    def find_start(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == 'S':
                    return (i, j)
        return None
    
    def is_stable(self, x, y):
        if x == self.n - 1:  # Last row is always stable
            return True
        if self.matrix[x][y] == 'B' or self.matrix[x][y] == 'E':
            return True
        return False

    def apply_gravity(self, x, y):
        # Gravity pulls you down if there's no building below you
        while x + 1 < self.n and self.matrix[x + 1][y] != 'B' and self.matrix[x + 1][y] != 'E':
            x += 1
        return x, y

    def bfs(self):
        q = deque([(self.start[0], self.start[1], 0)])  # (x, y, steps)
        self.visited[self.start[0]][self.start[1]] = True
        reachable_cells = []
        
        while q:
            x, y, steps = q.popleft()
            
            # Apply gravity if necessary
            if not self.is_stable(x, y):
                x, y = self.apply_gravity(x, y)
            
            # If it's stable and not in the last row
            if self.is_stable(x, y) and x != self.n - 1:
                reachable_cells.append((x, y, steps))
            
            # Check for all 4 possible movements
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                
                # Move within bounds and ensure we haven't visited
                if 0 <= nx < self.n and 0 <= ny < self.m and not self.visited[nx][ny]:
                    if self.matrix[nx][ny] == 'B' or self.matrix[nx][ny] == 'E':  # Move to B or E
                        if steps + 1 <= self.k:
                            self.visited[nx][ny] = True
                            q.append((nx, ny, steps + 1))
        
        # Sort by Manhattan distance, top-to-bottom, left-to-right order
        reachable_cells.sort(key=lambda x: (-abs(self.start[0] - x[0]) - abs(self.start[1] - x[1]), x[0], x[1]))
        
        return reachable_cells

    def play_game(self):
        reachable_cells = self.bfs()
        
        # Only print the farthest reachable cell within K moves
        farthest_cell = None
        for x, y, steps in reachable_cells:
            if steps <= self.k:
                farthest_cell = (x, y)
                break
        
        if farthest_cell:
            print(farthest_cell[0], farthest_cell[1])

# Input parsing and class usage

N, M = map(int, input().split())
matrix = [input().split() for _ in range(N)]
K = int(input())

# Create the game object
game = VaishnaviGame(N, M, matrix, K)

# Run the game and output the result
game.play_game()
