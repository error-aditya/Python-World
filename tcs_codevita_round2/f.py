from collections import defaultdict

def get_piece_moves(piece, row, col):
    """
    Calculates the possible moves for a given piece.

    Args:
        piece: The type of piece ('Q', 'R', or 'B').
        row: The current row of the piece (1-indexed).
        col: The current column of the piece (A-H, converted to 0-indexed).

    Returns:
        A set of possible move coordinates (row, col).
    """
    moves = set()
    if piece == 'Q':  # Queen
        # Diagonal moves
        for i in range(1, 8):
            if 1 <= row + i <= 8 and 0 <= col + i < 8:
                moves.add((row + i, col + i))
            if 1 <= row - i <= 8 and 0 <= col - i < 8:
                moves.add((row - i, col - i))
            if 1 <= row + i <= 8 and 0 <= col - i < 8:
                moves.add((row + i, col - i))
            if 1 <= row - i <= 8 and 0 <= col + i < 8:
                moves.add((row - i, col + i))
        # Horizontal and vertical moves
        for i in range(1, 8):
            if 1 <= row + i <= 8:
                moves.add((row + i, col))
            if 1 <= row - i <= 8:
                moves.add((row - i, col))
            if 0 <= col + i < 8:
                moves.add((row, col + i))
            if 0 <= col - i < 8:
                moves.add((row, col - i))
    elif piece == 'R':  # Rook
        for i in range(1, 8):
            if 1 <= row + i <= 8:
                moves.add((row + i, col))
            if 1 <= row - i <= 8:
                moves.add((row - i, col))
            if 0 <= col + i < 8:
                moves.add((row, col + i))
            if 0 <= col - i < 8:
                moves.add((row, col - i))
    elif piece == 'B':  # Bishop
        for i in range(1, 8):
            if 1 <= row + i <= 8 and 0 <= col + i < 8:
                moves.add((row + i, col + i))
            if 1 <= row - i <= 8 and 0 <= col - i < 8:
                moves.add((row - i, col - i))
            if 1 <= row + i <= 8 and 0 <= col - i < 8:
                moves.add((row + i, col - i))
            if 1 <= row - i <= 8 and 0 <= col + i < 8:
                moves.add((row - i, col + i))
    return moves

def calculate_unique_positions(pieces, depth):
    """
    Calculates the number of unique chessboard positions.

    Args:
        pieces: A list of strings representing the positions of the pieces.
        depth: The depth of the search.

    Returns:
        The number of unique chessboard positions.
    """

    if depth == 0:
        return 1

    positions = set()

    # For each piece, calculate the new positions it can move to.
    for i, piece_str in enumerate(pieces):
        piece = piece_str[0]
        col = ord(piece_str[1]) - ord('A')
        row = int(piece_str[2])

        for new_row, new_col in get_piece_moves(piece, row, col):
            new_pieces = pieces.copy()
            new_pieces[i] = f"{piece}{chr(new_col + ord('A'))}{new_row}" 
            positions.add(tuple(new_pieces))  # Store positions as tuples for hashability

    if depth > 1:
        next_positions = set()
        for new_position in positions:
            # Correctly call the recursive function and update next_positions
            next_positions.update(calculate_unique_positions(list(new_position), depth - 1))

        # After calculating positions for depth-1, accumulate all the results in the original set.
        positions.update(next_positions)

    return len(positions)

if __name__ == "__main__":
    pieces = input("Enter the positions of the pieces (e.g., QA3 RB3): ").split()
    depth = int(input("Enter the depth (d): "))

    unique_positions = calculate_unique_positions(pieces, depth)
    print(f"Number of unique positions: {unique_positions}")
