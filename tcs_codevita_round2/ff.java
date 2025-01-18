import java.util.HashSet;
import java.util.Set;

public class ff {

    // Method to get the possible moves for a piece
    public static Set<String> getPieceMoves(char piece, int row, int col) {
        Set<String> moves = new HashSet<>();

        // Queen
        if (piece == 'Q') {
            for (int i = 1; i <= 8; i++) {
                if (row + i <= 8) moves.add((row + i) + "" + (char)(col + 'A'));
                if (row - i >= 1) moves.add((row - i) + "" + (char)(col + 'A'));
                if (col + i <= 7) moves.add(row + "" + (char)(col + i + 'A'));
                if (col - i >= 0) moves.add(row + "" + (char)(col - i + 'A'));
            }
        }
        // Rook
        else if (piece == 'R') {
            for (int i = 1; i <= 8; i++) {
                if (row + i <= 8) moves.add((row + i) + "" + (char)(col + 'A'));
                if (row - i >= 1) moves.add((row - i) + "" + (char)(col + 'A'));
                if (col + i <= 7) moves.add(row + "" + (char)(col + i + 'A'));
                if (col - i >= 0) moves.add(row + "" + (char)(col - i + 'A'));
            }
        }
        // Bishop
        else if (piece == 'B') {
            for (int i = 1; i <= 8; i++) {
                if (row + i <= 8 && col + i <= 7) moves.add((row + i) + "" + (char)(col + i + 'A'));
                if (row - i >= 1 && col - i >= 0) moves.add((row - i) + "" + (char)(col - i + 'A'));
            }
        }

        return moves;
    }

    // Recursive function to calculate unique positions
    public static Set<Set<String>> calculateUniquePositions(Set<String> pieces, int depth) {
        if (depth == 0) {
            Set<Set<String>> baseSet = new HashSet<>();
            baseSet.add(new HashSet<>(pieces)); // Return the current positions as a set
            return baseSet;
        }

        Set<Set<String>> positions = new HashSet<>();

        // For each piece, calculate the new positions it can move to
        for (String piece : pieces) {
            char pieceType = piece.charAt(0);
            int row = Integer.parseInt(piece.substring(1, 2));
            int col = piece.charAt(2) - 'A';

            Set<String> newMoves = getPieceMoves(pieceType, row, col);
            for (String newPosition : newMoves) {
                Set<String> newPieces = new HashSet<>(pieces);
                newPieces.add(newPosition);
                Set<Set<String>> recursivePositions = calculateUniquePositions(newPieces, depth - 1);
                positions.addAll(recursivePositions); // Combine all results from recursion
            }
        }

        return positions;
    }

    public static void main(String[] args) {
        // Example usage
        Set<String> pieces = new HashSet<>();
        pieces.add("QA3");
        int depth = 2;

        Set<Set<String>> uniquePositions = calculateUniquePositions(pieces, depth);
        System.out.println("Number of unique positions: " + uniquePositions.size());
    }
}
