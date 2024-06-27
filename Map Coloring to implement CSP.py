# Function to check if the current color assignment is safe for vertex v
def is_safe(graph, color, v, c):
    for i in graph[v]:
        if color[i] == c:
            return False
    return True

# A recursive utility function to solve the map coloring problem
def map_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True
    
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if map_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
            
    return False

# Function to solve the map coloring problem
def map_coloring(graph, m):
    color = [0] * len(graph)
    if not map_coloring_util(graph, m, color, 0):
        return None
    return color

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3  # Number of colors
result = map_coloring(graph, m)

if result:
    print("Solution exists: Following are the assigned colors:")
    for v, c in enumerate(result):
        print(f"Vertex {v} ---> Color {c}")
else:
    print("No solution exists")
