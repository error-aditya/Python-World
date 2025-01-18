from collections import deque

def find_switched_snake_or_ladder(snakes_and_ladders, rolls, final_position):
    # Create a dictionary to store the snakes and ladders
    snakes_and_ladders_dict = {}
    for start, end in snakes_and_ladders:
        snakes_and_ladders_dict[start] = end

    # Create a queue for BFS and add the initial position
    queue = deque([(1, 0)])  # (position, number of rolls)

    # Create a set to store the visited positions
    visited = set()

    while queue:
        position, num_rolls = queue.popleft()

        # If the position is the final position, check if it's reachable
        if position == final_position:
            # If the number of rolls is equal to the number of rolls given, return "Not affected"
            if num_rolls == len(rolls):
                return "Not affected"
            # Otherwise, return the switched snake or ladder
            else:
                for start, end in snakes_and_ladders:
                    if end == position:
                        return f"Ladder {start} {end}"
                    elif start == position:
                        return f"Snake {start} {end}"

        # If the position is not the final position, add the next positions to the queue
        for i in range(1, 7):
            next_position = position + i

            # If the next position is a snake or ladder, move to the corresponding position
            if next_position in snakes_and_ladders_dict:
                next_position = snakes_and_ladders_dict[next_position]

            # If the next position is not visited, add it to the queue and mark it as visited
            if next_position not in visited:
                queue.append((next_position, num_rolls + 1))
                visited.add(next_position)

    # If the final position is not reachable, return "Not reachable"
    return "Not reachable"

# Test the function
n = int(input())  # Number of snakes or ladders
snakes_and_ladders = []
for _ in range(n):
    start, end = map(int, input().split())
    snakes_and_ladders.append((start, end))
rolls = list(map(int, input().split()))
final_position = int(input())
print(find_switched_snake_or_ladder(snakes_and_ladders, rolls, final_position))