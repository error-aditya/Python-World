def extract_shapes(R, C, S, N, lines):
    # Step 1: Initialize a grid to track occupied cells (True if covered by a shape)
    grid = [[False] * C for _ in range(R)]
    
    # Step 2: Mark the grid based on lines (representing shapes)
    for x1, y1, x2, y2 in lines:
        # Ensure the coordinates are within bounds (0 <= x < C, 0 <= y < R)
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        
        if x1 == x2:  # vertical line
            for y in range(y1, y2 + 1):
                if 0 <= x1 < C and 0 <= y < R:
                    grid[y][x1] = True
        elif y1 == y2:  # horizontal line
            for x in range(x1, x2 + 1):
                if 0 <= x < C and 0 <= y1 < R:
                    grid[y1][x] = True

    # Debug: Print grid to see if shapes are marked correctly
    print("Grid after marking shapes:")
    for row in grid:
        print(row)
    
    # Step 3: Iterate through possible block placements
    def can_place_block(x, y):
        # Check if the block can be placed at (x, y)
        if x + S > C or y + S > R:
            return False  # Out of bounds
        for i in range(y, y + S):
            for j in range(x, x + S):
                if i >= R or j >= C or not grid[i][j]:  # Block doesn't cover the shape
                    return False
        return True

    total_area_extracted = 0
    placements = 0
    extracted = [[False] * C for _ in range(R)]
    
    while True:
        max_area = 0
        best_x, best_y = -1, -1
        
        # Find the best block placement (maximize extraction)
        for x in range(C - S + 1):
            for y in range(R - S + 1):
                if can_place_block(x, y):
                    # Count the number of cells that can be extracted
                    area = 0
                    for i in range(y, y + S):
                        for j in range(x, x + S):
                            if not extracted[i][j]:
                                area += 1
                    
                    # Maximize the area extracted
                    if area > max_area:
                        max_area = area
                        best_x, best_y = x, y
                    elif area == max_area:
                        if y < best_y or (y == best_y and x < best_x):
                            best_x, best_y = x, y
        
        # If no valid placement is found, we're done
        if max_area == 0:
            break
        
        # Mark the area as extracted
        for i in range(best_y, best_y + S):
            for j in range(best_x, best_x + S):
                extracted[i][j] = True
        
        total_area_extracted += max_area
        placements += 1
    
    return placements, total_area_extracted

# Read inputs
C, R = map(int, input().split())
S = int(input())
N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

# Calculate the result
result = extract_shapes(R, C, S, N, lines)
print(result[0], result[1])
