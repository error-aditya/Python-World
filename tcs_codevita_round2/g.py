def get_new_position(position, move):
    """
    Get the new position based on the move.
    """
    y, x, z = position
    if move == 'u':  # up
        return (y - 1, x, z)
    elif move == 'd':  # down
        return (y + 1, x, z)
    elif move == 'f':  # front
        return (y, x + 1, z)
    elif move == 'b':  # back
        return (y, x - 1, z)
    elif move == 'l':  # left
        return (y, x, z - 1)
    elif move == 'r':  # right
        return (y, x, z + 1)

def simulate_band(start_pos, moves, S):
    """
    Simulate the path of a band inside a 3D matrix and return the occupied positions.
    """
    occupied = set()
    current_pos = start_pos
    occupied.add(current_pos)
    
    for move in moves:
        new_pos = get_new_position(current_pos, move)
        
        # Check if the new position is within the bounds
        if not (0 <= new_pos[0] < S and 0 <= new_pos[1] < S and 0 <= new_pos[2] < S):
            raise ValueError("Out of bounds move detected")
        
        # Add the new position to the occupied set
        occupied.add(new_pos)
        
        # Update the current position
        current_pos = new_pos
        
    return occupied

def calculate_maximum_cells_band_above_other(band1, band2):
    """
    Calculate the maximum number of cells one band is above the other.
    """
    max_cells = 0
    for pos1 in band1:
        count = sum(1 for pos2 in band2 if pos2[0] < pos1[0] and pos2[1] == pos1[1] and pos2[2] == pos1[2])
        max_cells = max(max_cells, count)
    
    return max_cells

def main():
    # Read inputs
    S = int(input())  # Size of the cube
    band1_start = tuple(map(int, input().split()))  # Starting position of Band 1
    band1_moves = input().strip()  # Movement sequence of Band 1
    band2_start = tuple(map(int, input().split()))  # Starting position of Band 2
    band2_moves = input().strip()  # Movement sequence of Band 2
    
    # Simulate the movement of the bands
    try:
        band1_occupied = simulate_band(band1_start, band1_moves, S)
        band2_occupied = simulate_band(band2_start, band2_moves, S)
    except ValueError:
        print("Impossible")
        return
    
    # Check if the bands are interlocked
    if band1_occupied & band2_occupied:
        print("Impossible")
        return
    
    # Calculate the maximum number of cells one band is above the other
    max_cells = calculate_maximum_cells_band_above_other(band1_occupied, band2_occupied)
    
    # Output the result
    print(max_cells)

# Entry point for the program
if __name__ == "__main__":
    main()
