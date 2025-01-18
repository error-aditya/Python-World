import heapq

# Dijkstra's algorithm to find the shortest path from the office (location 0) to all other locations
def dijkstra(matrix, M):
    distances = [float('inf')] * M
    distances[0] = 0  # Start from the office
    priority_queue = [(0, 0)]  # (distance, location)
    
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
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances

# Function to calculate the minimum number of buses required
def min_buses(M, matrix, employees, bus_capacity):
    # Find the shortest path from the office (location 0) to all other locations
    shortest_distances = dijkstra(matrix, M)
    
    # Initialize the total number of people and buses needed
    total_people = 0
    for location in range(1, M):  # Ignore the office location (0)
        total_people += employees[location - 1]  # Employees at each location
    
    # Calculate the minimum number of buses required
    buses_needed = (total_people + bus_capacity - 1) // bus_capacity  # Round up the division
    
    return buses_needed

# Input parsing
M = int(input())  # Number of locations (including office)
matrix = [list(map(int, input().split())) for _ in range(M)]  # M*M distance matrix
employees = list(map(int, input().split()))  # Employees at each location (excluding the office)
bus_capacity = int(input())  # Bus capacity

# Output the result
print(min_buses(M, matrix, employees, bus_capacity))
