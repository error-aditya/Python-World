def simulate_path(board, rolls):
    """
    Simulates the player's path based on the dice rolls and the board configuration.
    """
    position = 1  # Start at position 1
    for roll in rolls:
        position += roll
        if position > 100:
            position = 100  # Cap the position at 100
        position = board[position]  # Apply the snake/ladder effect
        if position == 100:
            break  # Stop if we reach cell 100
    return position

def find_switched_snake_or_ladder(snakes_and_ladders, rolls, final_position):
    # Create the initial board (1 to 100), no snakes or ladders
    board = list(range(101))  # Default: board[i] = i (no snake or ladder)
    
    # Apply the snakes and ladders to the board
    for start, end in snakes_and_ladders.items():
        board[start] = end
    
    # Simulate the path with the original board
    original_position = simulate_path(board, rolls)
    
    # If the original position is the same as the final position, it's stable, no need for switching
    if original_position == final_position:
        return "Not affected"
    
    # Try switching each snake and ladder and check the result
    for start, end in snakes_and_ladders.items():
        # If it's a snake (start > end), try switching with a ladder
        if end < start:
            for other_start, other_end in snakes_and_ladders.items():
                # If it's a ladder (start < end), try switching with a snake
                if other_end > other_start:
                    # Create a new board with the swapped snake and ladder
                    modified_board = board[:]
                    modified_board[start] = other_end  # Swap the snake with the ladder
                    modified_board[other_start] = end  # Swap the ladder with the snake
                    
                    # Simulate the modified path with the new board
                    modified_position = simulate_path(modified_board, rolls)
                    
                    # If after the switch, the final position matches the expected final position
                    if modified_position == final_position:
                        if end < start:  # It was a snake
                            return f"snake {start} {other_end}"
                        else:  # It was a ladder
                            return f"ladder {other_start} {end}"
    
    # If after all switches the final position is still not reachable, return "Not reachable"
    return "Not reachable"

# Input reading and processing
n = int(input())  # Number of snakes or ladders
snakes_and_ladders = {}

# Read the snakes and ladders
for _ in range(n):
    start, end = map(int, input().split())
    snakes_and_ladders[start] = end

# Read the dice rolls
rolls = list(map(int, input().split()))

# Read the final position
final_position = int(input())

# Run the function and print the result
print(find_switched_snake_or_ladder(snakes_and_ladders, rolls, final_position))
