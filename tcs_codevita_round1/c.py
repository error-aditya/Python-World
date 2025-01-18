import heapq
from math import ceil

# Dijkstra's algorithm to find the shortest path from the office (location 0) to all other locations
def dijkstra(matrix, M):
    distances = [float('inf')] * M
    distances[0] = 0  # Start from the office
    priority_queue = [(0, 0)]  # (distance, location)
    previous_nodes = [-1] * M  # To track the shortest path
    
    while priority_queue:
        current_distance, current_location = heapq.heappop(priority_queue)
        
        # If this is not the shortest distance, skip it
        if current_distance > distances[current_location]:
            continue
        
        for neighbor in range(M):
            if neighbor != current_location:
                distance = matrix[current_location][neighbor]
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_location
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances, previous_nodes

# Function to calculate the minimum number of buses required
def min_buses(M, matrix, employees, bus_capacity):
    # Find the shortest path from the office (location 0) to all other locations
    shortest_distances, previous_nodes = dijkstra(matrix, M)
    
    # Create a dictionary to store employees grouped by their shortest path to the office
    path_employees = {}
    
    # Group employees by their paths
    for location in range(1, M):  # Skip the office location (0)
        path = []
        current = location
        while current != -1:
            path.append(current)
            current = previous_nodes[current]
        
        path.reverse()  # Get the path from office to current location
        path_tuple = tuple(path)  # Use tuple as dictionary key
        
        if path_tuple not in path_employees:
            path_employees[path_tuple] = 0
        path_employees[path_tuple] += employees[location - 1]

    # Calculate buses required for each path
    buses_needed = 0
    for path, total_employees in path_employees.items():
        buses_needed += ceil(total_employees / bus_capacity)  # Round up to nearest whole bus

    return buses_needed

# Input parsing
M = int(input())  # Number of locations (including office)
matrix = [list(map(int, input().split())) for _ in range(M)]  # M*M distance matrix
employees = list(map(int, input().split()))  # Employees at each location (excluding the office)
bus_capacity = int(input())  # Bus capacity

# Output the result
print(min_buses(M, matrix, employees, bus_capacity))
