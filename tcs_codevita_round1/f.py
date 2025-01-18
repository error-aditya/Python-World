def find_faulty_snake_or_ladder():
    # Input parsing
    N = int(input("Enter number of snakes and ladders: "))  # Number of snakes and ladders
    snakes_and_ladders = {}  # Dictionary to store board changes
    print("Enter the positions of snakes and ladders (format: 'start end'):")
    for _ in range(N):
        start, end = map(int, input().split())
        snakes_and_ladders[start] = end

    print("Enter the die rolls (space-separated):")
    dice_rolls = list(map(int, input().split()))

    final_position = int(input("Enter the final position Chaitra reached: "))

    # Function to simulate the game
    def simulate_game(snakes_and_ladders):
        """Simulates the game based on the current board state."""
        current_position = 1
        for roll in dice_rolls:
            next_position = current_position + roll
            if next_position > 100:
                continue
            # Check if the position has a snake or ladder
            if next_position in snakes_and_ladders:
                next_position = snakes_and_ladders[next_position]
            current_position = next_position
        return current_position

    # Check if the current setup allows reaching the final position
    if simulate_game(snakes_and_ladders) == final_position:
        print("Not affected")
        return

    # Check all possible switches
    for start, end in snakes_and_ladders.items():
        # Copy the original board and switch the current snake/ladder
        modified_board = snakes_and_ladders.copy()
        if start > end:  # Snake -> Ladder
            modified_board[start] = start + (start - end)
        else:  # Ladder -> Snake
            modified_board[start] = start - (end - start)

        # Simulate with the modified board
        if simulate_game(modified_board) == final_position:
            if start > end:
                print(f"Ladder {start} {modified_board[start]}")
            else:
                print(f"Snake {start} {modified_board[start]}")
            return

    # If no switch leads to the final position
    print("Not reachable")

# Run the function
find_faulty_snake_or_ladder()
