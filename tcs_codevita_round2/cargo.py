from collections import defaultdict

def calculate_manual_shipping_cost(n, conveyor_data, goods, costs, K):
    """
    Calculates the total manual shifting cost for cargo shipping.

    Args:
        n: Number of lines describing the conveyor belt system.
        conveyor_data: List of strings representing the conveyor connections.
        goods: List of flight gates.
        costs: List of manual shipping costs for each item.
        K: Maximum number of switches allowed at any junction.

    Returns:
        Total manual shipping cost.
    """
    # Create a graph for junctions and their connected paths
    graph = defaultdict(list)
    for line in conveyor_data:
        parts = line.split()
        junction = parts[0]
        for connection in parts[1:]:
            graph[junction].append(connection)

    # Track switches at each junction
    junction_switches = defaultdict(int)
    total_manual_cost = 0

    # Iterate through each good and its path
    for good_index, good in enumerate(goods):
        current = good
        path = []

        # Follow the path until we reach the warehouse
        while current != 'warehouse':
            path.append(current)
            # Move to the next junction in the path
            if not graph[current]:
                break  # No outgoing path, handle as error or adjust logic
            current = graph[current][0]
            junction_switches[current] += 1  # Increment switch count for the junction

        # Check if any junction in the path exceeds the switch limit
        for junction in path:
            if junction_switches[junction] > K:
                total_manual_cost += costs[good_index]  # Add manual shipping cost for this good
                break  # Once a manual shift is required, no need to check further junctions

    return total_manual_cost

# User Input
n = int(input("Enter the number of lines describing the conveyor belt system: "))
conveyor_data = []
print("Enter the conveyor belt system details:")
for _ in range(n):
    conveyor_data.append(input())

goods = input("Enter the sequence of gates for the goods, separated by spaces: ").split()
costs = list(map(int, input("Enter the manual shipping costs for each item, separated by spaces: ").split()))
K = int(input("Enter the maximum number of switches allowed at any junction (inclusive): "))

# Calculate the manual shipping cost
result = calculate_manual_shipping_cost(n, conveyor_data, goods, costs, K)
print(f"Total Manual Shifting Cost: {result}")
